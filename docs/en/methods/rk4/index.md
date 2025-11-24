---
layout: methods
lang: en
title: Runge–Kutta Method
permalink: /en/methods/rk4/
alt_url: /pl/metody/rk4/
---

<p><b>Essence.</b>  
The fourth-order Runge–Kutta method (RK4) is one of the most widely used
techniques for integrating ordinary differential equations.  
Like the Heun method, it is based on averaging slopes, but instead of using two
approximations of the derivative, it evaluates <i>four</i> derivative estimates
within a single time step \( \Delta t \).  
For a system  
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \),  
RK4 uses four slope vectors:

<br><br>
\( \mathbf{k}_1 = f(\mathbf{x}_n) \),<br>
\( \mathbf{k}_2 = f\big(\mathbf{x}_n + \tfrac{\Delta t}{2} \mathbf{k}_1\big) \),<br>
\( \mathbf{k}_3 = f\big(\mathbf{x}_n + \tfrac{\Delta t}{2} \mathbf{k}_2\big) \),<br>
\( \mathbf{k}_4 = f\big(\mathbf{x}_n + \Delta t\, \mathbf{k}_3\big) \).<br><br>

The next state value is then computed as a weighted average of these slopes:

<p class="mathline">
\( \displaystyle 
\mathbf{x}_{n+1} = \mathbf{x}_n + \frac{\Delta t}{6}
\big( \mathbf{k}_1 + 2\mathbf{k}_2 + 2\mathbf{k}_3 + \mathbf{k}_4 \big).
\)
</p>

<p>
Intuitively, one may think of RK4 as a multi-stage refinement of the Euler step:
the intermediate slopes \( \mathbf{k}_2, \mathbf{k}_3, \mathbf{k}_4 \) probe how
the derivative changes at the midpoint and at the end of the step.  
Thanks to this, the method achieves order 4, and its global error is typically
orders of magnitude smaller than that of Euler or Heun for the same time step
\( \Delta t \).
</p>

<p><b>Example.</b>  
Consider again the simple equation  
\( \dot{x} = -2x \) with initial value \( x_0 = 1 \)
and time step \( \Delta t = 0.1 \).  
For each iteration we compute four slopes and their weighted average.
In the first step (from \( x_0 \) to \( x_1 \)) we have  
\( f(x) = -2x \), and the slopes are:

<br><br>
\( k_1 = f(x_0) = -2 \cdot 1 = -2 \),<br>
\( k_2 = f(x_0 + 0.5 \Delta t \, k_1)
= f(1 + 0.5 \cdot 0.1 \cdot (-2)) = f(0.9) = -1.8 \),<br>
\( k_3 = f(x_0 + 0.5 \Delta t \, k_2)
= f(1 + 0.5 \cdot 0.1 \cdot (-1.8)) = f(0.91) = -1.82 \),<br>
\( k_4 = f(x_0 + \Delta t \, k_3)
= f(1 + 0.1 \cdot (-1.82)) = f(0.818) = -1.636 \).<br><br>

Weighted average:  
\( \bar{k} = \tfrac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
\approx \tfrac{1}{6}(-2 - 3.6 - 3.64 - 1.636) \approx -1.818 \).<br>

Thus the new point is:  
\( x_1 = x_0 + \Delta t\, \bar{k}
\approx 1 + 0.1 \cdot (-1.818) \approx 0.8182. \)<br><br>

For comparison: Euler gives \( x_1 = 0.8 \),  
Heun gives \( x_1 = 0.82 \),  
and RK4 yields \( x_1 \approx 0.8182 \),  
which is closer to the exact value \( x(t) = e^{-2t} \)
(for \( t = 0.1 \), \( e^{-0.2} \approx 0.8187 \)).  
In subsequent steps we repeat the same procedure: compute  
\( k_1, k_2, k_3, k_4 \) based on \( x_n \), and then combine them
into \( x_{n+1} \).  
For a given \( \Delta t \), RK4 produces significantly smaller errors than
Euler or Heun, though it requires more function evaluations (four instead of
one or two).
</p>

<p><b>Usage.</b>  
RK4 is often considered a “golden mean” between accuracy and computational
cost.  
It performs extremely well in many engineering and scientific contexts,  
including chaotic trajectories—provided the time step \( \Delta t \)  
is chosen sensibly.  
If the step is too large, chaos may still distort the trajectory,
but RK4’s stability margin and geometric fidelity are much better  
than in Euler or Heun.  
In practice RK4 is usually the first choice when one needs high-quality
integration with a fixed time step.
</p>

<p><b>Implementation.</b>  
In the Attractor Builder add-on, each RK4 step is performed by the  
function <code>step_rk4</code>.  
As in the Heun method, we use the right-hand side function  
<code>rhs_func</code>, which returns the derivative vector  
\( (\dot{x}, \dot{y}, \dot{z}) \) for given coordinates and parameters.  
The Python implementation (simplified to the form used in the add-on)
is:
</p>

<code>
def step_rk4(rhs_func, p: Vector, params: dict, dt: float):  
    k1 = rhs_func(p, params)  
    k2 = rhs_func(p + 0.5 * dt * k1, params)  
    k3 = rhs_func(p + 0.5 * dt * k2, params)  
    k4 = rhs_func(p + dt * k3, params)  
    return p + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
</code>

<p>
The procedure follows exactly the formulas above.  
Step 1 computes the derivative at the current point \( p \).  
Step 2 moves half a step in the direction of \( k_1 \) and evaluates the
derivative there.  
Step 3 repeats the half-step, now using \( k_2 \).  
Step 4 advances a full step in the direction of \( k_3 \) and computes the
derivative at the end of the step.  
Finally, Step 5 constructs the weighted combination of  
\( k_1, k_2, k_3, k_4 \) with weights 1–2–2–1.  
For example, using the Lorenz system in Attractor Builder:
</p>

<pre class="eq-plain">
<b>Equations:</b>
dx/dt = a * (y - x)
dy/dt = x * (b - z) - y
dz/dt = x * y - c * z

<b>Parameters:</b>
| a = 10 | b = 28 | c = 8/3 |

<b>Simulation settings:</b>
Initial state: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Method: RK4
Time step (dt): 0.01
Number of steps: 3
Burn-in: 0
Scale: 1
</pre>

<p>
In each RK4 step the algorithm evaluates  
<code>rhs_func</code> four times, generating slope vectors  
\( \mathbf{k}_1, \mathbf{k}_2, \mathbf{k}_3, \mathbf{k}_4 \).  
It then computes their weighted average following the RK4 scheme.
As a result, the trajectory points  
\( (x_1, y_1, z_1), (x_2, y_2, z_2), (x_3, y_3, z_3) \)  
closely reflect the true shape of the Lorenz attractor,  
far better than those obtained via Euler or Heun with the same step  
\( \Delta t = 0.01 \).  
These points can be obtained directly from the Attractor Builder add-on using  
Raw Data → Export.  
The CSV file contains the initial state in the first row and the coordinates
after each integration step in subsequent rows.  
For the settings shown above, the exported data look as follows:
</p>

<style>
.table-eq td, .table-eq th {
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
    font-size: 0.90rem;
    text-align: center;
    padding: 0.25rem 0.5rem;
}
.table-eq thead th {
    font-weight: 700;
}
</style>

<table class="table-eq">
<thead>
<tr><th>steps</th><th>dt</th><th>x</th><th>y</th><th>z</th></tr>
</thead>
<tbody>
<tr><td>0</td><td>0.00000</td><td>0.01000</td><td>0.01000</td><td>0.01000</td></tr>
<tr><td>1</td><td>0.01000</td><td>0.01013</td><td>0.01270</td><td>0.00974</td></tr>
<tr><td>2</td><td>0.01000</td><td>0.01051</td><td>0.01544</td><td>0.00948</td></tr>
<tr><td>3</td><td>0.01000</td><td>0.01111</td><td>0.01829</td><td>0.00924</td></tr>
</tbody>
</table>

<p>
Row \(0\) contains the initial state  
\( (x_0, y_0, z_0) = (0.01, 0.01, 0.01) \).  
Rows 1–3 correspond to the points  
\( (x_1, y_1, z_1) \),  
\( (x_2, y_2, z_2) \),  
\( (x_3, y_3, z_3) \)  
obtained using RK4.  
This representation allows for easy comparison of integration methods,  
trajectory analysis, and export to tools such as Python, MATLAB, or Excel.
</p>
