## Attractor Builder — Blender Add-on

Attractor Builder is a free Blender add-on for numerical integration and
3D visualization of nonlinear dynamical systems.  
It allows you to generate trajectories of differential equations,
export raw simulation data, build animated attractors, and experiment with
both classic and custom chaotic models — directly inside **Blender 4.5+**.

---

## Installation

1. Download **`attractor_builder.zip`** from this repository.  
2. In Blender, open:  
   **Edit → Preferences → Add-ons**  
3. Click **Install…** and select the ZIP file.  
4. Enable the add-on in the list.  
5. The add-on will appear in the **N-panel → Attractors**.

<img src="docs/assets/media/addon/intro.png" alt="Attractor Builder – panel location">

---

## Features

### Default Mode (built-in systems)

A curated set of classic dynamical systems, including Lorenz, Chen, Lü, Thomas,
Arneodo–Coullet–Tresser, and others.  
Each system includes:

- differential equations (`dx/dt`, `dy/dt`, `dz/dt`)
- editable parameters
- “Copy to Custom Mode”

<img src="docs/assets/media/addon/mode_default.png" alt="Default mode">

---

### Custom Mode (user-defined equations)

Define a custom dynamical system using safe mathematical expressions.

Allowed variables:

`x`, `y`, `z`

Allowed functions:

`sin`, `cos`, `tan`, `asin`, `acos`, `atan`,  
`sinh`, `cosh`, `tanh`, `exp`, `log`, `sqrt`, `pow`, `fabs`

Allowed operators:

`+`, `-`, `*`, `/`, `**`, `%`, unary `+`, unary `-`

<img src="docs/assets/media/addon/mode_custom.png" alt="Custom mode">

---

### Simulation Settings

#### Fixed step methods

- Euler  
- Heun (RK2)  
- Runge–Kutta 4 (RK4)

<img src="docs/assets/media/addon/fixed_dt.png" alt="Fixed dt settings">

#### Adaptive step methods

- Runge–Kutta–Fehlberg 4(5) (RKF45)  
- Dormand–Prince 5(4) (DP5)

<img src="docs/assets/media/addon/adaptive_dt.png" alt="Adaptive dt settings">

---

### Raw Data and Export

After building an attractor, the add-on provides:

- **Points** — a mesh containing all generated points  
- **Export** — CSV data:  
  `steps, dt, x, y, z`

`dt` varies for adaptive methods.

<img src="docs/assets/media/addon/output.png" alt="Output section">

---

### Post-Processing Tools

Available after generating a trajectory:

- **Trim** — remove start/end of the curve  
- **Simplify** — reduce point count  
- **Smooth to Bézier**

<img src="docs/assets/media/addon/post_processing.png" alt="Post-processing tools">

---

## Documentation

Full documentation (PL/EN):

**https://pcabala.github.io/AttractorBuilder/**  
(Enable GitHub Pages with `/docs` as the source.)

---

## Issues

If you have suggestions or encounter bugs, please open an Issue:

**https://github.com/pcabala/AttractorBuilder/issues**

---

## Requirements

- Blender **4.5+**  
- Works on Windows, Linux, macOS  
- No external Python installation required

---

## License

**GPL-2.0-or-later**

---

## Author

Paweł Cabała  
2024–2025
