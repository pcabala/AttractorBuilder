
# Blender 4.x — Attractor builder (panel + operator)
bl_info = {
    "name": "Attractor Builder",
    "author": "Pawel Cabala",
    "version": (1, 8, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > Attractor",
    "description": "Generate and visualize 3D chaotic attractors.",
    "doc_url": "https://github.com/pcabala/AttractorBuilder",
    "license": "GPL-2.0-or-later",
    "category": "Add Curve",
}

# ==========================================================================
# 1. Imports
# ==========================================================================
import bpy
from mathutils import Vector, Matrix
import functools
import math
import operator
import ast
import json
import os
import time
import textwrap


def _addon_dir():
    """Returns the installation directory of this addon."""
    return os.path.dirname(os.path.abspath(__file__))


def _get_user_data_path():
    """
    Returns the full, writable path for the user's custom attractors library.
    This is the correct, safe location that persists across updates.
    """
    user_config_dir = bpy.utils.user_resource('CONFIG', create=True)    
    addon_data_dir = os.path.join(user_config_dir, "AttractorBuilder")
    return os.path.join(addon_data_dir, "custom_attractors.json")


# ==========================================================================
# 2. Global Caches & State
# ==========================================================================

_original_curve_cache = {}
_simplify_source_cache = {}
_working_curve_cache = {}
_smooth_source_cache = {}
_raw_points = []
_raw_dts = []


# ==========================================================================
# 3. Core Mathematics (Numerical Integration Steppers)
# ==========================================================================

def step_euler(rhs_func, p: Vector, params: dict, dt: float) -> Vector:
    """Performs a single Forward Euler integration step."""
    return p + rhs_func(p, params) * dt


def step_heun(rhs_func, p: Vector, params: dict, dt: float) -> Vector:
    """Performs a single Heun's method (RK2) integration step."""
    p_pred = p + rhs_func(p, params) * dt
    avg_slope = 0.5 * (rhs_func(p, params) + rhs_func(p_pred, params))
    return p + avg_slope * dt


def step_rk4(rhs_func, p: Vector, params: dict, dt: float) -> Vector:
    """Performs a single Runge-Kutta 4th order integration step."""
    k1 = rhs_func(p, params)
    k2 = rhs_func(p + k1 * (0.5 * dt), params)
    k3 = rhs_func(p + k2 * (0.5 * dt), params)
    k4 = rhs_func(p + k3 * dt, params)
    return p + (dt / 6.0)*(k1 + k2 * 2.0 + k3 * 2.0 + k4)


def step_rkf45(rhs_func, p: Vector, params: dict, current_dt: float, tolerance: float):
    """Performs an adaptive Runge-Kutta-Fehlberg 4(5) step."""
    A = [
        [], [1/4], [3/32, 9/32], [1932/2197, -7200/2197, 7296/2197],
        [439/216, -8, 3680/513, -845/4104],
        [-8/27, 2, -3544/2565, 1859/4104, -11/40]
    ]
    B_star = [25/216, 0, 1408/2565, 2197/4104, -1/5, 0]
    B = [16/135, 0, 6656/12825, 28561/56430, -9/50, 2/55]

    k1 = rhs_func(p, params)
    k2 = rhs_func(p + A[1][0] * current_dt * k1, params)
    k3 = rhs_func(p + current_dt * (A[2][0]*k1 + A[2][1]*k2), params)
    k4 = rhs_func(p + current_dt * (A[3][0]*k1 + A[3][1]*k2 + A[3][2]*k3), params)
    k5 = rhs_func(p + current_dt * (A[4][0]*k1 + A[4][1]*k2 + A[4][2]*k3 + A[4][3]*k4), params)
    k6 = rhs_func(p + current_dt * (A[5][0]*k1 + A[5][1]*k2 + A[5][2]*k3 + A[5][3]*k4 + A[5][4]*k5), params)

    y4 = p + current_dt * (B_star[0]*k1 + B_star[2]*k3 + B_star[3]*k4 + B_star[4]*k5)
    y5 = p + current_dt * (B[0]*k1 + B[2]*k3 + B[3]*k4 + B[4]*k5 + B[5]*k6)

    error = (y4 - y5).length
    if error <= 1e-20: error = 1e-20

    safety_factor = 0.9
    optimal_dt = safety_factor * current_dt * (tolerance / error)**0.2

    if error <= tolerance:
        return (y5, optimal_dt, True)
    else:
        return (p, optimal_dt, False)


def step_dp5(rhs_func, p: Vector, params: dict, current_dt: float, tolerance: float):
    """Performs an adaptive Dormand-Prince 5(4) step."""
    A = [
        [], [1/5], [3/40, 9/40], [44/45, -56/15, 32/9],
        [19372/6561, -25360/2187, 64448/6561, -212/729],
        [9017/3168, -355/33, 46732/5247, 49/176, -5103/18656],
    ]
    B = [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0]
    B_star = [5179/57600, 0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40]

    k1 = rhs_func(p, params)
    k2 = rhs_func(p + current_dt * A[1][0]*k1, params)
    k3 = rhs_func(p + current_dt * (A[2][0]*k1 + A[2][1]*k2), params)
    k4 = rhs_func(p + current_dt * (A[3][0]*k1 + A[3][1]*k2 + A[3][2]*k3), params)
    k5 = rhs_func(p + current_dt * (A[4][0]*k1 + A[4][1]*k2 + A[4][2]*k3 + A[4][3]*k4), params)
    k6 = rhs_func(p + current_dt * (A[5][0]*k1 + A[5][1]*k2 + A[5][2]*k3 + A[5][3]*k4 + A[5][4]*k5), params)
    y5 = p + current_dt * (B[0]*k1 + B[1]*k2 + B[2]*k3 + B[3]*k4 + B[4]*k5 + B[5]*k6)
    k7 = rhs_func(y5, params)

    all_k = [k1, k2, k3, k4, k5, k6, k7]
    error_vec = current_dt * sum([(b - bs) * k for b, bs, k in zip(B, B_star, all_k)], Vector())

    error = error_vec.length
    if error <= 1e-20: error = 1e-20

    safety_factor = 0.9
    optimal_dt = safety_factor * current_dt * (tolerance / error)**0.2

    if error <= tolerance:
        return (y5, optimal_dt, True)
    else:
        return (p, optimal_dt, False)


# ==========================================================================
# 4. Safe Expression Parsing (AST Evaluation)
# ==========================================================================

_ALLOWED_VARS = {"x", "y", "z"}
_ALLOWED_FUNCS = {"sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh", "tanh", "exp", "log", "sqrt", "pow", "fabs"}
_MATH_FUNCS_MAP = {name: getattr(math, name) for name in _ALLOWED_FUNCS if hasattr(math, name)}
_ALLOWED_NODES = {ast.Expression, ast.BinOp, ast.UnaryOp, ast.Call, ast.Name, ast.Load, ast.Constant, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod, ast.USub, ast.UAdd}


class _UnsafeNodeError(Exception):
    """Custom exception for disallowed AST nodes during evaluation."""
    pass


def _eval_ast(node, env):
    """
    Safely evaluates a single AST node, whitelisting allowed operations.
    This prevents execution of arbitrary Python code from user input.
    """
    node_type = type(node)
    if node_type not in _ALLOWED_NODES:
        raise _UnsafeNodeError(f"Disallowed element: {node_type.__name__}")
    if isinstance(node, ast.Expression):
        return _eval_ast(node.body, env)
    if isinstance(node, ast.Constant):
        return float(node.value)
    if isinstance(node, ast.Name):
        if node.id in env:
            return env[node.id]
        raise _UnsafeNodeError(f"Unknown symbol '{node.id}'")
    if isinstance(node, ast.UnaryOp):
        op = {ast.UAdd: operator.pos, ast.USub: operator.neg}.get(type(node.op))
        return op(_eval_ast(node.operand, env))
    if isinstance(node, ast.BinOp):
        op = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod}.get(type(node.op))
        return op(_eval_ast(node.left, env), _eval_ast(node.right, env))
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _MATH_FUNCS_MAP:
        args = [_eval_ast(a, env) for a in node.args]
        return _MATH_FUNCS_MAP[node.func.id](*args)
    raise _UnsafeNodeError("Unsupported operation")


def _compile_rhs_expression(expr_src: str):
    """Parses and compiles a single user-provided math expression string."""
    parsed = ast.parse(expr_src, mode="eval")
    def _f(x, y, z, params):
        env = {"x": x, "y": y, "z": z, **params}
        return _eval_ast(parsed, env)
    return _f


def build_rhs_function(dx_src, dy_src, dz_src):
    """Builds a vector function from three expression strings (dx/dt, dy/dt, dz/dt)."""
    fx = _compile_rhs_expression(dx_src)
    fy = _compile_rhs_expression(dy_src)
    fz = _compile_rhs_expression(dz_src)
    def _rhs(p, params):
        x, y, z = p
        return Vector((fx(x, y, z, params), fy(x, y, z, params), fz(x, y, z, params)))
    return _rhs


def detect_parameter_names(dx, dy, dz) -> list[str]:
    """Scans expression strings to find all used parameter names."""
    names = set()
    for expr in (dx, dy, dz):
        try:
            names.update(n.id for n in ast.walk(ast.parse(expr, mode="eval")) if isinstance(n, ast.Name))
        except (SyntaxError, TypeError):
            continue
    # Exclude coordinate variables and math functions from the parameter list.
    return sorted(list(names - _ALLOWED_VARS - _ALLOWED_FUNCS))


# ==========================================================================
# 5. Attractor Library Management
# ==========================================================================

class AttractorLibraryManager:
    """Handles loading and saving of default (read-only) and custom (writable) attractors."""
    def __init__(self):
        self.default_systems = {}
        self.custom_library = {}
        self.custom_enum_cache = [("__NONE__", "<new>", "Create a new custom attractor")]

    def load_defaults(self):
            """Loads default attractors from the addon's bundled JSON file."""
            base_dir = _addon_dir()
            
            path = os.path.join(base_dir, "lib", "default_attractors.json")
            if not os.path.exists(path):
                path_upper = os.path.join(base_dir, "Lib", "default_attractors.json")
                if os.path.exists(path_upper):
                    path = path_upper

            if os.path.exists(path):
                try:
                    with open(path, "r", encoding="utf-8-sig") as f:
                        self.default_systems = json.load(f).get("items", {})
                except (IOError, json.JSONDecodeError) as e:
                    print(f"[Attractor] Error loading default library: {e}")
                    self.default_systems = {}
            else:
                print(f"[Attractor] Warning: Default library file not found at '{path}'")
                self.default_systems = {}

    def load_customs(self):
        """Loads custom attractors from the user's dedicated config directory."""
        self.custom_library = {}
        path = _get_user_data_path()

        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.custom_library = json.load(f).get("items", {})
            except (IOError, json.JSONDecodeError) as e:
                print(f"[Attractor] Custom library load failed at '{path}': {e}")
                self.custom_library = {}
        
        self._rebuild_custom_enum()

    def save_customs(self) -> bool:
        """Saves the custom library to the user's dedicated config directory."""
        path = _get_user_data_path()
        data = {"schema": 1, "items": self.custom_library}

        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"[Attractor] Customs saved to user library: {path}")
            return True
        except IOError as e:
            print(f"[Attractor] Error saving customs to '{path}': {e}")
            return False

    def _rebuild_custom_enum(self):
        """Rebuilds the cached list of items for the custom attractor EnumProperty."""
        items = [("__NONE__", "<new>", "Create a new custom attractor")]
        if self.custom_library:
            # Sort by creation timestamp to show newest first.
            sorted_items = sorted(
                self.custom_library.items(),
                key=lambda item: item[1].get('creation_timestamp', 0),
                reverse=True
            )
            items.extend([(name, name, "") for name, data in sorted_items])
        self.custom_enum_cache = items

    def get_default_enum_items(self):
        """Return enum items for defaults, ordering 'Lorenz' first, then alphabetical."""
        if not self.default_systems:
            return []
        names = list(self.default_systems.keys())
        # Sort so 'Lorenz' is first; others alphabetical (case-insensitive)
        names.sort(key=lambda s: (s.lower() != "lorenz", s.lower()))
        return [(n, n, "") for n in names]


    def get_first_default_name(self):
        """Pick a stable first default. Prefer 'Lorenz', else alphabetical first."""
        if self.default_systems:
            if "Lorenz" in self.default_systems:
                return "Lorenz"
            return sorted(self.default_systems.keys(), key=str.lower)[0]
        return None

    def get_custom_enum_items(self):
        """Returns cached items for the custom attractor EnumProperty."""
        return self.custom_enum_cache


# Singleton instance of the library manager.
lib_manager = AttractorLibraryManager()


# ==========================================================================
# 6. Blender Data & Curve Utilities
# ==========================================================================

def make_or_get_curve(context, name: str) -> tuple[bpy.types.Curve, bpy.types.Object]:
    """
    Honor Output Name strictly:
      - If an object with this exact name exists: reuse that object (overwrite its curve splines).
      - If no such object exists: create a NEW object with that exact name.
    Never reuse an existing curve *data* block by name (to avoid writing into other objects).
    """
    base = (name or "Attractor").strip()

    # 1) Exact object match → reuse object, ensure it's a curve, clear splines
    obj = bpy.data.objects.get(base)
    if obj is not None:
        # If it's not a curve, give it a curve datablock
        if obj.type != 'CURVE':
            cu = bpy.data.curves.new(f"{base}_Curve", type='CURVE')
            cu.dimensions = '3D'
            obj.data = cu
        else:
            cu = obj.data
            # overwrite behavior: start fresh
            if hasattr(cu, "splines"):
                cu.splines.clear()

        # make sure it's linked & visible in the active collection
        target_coll = getattr(context, "collection", None) or context.scene.collection
        if obj.name not in {o.name for o in target_coll.objects}:
            try:
                target_coll.objects.link(obj)
            except RuntimeError:
                pass  # already linked somewhere visible

        obj.hide_set(False)
        obj.hide_viewport = False
        obj.hide_render = False
        return cu, obj

    # 2) No object with that name → create a brand-new object with EXACT name
    cu = bpy.data.curves.new(f"{base}_Curve", type='CURVE')  # always new data to avoid collisions
    cu.dimensions = '3D'

    obj = bpy.data.objects.new(base, cu)  # object name == Output Name
    (getattr(context, "collection", None) or context.scene.collection).objects.link(obj)

    # visible + identity transform
    obj.hide_set(False)
    obj.hide_viewport = False
    obj.hide_render = False
    try:
        obj.matrix_world = Matrix.Identity(4)
    except Exception:
        pass

    return cu, obj


def write_polyline(curve: bpy.types.Curve, points: list[Vector]):
    """Clears a curve and writes a new polyline spline from a list of points."""
    curve.splines.clear()
    if not points:
        return
    spline = curve.splines.new('POLY')
    spline.points.add(len(points) - 1)
    for i, p in enumerate(points):
        spline.points[i].co = (p.x, p.y, p.z, 1.0)


def center_attractor_object(context: bpy.context, obj: bpy.types.Object):
    """(Deprecated/Unused) Utility to center an object's geometry around its origin."""
    if not obj or obj.type != 'CURVE' or not obj.data or not obj.data.splines:
        return

    M, Minv = obj.matrix_world, obj.matrix_world.inverted_safe()
    wcoords = [M @ pt.co.to_3d() for sp in obj.data.splines for pt in (getattr(sp, 'points', []) or getattr(sp, 'bezier_points', []))]
    if not wcoords:
        return

    wcenter = sum(wcoords, Vector()) / len(wcoords)
    lcenter = Minv @ wcenter

    for sp in obj.data.splines:
        if sp.type in {'POLY', 'NURBS'}:
            for pt in sp.points:
                pt.co.xyz -= lcenter
        elif sp.type == 'BEZIER':
            for bp in sp.bezier_points:
                bp.co -= lcenter
                bp.handle_left -= lcenter
                bp.handle_right -= lcenter

    obj.location = (0.0, 0.0, 0.0)
    try:
        obj.data.update_tag()
        obj.update_tag()
        context.view_layer.update()
    except RuntimeError:
        pass


def _resample_even(points, m):
    """Resamples a list of points to a new count, distributing them evenly by length."""
    n = len(points)
    if n < 2 or m <= 1 or m >= n:
        return points[:]

    segL = [(points[i+1] - points[i]).length for i in range(n-1)]
    total = sum(segL)
    if total <= 1e-12:
        return points[:]

    cum = [0.0] + [sum(segL[:i+1]) / total for i in range(len(segL))]

    out, j = [], 0
    for k in range(m):
        t = k / (m - 1) if m > 1 else 0.0
        while j < n - 2 and cum[j+1] < t:
            j += 1
        t0, t1 = cum[j], cum[j+1]
        f = 0.0 if t1 <= t0 else (t - t0) / (t1 - t0)
        out.append(points[j].lerp(points[j+1], f))
    return out


def _build_bezier_on_object(obj, pts, handle_type):
    """Converts a curve object to a Bezier spline defined by the given points."""
    cu = obj.data
    cu.splines.clear()
    sp = cu.splines.new('BEZIER')
    sp.bezier_points.add(len(pts) - 1)

    for i, p in enumerate(pts):
        bp = sp.bezier_points[i]
        bp.co = p
        bp.handle_left_type = 'AUTO'
        bp.handle_right_type = 'AUTO'
        if handle_type == 'AUTO_CLAMP' and hasattr(bp, 'handle_left_use_clamp'):
            bp.handle_left_use_clamp = True
            bp.handle_right_use_clamp = True

    sp.use_cyclic_u = False
    try:
        cu.update_tag()
        obj.update_tag()
    except RuntimeError:
        pass


def _sample_bezier_uniform(obj, target_count, dense_cap=12000):
    """Samples points from a Bezier curve to convert it back to a polyline."""
    cu = obj.data
    if not cu.splines or cu.splines[0].type != 'BEZIER':
        return None
    sp, bps = cu.splines[0], cu.splines[0].bezier_points
    if len(bps) < 2 or target_count < 2:
        return None

    segs = len(bps) - (1 - sp.use_cyclic_u)
    if segs <= 0:
        return None
    steps_per_seg = max(4, dense_cap // segs)

    def cubic(p0, h0, h1, p1, t):
        a = p0.lerp(h0, t)
        b = h0.lerp(h1, t)
        c = h1.lerp(p1, t)
        d = a.lerp(b, t)
        e = b.lerp(c, t)
        return d.lerp(e, t)

    dense_pts = []
    for i in range(segs):
        p0 = bps[i].co
        h0 = bps[i].handle_right
        p1 = bps[(i+1) % len(bps)].co
        h1 = bps[(i+1) % len(bps)].handle_left
        for s in range(steps_per_seg + 1):
            t = s / steps_per_seg
            if s > 0 or i == 0:
                dense_pts.append(cubic(p0, h0, h1, p1, t))

    return _resample_even(dense_pts, target_count) if dense_pts else None


def _visible_curve_as_points(obj, fallback_count=None):
    """Extracts a list of 3D vectors from a curve object, handling different spline types."""
    if not obj or not obj.data or not obj.data.splines:
        return None
    sp = obj.data.splines[0]

    if sp.type == 'POLY':
        return [p.co.to_3d() for p in sp.points]
    if sp.type == 'BEZIER':
        count = fallback_count or len(sp.bezier_points)
        return _sample_bezier_uniform(obj, max(2, int(count)))
    return [p.co.to_3d() for p in getattr(sp, "points", [])]


def ramer_douglas_peucker(points, epsilon):
    """Simplifies a 2D/3D polyline using the Ramer-Douglas-Peucker algorithm."""
    if not points or len(points) < 3:
        return points

    dmax, index, end = 0.0, 0, len(points) - 1
    p1, p2 = points[0], points[end]
    line_vec = p2 - p1
    line_len_sq = line_vec.length_squared

    for i in range(1, end):
        p = points[i]
        if line_len_sq == 0:
            d = (p - p1).length
        else:
            t = line_vec.dot(p - p1) / line_len_sq
            projection = p1 + max(0, min(1, t)) * line_vec
            d = (p - projection).length

        if d > dmax:
            index, dmax = i, d

    if dmax > epsilon:
        rec1 = ramer_douglas_peucker(points[:index + 1], epsilon)
        rec2 = ramer_douglas_peucker(points[index:], epsilon)
        return rec1[:-1] + rec2
    else:
        return [p1, p2]


# ==========================================================================
# 7. Property Update Callbacks
# ==========================================================================

def reset_post_processing_state_update(self, context):
    """Callback to hide post-processing when a main parameter changes."""
    props = context.scene.attractor_props
    if props.show_post_processing:
        props.show_post_processing = False
        props.active_curve_name = ""


def integration_method_update(self, context):
    """
    Synchronize high-level integration_method with internal
    integration_approach + method/adaptive_method.
    """
    method = self.integration_method

    # Fixed-step methods
    if method in {'EULER', 'HEUN', 'RK4'}:
        self.integration_approach = 'FIXED'
        self.method = method
    # Adaptive-step methods
    elif method in {'RKF45', 'DP5'}:
        self.integration_approach = 'ADAPTIVE'
        self.adaptive_method = method

    # Zachowaj dotychczasowe zachowanie: zmiana metody resetuje post-processing
    reset_post_processing_state_update(self, context)


def on_custom_equation_change(self, context):
    """Callback when custom equations change to require re-validation."""
    self.custom_validate_state = "NONE"
    reset_post_processing_state_update(self, context)


def update_attractor_defaults(self, context):
    """Callback to load settings when a new default attractor is selected."""
    reset_post_processing_state_update(self, context)
    self.show_simulation_tips = False
    entry = lib_manager.default_systems.get(self.attractor_type)
    if entry:
        apply_snapshot_to_props(self, entry)


def _on_mode_change(self, context):
    """Callback when switching between Default and Custom modes."""
    reset_post_processing_state_update(self, context)
    self.show_simulation_tips = False
    self.show_custom_details = False
    if self.mode == "CUSTOM":
        if self.custom_selected not in lib_manager.custom_library:
            self.custom_selected = "__NONE__"
    elif self.mode == "DEFAULT":
        first_default = lib_manager.get_first_default_name()
        if first_default:
            self.attractor_type = first_default


def _on_custom_select(self, context):
    """Callback when selecting an item from the custom library dropdown."""
    reset_post_processing_state_update(self, context)
    self.show_custom_details = False
    name = self.custom_selected
    if name == "__NONE__":
        # Reset to a simple default state for creating a new one.
        self.custom_name, self.custom_dx, self.custom_dy, self.custom_dz = "My Attractor", "y", "-x", "0"
        self.custom_params.clear()
        self.custom_validate_state = "NONE"
        self.x0, self.y0, self.z0, self.dt, self.steps, self.burn_in, self.scale = 1.0, 0.0, 0.0, 0.01, 700, 0, 1.0
    elif name in lib_manager.custom_library:
        apply_snapshot_to_props(self, lib_manager.custom_library[name])
        validate_and_update_params(self)


def apply_snapshot_to_props(props, entry):
    """Applies a saved attractor configuration (dict) to the scene properties."""
    props.custom_name = entry.get("name", "")
    rhs = entry.get("rhs", {})
    props.custom_dx, props.custom_dy, props.custom_dz = rhs.get("dx", ""), rhs.get("dy", ""), rhs.get("dz", "")
    props.custom_params.clear()
    for k, v in (entry.get("params") or {}).items():
        item = props.custom_params.add()
        item.name, item.value = k, float(v)
    initial = entry.get("initial", [0.01, 0.01, 0.01])
    props.x0, props.y0, props.z0 = [float(c) for c in initial]

    defaults = entry.get("defaults", {})
    procedure = defaults.get("procedure", "RK4")
    if procedure in {"EULER", "HEUN", "RK4", "RKF45", "DP5"}:
        props.integration_method = procedure
    else:
        props.integration_method = "RK4" 

    props.tolerance = float(defaults.get("tolerance", props.tolerance))
    props.min_dt = float(defaults.get("min_dt", props.min_dt))
    props.max_dt = float(defaults.get("max_dt", props.max_dt))
    props.dt = float(defaults.get("dt", props.dt))
    props.steps = int(defaults.get("steps", props.steps))
    props.burn_in = int(defaults.get("burn_in", props.burn_in))
    props.scale = float(defaults.get("scale", props.scale))


def validate_and_update_params(props):
    """Validates custom equations and updates the parameter list."""
    detected = detect_parameter_names(props.custom_dx, props.custom_dy, props.custom_dz)
    existing = {p.name: p.value for p in props.custom_params}
    props.custom_params.clear()
    for name in detected:
        item = props.custom_params.add()
        item.name, item.value = name, existing.get(name, 1.0)
    try:
        build_rhs_function(props.custom_dx, props.custom_dy, props.custom_dz)
        props.custom_validate_state, props.custom_validate_msg = "OK", "Validated! Enter parameter values:"
    except Exception as e:
        props.custom_validate_state, props.custom_validate_msg = "ERROR", str(e)
    return props.custom_validate_state == "OK"


def update_interactive_trim(self, context):
    """Callback for interactively trimming the curve in the viewport."""
    obj = self.active_curve or context.scene.objects.get(self.active_curve_name, None)
    if not obj or obj.type != 'CURVE':
        return

    src = _working_curve_cache.get(obj.name) or _original_curve_cache.get(obj.name)
    if not src:
        src = _visible_curve_as_points(obj)
        if not src:
            return
        _original_curve_cache[obj.name] = src

    N = len(src)
    if N < 2:
        return

    start_f = max(0.0, min(1.0, float(self.trim_start) / 100.0))
    end_f   = max(start_f, min(1.0, float(self.trim_end) / 100.0))
    start_i = int(start_f * (N - 1))
    end_i   = int(end_f * (N - 1))

    if start_i >= end_i:
        end_i = min(N - 1, start_i + 1) if start_i < N - 1 else start_i

    write_polyline(obj.data, src[start_i : end_i + 1])
    try:
        obj.data.update_tag()
        obj.update_tag()
        context.view_layer.update()
    except RuntimeError:
        pass


# ==========================================================================
# 8. Blender Property Groups
# ==========================================================================

class ATTRACTOR_CustomParam(bpy.types.PropertyGroup):
    """A single key-value pair for a custom attractor parameter."""
    name: bpy.props.StringProperty()
    value: bpy.props.FloatProperty(default=1.0, precision=6, update=reset_post_processing_state_update)


class ATTRACTOR_Props(bpy.types.PropertyGroup):
    """The main collection of properties for the addon."""
    mode: bpy.props.EnumProperty(items=[("DEFAULT", "Default", ""), ("CUSTOM", "Custom", "")], default="DEFAULT", update=_on_mode_change)
    attractor_type: bpy.props.EnumProperty(items=lambda s, c: lib_manager.get_default_enum_items(), update=update_attractor_defaults)
    custom_selected: bpy.props.EnumProperty(items=lambda s, c: lib_manager.get_custom_enum_items(), update=_on_custom_select)
    custom_name: bpy.props.StringProperty(name="Name", default="My Attractor")
    custom_dx: bpy.props.StringProperty(name="ẋ", default="y", update=on_custom_equation_change)
    custom_dy: bpy.props.StringProperty(name="ẏ", default="-x", update=on_custom_equation_change)
    custom_dz: bpy.props.StringProperty(name="ż", default="0", update=on_custom_equation_change)
    custom_params: bpy.props.CollectionProperty(type=ATTRACTOR_CustomParam)
    custom_validate_state: bpy.props.EnumProperty(items=[("NONE", "None", ""), ("OK", "OK", ""), ("ERROR", "Error", "")])
    custom_validate_msg: bpy.props.StringProperty()
    show_simulation_tips: bpy.props.BoolProperty(name="Show Tips", default=False)
    show_custom_details: bpy.props.BoolProperty(name="Show Details", default=False)
    show_post_processing: bpy.props.BoolProperty(name="Show Post-Processing", default=False)
    active_curve_name: bpy.props.StringProperty()
    active_curve: bpy.props.PointerProperty(name="Active Curve Object", type=bpy.types.Object)
    simplify_suspend: bpy.props.BoolProperty(default=False, options={'HIDDEN'})
    x0: bpy.props.FloatProperty(name="x0", default=0.01, precision=4, update=reset_post_processing_state_update)
    y0: bpy.props.FloatProperty(name="y0", default=0.01, precision=4, update=reset_post_processing_state_update)
    z0: bpy.props.FloatProperty(name="z0", default=0.01, precision=4, update=reset_post_processing_state_update)
    integration_method: bpy.props.EnumProperty(
        name="Method",
        items=[
            ("EULER", "Euler", "Explicit Euler, fixed step"),
            ("HEUN",  "Heun (RK2)", "Heun / RK2, fixed step"),
            ("RK4",   "RK4", "Runge–Kutta 4, fixed step"),
            ("RKF45", "RKF45", "Runge–Kutta–Fehlberg 4(5), adaptive step"),
            ("DP5",   "DP5", "Dormand–Prince 5(4), adaptive step"),
        ],
        default="RK4",
        update=integration_method_update,
    )    
    integration_approach: bpy.props.EnumProperty(name="Approach", items=[("FIXED", "Fixed", ""), ("ADAPTIVE", "Adaptive", "")], default="FIXED", update=reset_post_processing_state_update)
    method: bpy.props.EnumProperty(name="Procedure", items=[("EULER", "Euler", ""), ("HEUN", "Heun (RK2)", ""), ("RK4", "RK4", "")], default="RK4", update=reset_post_processing_state_update)
    adaptive_method: bpy.props.EnumProperty(name="Procedure", items=[("RKF45", "RKF45", ""), ("DP5", "DP5", "")], default="DP5", update=reset_post_processing_state_update)
    dt: bpy.props.FloatProperty(name="Time Step (dt)", default=0.01, min=1e-8, precision=5, update=reset_post_processing_state_update)
    tolerance: bpy.props.FloatProperty(name="Tolerance", default=1e-4, min=1e-10, precision=6, subtype='FACTOR', update=reset_post_processing_state_update)
    min_dt: bpy.props.FloatProperty(name="Min Step", default=1e-6, min=1e-12, precision=7, update=reset_post_processing_state_update)
    max_dt: bpy.props.FloatProperty(name="Max Step", default=0.1, min=1e-4, precision=4, update=reset_post_processing_state_update)
    steps: bpy.props.IntProperty(name="Steps", default=20000, min=2, soft_max=500000, update=reset_post_processing_state_update)
    burn_in: bpy.props.IntProperty(name="Burn-in", default=500, min=0, update=reset_post_processing_state_update)
    scale: bpy.props.FloatProperty(name="Scale", default=1.0, min=0.001, update=reset_post_processing_state_update)
    curve_name: bpy.props.StringProperty(name="Output Name", default="Attractor", update=reset_post_processing_state_update)
    trim_start: bpy.props.FloatProperty(name="Start", default=0.0, min=0.0, max=100.0, subtype='PERCENTAGE', update=update_interactive_trim)
    trim_end: bpy.props.FloatProperty(name="End", default=100.0, min=0.0, max=100.0, subtype='PERCENTAGE', update=update_interactive_trim)
    smooth_fidelity: bpy.props.FloatProperty(name="Fidelity", description="Higher values preserve more detail", default=0.8, min=0.0, max=1.0, subtype='FACTOR')

    def update_simplify_live(self, context):
        """Callback for interactively simplifying the curve by point count."""
        if self.simplify_suspend:
            return
        obj = self.active_curve or context.scene.objects.get(self.active_curve_name, None)
        if not obj or obj.type != 'CURVE':
            return
        name = obj.name

        src = _simplify_source_cache.get(name)
        if not src:
            src = _visible_curve_as_points(obj)
            if not src:
                return
            _simplify_source_cache[name] = src

        baseline_count = len(src)
        if baseline_count < 2:
            return

        target_count = max(2, min(int(self.simplify_target), baseline_count))
        new_pts = src[:] if target_count == baseline_count else _resample_even(src, target_count)

        write_polyline(obj.data, new_pts)
        _working_curve_cache[name] = new_pts
        update_interactive_trim(self, context)

    simplify_target: bpy.props.IntProperty(name="Simplify", default=1000, min=2, soft_max=50000, update=update_simplify_live)

    def update_simplify_percent(self, context):
        """Callback for interactively simplifying the curve by percentage."""
        if self.simplify_suspend:
            return
        obj = self.active_curve or context.scene.objects.get(self.active_curve_name, None)
        if not obj or obj.type != 'CURVE':
            return
        name = obj.name

        if name not in _simplify_source_cache:
            src = _visible_curve_as_points(obj)
            if not src:
                return
            _simplify_source_cache[name] = src

        baseline = len(_simplify_source_cache[name])
        keep_ratio = float(self.simplify_percent) / 100.0
        target = max(2, int(round(baseline * keep_ratio)))

        if int(self.simplify_target) != target:
            self.simplify_target = target

    simplify_percent: bpy.props.FloatProperty(
        name="Fidelity (%)",
        default=100.0, min=0.0, max=100.0,
        subtype='PERCENTAGE', update=update_simplify_percent)


# ==========================================================================
# 9. Blender Operators
# ==========================================================================

class ATTRACTOR_OT_build(bpy.types.Operator):
    """Generates the attractor curve based on the current simulation settings."""
    bl_idname = "attractor.build_curve"
    bl_label = "Build Attractor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        P = context.scene.attractor_props

        target_name = (getattr(P, "output_name", "") or "").strip() or "Attractor"
        cu, obj = make_or_get_curve(context, target_name)
        P.active_curve_name = obj.name
        
        P.show_post_processing = False
        P.active_curve_name = ""

        try:
            if P.mode == "DEFAULT":
                entry = lib_manager.default_systems.get(P.attractor_type)
                rhs = entry.get("rhs", {})

                if len(P.custom_params) == 0:
                    P.custom_params.clear()
                    for k, v in (entry.get("params") or {}).items():
                        item = P.custom_params.add()
                        try:
                            item.name, item.value = k, float(v)
                        except Exception:
                            # Fallback in case JSON holds non-floats (e.g., strings like "0.95")
                            item.name, item.value = k, float(str(v))

                params = {p.name: p.value for p in P.custom_params}

                rhs_func = build_rhs_function(rhs.get('dx'), rhs.get('dy'), rhs.get('dz'))

            else: # CUSTOM
                if P.custom_validate_state != "OK":
                    raise ValueError("Custom equations are not validated.")
                params = {p.name: p.value for p in P.custom_params}
                rhs_func = build_rhs_function(P.custom_dx, P.custom_dy, P.custom_dz)

            p, points, wm = Vector((P.x0, P.y0, P.z0)), [], context.window_manager
            global _raw_points, _raw_dts
            _raw_points = [p.copy()]
            _raw_dts = [0.0]

            if P.integration_approach == 'ADAPTIVE':
                dt, pts_gen, burn_done = P.dt, 0, 0
                wm.progress_begin(0, P.steps)
                stepper = step_dp5 if P.adaptive_method == 'DP5' else step_rkf45
                while pts_gen < P.steps:
                    dt = max(P.min_dt, min(P.max_dt, dt))
                    p_next, next_dt, accepted = stepper(rhs_func, p, params, dt, P.tolerance)
                    if accepted:
                        p = p_next
                        if any(math.isnan(c) or math.isinf(c) for c in p):
                            raise ValueError("Numerical instability detected.")
                        if burn_done >= P.burn_in:
                            _raw_points.append(p.copy())
                            _raw_dts.append(dt)
                            points.append(p * P.scale)
                            pts_gen += 1
                        else:
                            burn_done += 1
                    dt = next_dt
                    if (pts_gen % 200) == 0:
                        wm.progress_update(pts_gen)
                wm.progress_end()
            else: # FIXED
                stepper = {"RK4": step_rk4, "HEUN": step_heun}.get(P.method, step_euler)
                stepper_fn = functools.partial(stepper, rhs_func)
                wm.progress_begin(0, P.steps)
                for i in range(P.steps + P.burn_in):
                    p = stepper_fn(p, params, P.dt)
                    if any(math.isnan(c) or math.isinf(c) for c in p):
                        raise ValueError(f"Numerical instability @ step {i}.")
                    if i >= P.burn_in:
                        _raw_points.append(p.copy())
                        _raw_dts.append(P.dt)
                        points.append(p * P.scale)
                    if (i % 200) == 0:
                        wm.progress_update(i - P.burn_in)
                wm.progress_end()

            if not points:
                self.report({'WARNING'}, "No points were generated.")
                return {'CANCELLED'}

            # Center the generated points before creating the curve
            centroid = sum(points, Vector()) / len(points)
            points = [pt - centroid for pt in points]

            cu, obj = make_or_get_curve(context, P.curve_name)
            write_polyline(cu, points)
            obj.matrix_world = Matrix.Identity(4)

            # Clear all caches for this object and re-initialize with the new data.
            for cache in [_original_curve_cache, _simplify_source_cache, _working_curve_cache, _smooth_source_cache]:
                cache.pop(obj.name, None)
            _original_curve_cache[obj.name] = [p.copy() for p in points]

            P.trim_start, P.trim_end = 0.0, 100.0
            P.simplify_percent = 100.0
            P.simplify_target = len(points)
            P.active_curve = obj
            P.active_curve_name = obj.name
            P.show_post_processing = True
            self.report({'INFO'}, f"Generated {len(points)} points for '{obj.name}'")

        except Exception as e:
            self.report({'ERROR'}, f"Failed to build attractor: {e}")
            return {'CANCELLED'}
        return {'FINISHED'}


class ATTRACTOR_OT_custom_validate(bpy.types.Operator):
    """Validates custom equations and detects parameter names."""
    bl_idname = "attractor.custom_validate"
    bl_label = "Detect Parameters"

    def execute(self, context):
        if validate_and_update_params(context.scene.attractor_props):
            self.report({'INFO'}, "Validation successful.")
        else:
            msg = context.scene.attractor_props.custom_validate_msg
            self.report({'ERROR'}, f"Validation failed: {msg}")
        return {'FINISHED'}


class ATTRACTOR_OT_custom_manage_library(bpy.types.Operator):
    """Adds or deletes the current configuration from the custom library."""
    bl_idname = "attractor.custom_manage_library"
    bl_label = "Manage Library"
    action: bpy.props.EnumProperty(items=[('ADD', 'Add', ''), ('DELETE', 'Delete', '')])

    def execute(self, context):
        P = context.scene.attractor_props
        if self.action == 'ADD':
            if not P.custom_name.strip():
                self.report({'ERROR'}, "Name cannot be empty.")
                return {'CANCELLED'}
            if P.custom_validate_state != "OK":
                self.report({'ERROR'}, "Please validate the equations first.")
                return {'CANCELLED'}

            procedure = P.adaptive_method if P.integration_approach == 'ADAPTIVE' else P.method
            entry = {
                "name": P.custom_name,
                "rhs": {"dx": P.custom_dx, "dy": P.custom_dy, "dz": P.custom_dz},
                "params": {p.name: p.value for p in P.custom_params},
                "initial": [P.x0, P.y0, P.z0],
                "defaults": {
                    "procedure": procedure, "dt": P.dt, "tolerance": P.tolerance,
                    "min_dt": P.min_dt, "max_dt": P.max_dt, "steps": P.steps,
                    "burn_in": P.burn_in, "scale": P.scale
                },
                "creation_timestamp": time.time(),
                "details": ""
            }
            lib_manager.custom_library[P.custom_name] = entry
            lib_manager._rebuild_custom_enum()
            if lib_manager.save_customs():
                self.report({'INFO'}, f"Saved '{P.custom_name}' to user library.")
            else:
                self.report({'WARNING'}, "Saved to memory, but failed to write to disk.")
            P.custom_selected = P.custom_name

        elif self.action == 'DELETE' and P.custom_selected in lib_manager.custom_library:
            name = P.custom_selected
            del lib_manager.custom_library[name]
            lib_manager._rebuild_custom_enum()
            lib_manager.save_customs()
            P.custom_selected = "__NONE__"
            self.report({'INFO'}, f"Deleted '{name}' from user library.")

        return {'FINISHED'}


class ATTRACTOR_OT_copy_to_custom(bpy.types.Operator):
    """Copies the current default attractor and its parameters to a new custom entry."""
    bl_idname = "attractor.copy_to_custom"
    bl_label = "Copy"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        P = context.scene.attractor_props
        if not P.attractor_type or P.attractor_type == "__NONE__":
            return {'CANCELLED'}

        base_name = P.attractor_type
        i = 1
        new_name = f"{base_name} Copy"
        while new_name in lib_manager.custom_library:
            i += 1
            new_name = f"{base_name} Copy {i}"

        default_entry = lib_manager.default_systems.get(P.attractor_type, {})
        procedure = P.adaptive_method if P.integration_approach == 'ADAPTIVE' else P.method
        entry = {
            "name": new_name,
            "rhs": default_entry.get("rhs", {}),
            "params": {p.name: p.value for p in P.custom_params},
            "initial": [P.x0, P.y0, P.z0],
            "defaults": {
                "procedure": procedure, "dt": P.dt, "tolerance": P.tolerance,
                "min_dt": P.min_dt, "max_dt": P.max_dt, "steps": P.steps,
                "burn_in": P.burn_in, "scale": P.scale
            },
            "creation_timestamp": time.time(),
            "details": default_entry.get("details", "")
        }
        lib_manager.custom_library[new_name] = entry
        lib_manager._rebuild_custom_enum()
        if lib_manager.save_customs():
            self.report({'INFO'}, f"Copied to custom library as '{new_name}'.")
        else:
            self.report({'WARNING'}, "Saved to memory, but failed to write to disk.")

        P.mode = 'CUSTOM'
        P.custom_selected = new_name
        return {'FINISHED'}


class ATTRACTOR_OT_edit_notes(bpy.types.Operator):
    """Opens a dialog to edit the notes for a custom attractor."""
    bl_idname = "attractor.edit_notes"
    bl_label = "Edit Attractor Notes"
    bl_options = {'REGISTER', 'UNDO'}

    attractor_name: bpy.props.StringProperty()
    details_text: bpy.props.StringProperty(name="Notes / Details")

    def invoke(self, context, event):
        if self.attractor_name in lib_manager.custom_library:
            self.details_text = lib_manager.custom_library[self.attractor_name].get("details", "")
        return context.window_manager.invoke_props_dialog(self, width=300)

    def draw(self, context):
        self.layout.prop(self, "details_text", text="")

    def execute(self, context):
        if self.attractor_name in lib_manager.custom_library:
            lib_manager.custom_library[self.attractor_name]["details"] = self.details_text
            lib_manager.save_customs()
        return {'FINISHED'}


class ATTRACTOR_OT_trim_apply(bpy.types.Operator):
    """Applies the current trim, making it the new 0-100% range."""
    bl_idname = "attractor.trim_apply"
    bl_label = "Apply Trim"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        P = context.scene.attractor_props
        obj = P.active_curve or context.scene.objects.get(P.active_curve_name)
        if not obj or obj.type != 'CURVE':
            return {'CANCELLED'}

        pts = _visible_curve_as_points(obj)
        if not pts or len(pts) < 2:
            return {'CANCELLED'}

        # The current state becomes the new source of truth.
        _original_curve_cache[obj.name] = pts
        _simplify_source_cache.pop(obj.name, None)
        _working_curve_cache.pop(obj.name, None)

        P.simplify_target, P.simplify_percent = len(pts), 100.0
        P.trim_start, P.trim_end = 0.0, 100.0
        update_interactive_trim(P, context)
        self.report({'INFO'}, f"Trim applied. '{obj.name}' is now the new base.")
        return {'FINISHED'}


class ATTRACTOR_OT_simplify_apply(bpy.types.Operator):
    """Applies the current simplification, making it the new base curve."""
    bl_idname = "attractor.simplify_apply"
    bl_label = "Apply Simplify"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        P = context.scene.attractor_props
        obj = P.active_curve or context.scene.objects.get(P.active_curve_name)
        if not obj or obj.type != 'CURVE':
            return {'CANCELLED'}

        pts = _working_curve_cache.get(obj.name) or _visible_curve_as_points(obj)
        if not pts or len(pts) < 2:
            return {'CANCELLED'}

        _original_curve_cache[obj.name] = pts
        _working_curve_cache.pop(obj.name, None)
        _simplify_source_cache.pop(obj.name, None)

        update_interactive_trim(P, context)
        self.report({'INFO'}, f"Simplify applied to '{obj.name}'.")
        return {'FINISHED'}


class ATTRACTOR_OT_smooth_apply(bpy.types.Operator):
    """Converts the polyline to a smooth Bezier curve."""
    bl_idname = "attractor.smooth_apply"
    bl_label = "Apply Smooth"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        P = context.scene.attractor_props
        obj = P.active_curve or context.scene.objects.get(P.active_curve_name)
        if not obj or obj.type != 'CURVE':
            self.report({'ERROR'}, "No valid curve object selected.")
            return {'CANCELLED'}

        src_points = _visible_curve_as_points(obj)
        if not src_points or len(src_points) < 2:
            self.report({'WARNING'}, "Not enough points to smooth.")
            return {'CANCELLED'}

        if len(src_points) > 150000:
            src_points = _resample_even(src_points, 150000)

        min_pt = Vector(map(min, zip(*[p.xyz for p in src_points])))
        max_pt = Vector(map(max, zip(*[p.xyz for p in src_points])))
        diagonal_length = (max_pt - min_pt).length if src_points else 0

        fidelity_factor = (1.0 - P.smooth_fidelity)**2
        epsilon = diagonal_length * (0.0001 + fidelity_factor * 0.05)

        control_points = ramer_douglas_peucker(src_points, epsilon)

        MAX_CONTROL_POINTS = 20000
        if len(control_points) > MAX_CONTROL_POINTS:
            control_points = _resample_even(control_points, MAX_CONTROL_POINTS)
            self.report({'WARNING'}, f"Point count capped at {MAX_CONTROL_POINTS} for stability.")

        if len(control_points) < 2:
            self.report({'WARNING'}, "Smoothing resulted in too few points.")
            return {'CANCELLED'}

        _build_bezier_on_object(obj, control_points, 'AUTO_CLAMP')

        new_base_pts = _sample_bezier_uniform(obj, len(control_points) * 4) or control_points
        _original_curve_cache[obj.name] = new_base_pts

        for cache in [_working_curve_cache, _simplify_source_cache]:
            cache.pop(obj.name, None)

        P.simplify_suspend = True
        P.simplify_target, P.simplify_percent = len(new_base_pts), 100.0
        P.simplify_suspend = False

        self.report({'INFO'}, f"Smoothed to {len(control_points)} control points.")
        return {'FINISHED'}

class ATTRACTOR_OT_export_raw(bpy.types.Operator):
    bl_idname = "attractor.export_raw_points"
    bl_label = "Export Raw ODE Points"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = ("Create a 'RawPoints' mesh object in the scene (unscaled)")

    def execute(self, context):
        if not _raw_points:
            self.report({'ERROR'}, "No raw ODE points available. Build the attractor first.")
            return {'CANCELLED'}

        mesh = bpy.data.meshes.new("RawPointsMesh")
        mesh.from_pydata([tuple(p) for p in _raw_points], [], [])
        obj = bpy.data.objects.new("RawPoints", mesh)
        context.scene.collection.objects.link(obj)

        self.report({'INFO'}, f"Exported {len(_raw_points)} raw points.")
        return {'FINISHED'}

class ATTRACTOR_OT_export_raw_csv(bpy.types.Operator):
    bl_idname = "attractor.export_raw_csv"
    bl_label = "Export Raw ODE Points CSV"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = ("Save the raw ODE trajectory to CSV (step, dt, x, y, z).")    
    
    filepath: bpy.props.StringProperty(
        name="File Path",
        description="File path for exporting raw ODE points as CSV",
        subtype='FILE_PATH',
        default="",
    )

    def invoke(self, context, event):
        if not _raw_points:
            self.report({'ERROR'}, "No raw ODE points available. Build the attractor first.")
            return {'CANCELLED'}

        if not self.filepath:
            # domyślna nazwa w katalogu blend-a
            self.filepath = bpy.path.abspath("//attractor_raw_points.csv")

        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        if not _raw_points:
            self.report({'ERROR'}, "No raw ODE points available. Build the attractor first.")
            return {'CANCELLED'}

        if not self.filepath:
            self.report({'ERROR'}, "No filepath specified for CSV export.")
            return {'CANCELLED'}

        abs_path = bpy.path.abspath(self.filepath)

        try:
            with open(abs_path, "w", encoding="utf-8", newline="") as f:
                f.write("steps,dt,x,y,z\n")
                for i, p in enumerate(_raw_points):
                    dt = _raw_dts[i] if i < len(_raw_dts) else 0.0
                    f.write(f"{i},{dt:.10g},{p.x:.10g},{p.y:.10g},{p.z:.10g}\n")
        except OSError as e:
            self.report({'ERROR'}, f"Failed to write CSV: {e}")
            return {'CANCELLED'}

        self.report({'INFO'}, f"Exported {len(_raw_points)} raw points to CSV.")
        return {'FINISHED'}


# ==========================================================================
# 10. Blender UI Panels
# ==========================================================================

def _defer_apply_defaults(scene_name: str, attractor_type: str):
    """Apply JSON defaults safely after UI draw (no writes in draw())."""
    def _do():
        # Resolve scene (works in unsaved files, too)
        scene = bpy.data.scenes.get(scene_name) or getattr(bpy.context, "scene", None)
        if not scene:
            return None  # stop timer

        P = getattr(scene, "attractor_props", None)
        if not P:
            return None

        entry = lib_manager.default_systems.get(attractor_type) if lib_manager else None
        if not entry:
            return None

        # Idempotent: only apply if not already in desired state
        want = (entry.get("defaults") or {}).get("scale")
        if (len(P.custom_params) == 0) or (want is not None and abs(P.scale - float(want)) > 1e-9):
            apply_snapshot_to_props(P, entry)

        return None  # run once
    bpy.app.timers.register(_do, first_interval=0.0)


class ATTRACTOR_PT_panel(bpy.types.Panel):
    """The main UI panel for generating attractors."""
    bl_label = "Attractor Builder"
    bl_idname = "ATTRACTOR_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Attractor"

    def draw(self, context):
        layout = self.layout
        P = context.scene.attractor_props
        entry = None
        if P.mode == 'DEFAULT':
            entry = lib_manager.default_systems.get(P.attractor_type)
            if entry:
                fresh_like = (
                    len(P.custom_params) == 0
                    and abs(P.scale - 1.0) < 1e-9
                    and P.integration_approach == 'FIXED'
                    and P.method == 'RK4')
                if fresh_like:
                    _defer_apply_defaults(context.scene.name, P.attractor_type)
        layout.row().prop(P, "mode", expand=True)

        if P.mode == 'DEFAULT':
            box = layout.box()
            box.label(text="Default Library", icon='ASSET_MANAGER')
            box.prop(P, "attractor_type", text="")
            entry = lib_manager.default_systems.get(P.attractor_type)
            if entry:
                col = box.column(align=True)
                col.label(text="Equations:", icon='FUND')
                rhs = entry.get("rhs", {})
                col.scale_y = 0.8
                col.label(text=f"ẋ = {rhs.get('dx', '...')}")
                col.label(text=f"ẏ = {rhs.get('dy', '...')}")
                col.label(text=f"ż = {rhs.get('dz', '...')}")
                if P.custom_params:
                    col.separator()
                    col.scale_y = 1.0
                    col.label(text="Parameters:")
                    for param in P.custom_params:
                        col.prop(param, "value", text=param.name)

                action_row = box.row(align=True)
                action_row.prop(P, "show_simulation_tips", text="Tips", toggle=True, icon='HELP')
                action_row.operator("attractor.copy_to_custom", icon='COPYDOWN')
                if P.show_simulation_tips:
                    tips_box = box.box()
                    details_text = entry.get("details", "No details available.")
                    wrap_width = max(20, (context.region.width - 40) // 7)
                    text_col = tips_box.column(align=True)
                    for line in textwrap.wrap(details_text, width=wrap_width):
                        row = text_col.row()
                        row.scale_y = 0.8
                        row.label(text=line)

        else:  # CUSTOM
            box = layout.box()
            box.label(text="Custom Library", icon='USER')
            box.prop(P, "custom_selected", text="")

            col = box.column(align=True)
            col.label(text="Equations:", icon='FUND')

            # ẋ
            row = col.row(align=True)
            split = row.split(factor=0.1, align=True)
            split.label(text="ẋ =")
            split.prop(P, "custom_dx", text="")

            # ẏ
            row = col.row(align=True)
            split = row.split(factor=0.1, align=True)
            split.label(text="ẏ =")
            split.prop(P, "custom_dy", text="")

            # ż
            row = col.row(align=True)
            split = row.split(factor=0.1, align=True)
            split.label(text="ż =")
            split.prop(P, "custom_dz", text="")


            box.operator("attractor.custom_validate", text="Detect Parameters")

            sbox = box.box()
            if P.custom_validate_state == "OK":
                sbox.label(text=P.custom_validate_msg, icon='CHECKMARK')
                param_col = sbox.column(align=True)
                for it in P.custom_params:
                    param_col.prop(it, "value", text=it.name)

            elif P.custom_validate_state == "ERROR":
                sbox.label(text=f"Error: {P.custom_validate_msg}", icon='ERROR')
            else: # "NONE" state
                sbox.label(text="Not validated yet", icon='INFO')

            manage_box = box.box()
            manage_col = manage_box.column(align=True)
            row_name = manage_col.row(align=True)
            split_name = row_name.split(factor=0.3)
            split_name.label(text="Name:")
            split_name.prop(P, "custom_name", text="")
            row_actions = manage_col.row(align=True)
            row_actions.operator("attractor.custom_manage_library", text="Save", icon='ADD').action = 'ADD'
            delete_col = row_actions.column(align=True)
            delete_col.active = P.custom_selected != "__NONE__"
            delete_col.operator("attractor.custom_manage_library", text="Delete", icon='TRASH').action = 'DELETE'
            notes_row = manage_col.row(align=True)
            notes_row.active = P.custom_selected != "__NONE__"
            notes_row.prop(P, "show_custom_details", text="Notes", toggle=True, icon='BOOKMARKS')
            op = notes_row.operator("attractor.edit_notes", text="Edit", icon='TEXT')
            op.attractor_name = P.custom_selected

            if P.show_custom_details and P.custom_selected != "__NONE__":
                entry = lib_manager.custom_library.get(P.custom_selected)
                if entry:
                    details_box = box.box()
                    details_text = entry.get("details", "No notes available.")
                    wrap_width = max(20, (context.region.width - 40) // 7)
                    for line in textwrap.wrap(details_text, width=wrap_width):
                        row = details_box.row(align=True)
                        row.scale_y = 0.6
                        row.label(text=line)

        sim = layout.box()
        sim.label(text="Simulation Settings", icon='SETTINGS')
        col = sim.column(align=True)
        col.label(text="Initial conditions:")
        row_init = col.row(align=True)
        row_init.prop(P, "x0")
        row_init.prop(P, "y0")
        row_init.prop(P, "z0")

        row = col.row(align=True)
        split = row.split(factor=0.55)

        col_left = split.column()
        col_right = split.column()

        col_left.label(text="Integration Method:")
        col_right.prop(P, "integration_method", text="")

        if P.integration_method in {'EULER', 'HEUN', 'RK4'}:
            col.label(text="Fixed dt:")
            col.prop(P, "dt")
            col.prop(P, "steps")
            col.prop(P, "burn_in")
            col.prop(P, "scale")
        else:
            col.label(text="Adaptive dt:")
            col.prop(P, "tolerance")
            col.prop(P, "min_dt")
            col.prop(P, "max_dt")
            col.prop(P, "steps")
            col.prop(P, "burn_in")
            col.prop(P, "scale")



        build_box = layout.box()
        build_col = build_box.column(align=True)
        row_name = build_col.row(align=True)
        split_name = row_name.split(factor=0.4)
        split_name.label(text="Output Name:")
        split_name.prop(P, "curve_name", text="")

        build_col.operator("attractor.build_curve", text="Build Attractor", icon='EXPERIMENTAL')

        build_col.separator()
        build_col.label(text="Raw data:")

        raw_row = build_col.row(align=True)
        raw_row.operator("attractor.export_raw_points", text="Points", icon='POINTCLOUD_DATA')
        raw_row.operator("attractor.export_raw_csv", text="Export", icon='EXPORT')




class ATTRACTOR_PT_post_processing(bpy.types.Panel):
    """A sub-panel for interactive tools that appears after an attractor is built."""
    bl_label = "Post-Processing Tools"
    bl_idname = "ATTRACTOR_PT_post_processing_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Attractor"
    bl_parent_id = "ATTRACTOR_PT_main_panel"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        P = context.scene.attractor_props
        obj = P.active_curve or context.scene.objects.get(P.active_curve_name)
        return P.show_post_processing and obj

    def draw(self, context):
        layout = self.layout
        P = context.scene.attractor_props
        obj = bpy.data.objects.get(P.active_curve_name)
        if not obj or obj.type != 'CURVE':
            return
        cu = obj.data
        
        box = layout.box()

        col = box.column(align=True)
        col.label(text="Trim", icon='CURVE_DATA')
        row = col.row(align=True)
        row.prop(P, "trim_start", slider=True)
        row.prop(P, "trim_end", slider=True)
        col.operator("attractor.trim_apply")
        col.separator()

        col.label(text="Simplify", icon='MOD_DECIM')
        name = P.active_curve.name if P.active_curve else P.active_curve_name
        baseline = len(_simplify_source_cache.get(name, [])) if name else 0
        keep_ratio = float(P.simplify_percent) / 100.0
        est_pts = max(2, int(baseline * keep_ratio)) if baseline > 0 else int(P.simplify_target)
        col.prop(P, "simplify_percent",
                 text=f"Points: {est_pts:,}", slider=True)
        col.operator("attractor.simplify_apply")


        col.label(text="Smooth to Bezier", icon='IPO_SINE')
        col.prop(P, "smooth_fidelity", slider=True)
        col.operator("attractor.smooth_apply")


# ==========================================================================
# 11. Addon Registration
# ==========================================================================

classes = (
    ATTRACTOR_CustomParam, ATTRACTOR_Props,
    ATTRACTOR_OT_build, ATTRACTOR_OT_custom_validate, ATTRACTOR_OT_custom_manage_library,
    ATTRACTOR_OT_copy_to_custom, ATTRACTOR_OT_edit_notes, ATTRACTOR_OT_trim_apply,
    ATTRACTOR_OT_simplify_apply, ATTRACTOR_OT_smooth_apply,
    ATTRACTOR_PT_panel, ATTRACTOR_PT_post_processing,
    ATTRACTOR_OT_export_raw, ATTRACTOR_OT_export_raw_csv,
)


def register():
    # 1) Register classes
    for cls in classes:
        bpy.utils.register_class(cls)

    # 2) Scene pointer
    bpy.types.Scene.attractor_props = bpy.props.PointerProperty(type=ATTRACTOR_Props)

    # 3) Library manager + initial loads (safe for unsaved files)
    global lib_manager
    lib_manager = AttractorLibraryManager()
    lib_manager.load_defaults()
    lib_manager.load_customs()

    # 4) Initialize UI state if a Scene exists (Preferences enable may have no scene)
    scene = getattr(bpy.context, "scene", None)
    if scene and hasattr(scene, "attractor_props"):
        P = scene.attractor_props
        P.mode = "DEFAULT"

        # Prefer Lorenz if present; otherwise use your stable first default
        chosen = "Lorenz" if "Lorenz" in lib_manager.default_systems else lib_manager.get_first_default_name()
        if chosen:
            P.attractor_type = chosen
            # Seed parameters exactly as if the user selected it in the UI
            update_attractor_defaults(P, bpy.context)

    print("Attractor Builder addon registered.")


def unregister():
    """Unregisters all addon classes and removes properties."""
    try:
        del bpy.types.Scene.attractor_props
    except (AttributeError, RuntimeError):
        pass
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except (RuntimeError, TypeError):
            pass
    print("Attractor Builder addon unregistered.")


if __name__ == "__main__":
    register()