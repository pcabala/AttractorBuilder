
# Attractor Builder — Blender Add-on

Attractor Builder is a free Blender add-on for numerical integration and
3D visualization of nonlinear dynamical systems.  
It allows you to generate trajectories of differential equation systems,
export raw simulation data, build animated attractors, and experiment with
both classic and custom chaotic models — directly inside **Blender 4.5+**.

The add-on is designed for researchers, students, and artists interested in
chaotic dynamics, generative art, or mathematical visualization.

---

## 📥 Installation

1. Download the file **`attractor_builder.zip`** from the GitHub repository.  
2. In Blender, open:  
   **Edit → Preferences → Add-ons**  
3. Click **Install…** and select the downloaded ZIP file.  
4. Enable the add-on in the list.  
5. The add-on panel will appear in the **N-panel → Attractors**.

<p align="center">
  <img src="assets/media/addon/intro.png" width="750">
</p>

---

## 📂 Features Overview

### **✓ Default Mode — Built-in Systems**
The Default mode contains a curated set of well-known dynamical systems  
(Lorenz, Chen, Lü, Thomas, Arneodo–Coullet–Tresser, and others) with  
preconfigured equations and parameters.

<p align="center">
  <img src="assets/media/addon/mode_default.png" width="750">
</p>

Each system includes:
- differential equations (`dx/dt`, `dy/dt`, `dz/dt`)
- editable parameters (e.g., `a`, `b`, `c`)
- a **Copy** button to transfer the system into Custom Mode

---

### **✓ Custom Mode — User-defined Equations**
You can define your own dynamical system using safe mathematical expressions.

Allowed variables:


x, y, z


Allowed functions:


sin, cos, tan, asin, acos, atan,
sinh, cosh, tanh,
exp, log, sqrt, pow, fabs


Allowed operators:


+, -, *, /, **, %, unary +, unary -


After typing the equations, use **Detect Parameters** to analyze the system
and build a parameter list. You can then save your system to the **Custom Library**
(internal JSON storage), add notes, edit entries, or delete them.

<p align="center">
  <img src="assets/media/addon/mode_custom.png" width="750">
</p>

---

### **✓ Simulation Settings**

You can choose between:

#### **Fixed Step Methods**
- Euler  
- Heun (RK2)  
- Runge–Kutta 4 (RK4)

Settings include:
- **Time Step (dt)**
- **Steps**
- **Burn-in**
- **Scale**

<p align="center">
  <img src="assets/media/addon/fixed_dt.png" width="750">
</p>

#### **Adaptive Step Methods**
- Runge–Kutta–Fehlberg 4(5) (RKF45)  
- Dormand–Prince 5(4) (DP5)

These methods do **not** use a fixed `dt`.  
Instead, the step size is chosen automatically based on:

- **Tolerance**  
- **Min Step**
- **Max Step**

<p align="center">
  <img src="assets/media/addon/adaptive_dt.png" width="750">
</p>

---

### **✓ Generating and Exporting Trajectories**

Click **Build Attractor** to generate a trajectory as a  
**Poly Curve** object (default name: `Attractor`).  
After building the trajectory, the **Raw Data** section becomes available.

- **Points** — creates a mesh containing all generated points  
- **Export** — saves a CSV file with columns:



steps, dt, x, y, z


Row `0` contains the initial conditions.  
In adaptive methods, `dt` varies at every step.

<p align="center">
  <img src="assets/media/addon/output.png" width="750">
</p>

---

### **✓ Post-Processing Tools**

Available only after generating an attractor.

Tools include:
- **Trim** — cut the beginning or end of the curve  
- **Simplify** — reduce the number of Poly Curve points  
- **Smooth to Bezier** — convert to a Bézier curve using a smoothing algorithm  

<p align="center">
  <img src="assets/media/addon/post_processing.png" width="750">
</p>

These tools help prepare trajectories for animation or artistic rendering.

---

## 📘 Documentation

Full documentation (PL/EN) with detailed examples and mathematical explanations  
is available at:

👉 **https://pcabala.github.io/**

---

## 🧩 Requirements

- **Blender 4.5+**  
- No external Python installation required  
- Works on Windows, Linux, and macOS

---

## 📝 License

Specify your license here, e.g.:

**MIT License**

---

## 🙋‍♂️ Author

Paweł Cabała  
2024–2025