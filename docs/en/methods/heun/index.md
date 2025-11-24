---
layout: methods
lang: en
title: Heun Method
permalink: /en/methods/heun/
alt_url: /pl/metody/heun/
---

<p><b>Essence.</b>  
The Heun method is a simple improvement over the Euler method.  
Instead of relying solely on the derivative at the initial point  
\( \mathbf{x}_n \), it uses the <i>average</i> slope at the beginning  
and at the end of the time step \( \Delta t \).  
For a system  
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \),  
the method first performs an Euler step (the predictor):
\( \mathbf{x}_{n+1}^{(p)} = \mathbf{x}_n + \Delta t\, f(\mathbf{x}_n) \),  
and then corrects this result (the corrector):
\( \mathbf{x}_{n+1} = \mathbf{x}_n + \tfrac{\Delta t}{2}\big[ f(\mathbf{x}_n) + f(\mathbf{x}_{n+1}^{(p)}) \big] \).  
Instead of assuming a constant slope across the entire interval (as in Euler),  
Heun's method averages the slope from the beginning and the end of the step.  
This yields a significantly lower global error than Euler,  
while keeping the computational cost relatively small.
</p>

<p><b>Example.</b>  
For the equation  
\( \dot{x} = -2x \) with initial condition \( x_0 = 1 \)  
and time step \( \Delta t = 0.1 \).  
Each step consists of two stages: predictor and corrector.
</p>

<p>
<i>Step 1</i> (from \( x_0 \) to \( x_1 \)).  
Derivative at \( x_0 = 1 \):  
\( f(x_0) = -2 \cdot 1 = -2 \) (predictor),  
predictor value:  
\( x_{1}^{(p)} = x_0 + 0.1 \cdot (-2) = 0.8 \),  
derivative at the predicted point \( x_{1}^{(p)} = 0.8 \):  
\( f(x_{1}^{(p)}) = -2 \cdot 0.8 = -1.6 \).  
New approximation (average slope):
\( x_1 = x_0 + \tfrac{0.1}{2}\big[ f(x_0) + f(x_{1}^{(p)}) \big] 
= 1 + 0.05 \cdot (-2 - 1.6) = 0.82. \)
</p>

<p>
<i>Step 2</i> (from \( x_1 \) to \( x_2 \)).  
Predictor: \( f(x_1) = -2 \cdot 0.82 = -1.64 \),  
\( x_{2}^{(p)} = 0.82 + 0.1 \cdot (-1.64) = 0.656 \).  
Corrector: \( f(x_{2}^{(p)}) = -2 \cdot 0.656 = -1.312 \),  
\( x_2 = 0.82 + 0.05 \cdot (-1.64 - 1.312) \approx 0.6724. \)
</p>

<p>
Further steps proceed in the same way:  
first compute the derivative at \( x_n \),  
then perform an Euler step to obtain \( x_{n+1}^{(p)} \),  
and finally correct the result by averaging the slopes at both points.  
Compared to the Euler method, the resulting sequence \( x_n \)  
is closer to the exact solution even for the same time step \( \Delta t \).
</p>

<p><b>Usage.</b>  
The Heun method offers a good balance between simplicity and accuracy.  
It typically produces more stable trajectories than Euler,  
especially for moderately sized time steps.  
In chaotic systems one must still choose \( \Delta t \) carefully,  
but for many attractors the Heun method yields visibly “cleaner” trajectories  
than Euler for the same step size.  
In practice, Heun is useful when Euler produces excessive distortion  
or when one wants a quick improvement in accuracy without moving  
to higher-order methods such as RK4 or Dormand–Prince.
</p>

<p><b>Implementation.</b>  
In the Attractor Builder add-on, each Heun step is performed by  
the function <code>step_heun</code>.  
Unlike Euler, which uses only the derivative at the current point,  
Heun computes the derivative twice: at the current point and at the  
predicted point (the predictor).  
The implementation is:
</p>

<code>
def step_heun(rhs_func, p: Vector, params: dict, dt: float):  
    p_pred = p + rhs_func(p, params) * dt  
    avg_slope = 0.5 * (rhs_func(p, params) + rhs_func(p_pred, params))  
    return p + avg_slope * dt
</code>

<p>
The algorithm proceeds as follows:<br>
1. Compute the derivative at the current point \( p \):  
\( f(p) = rhs\_func(p, params) \).<br>
2. Predictor (Euler step):  
\( p^{(p)} = p + \Delta t \, f(p) \).<br>
3. Compute the derivative at the predicted point \( p^{(p)} \):  
\( f(p^{(p)}) \).<br>
4. Average the slopes:  
\( \tfrac{1}{2}[ f(p) + f(p^{(p)}) ] \).<br>
5. Compute the new point:  
\( p_{n+1} = p + \Delta t \cdot \tfrac{1}{2}[ f(p) + f(p^{(p)}) ] \).  
For example, in the Attractor Builder we choose the Lorenz system:
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
Method: Heun
Time step (dt): 0.01
Number of steps: 3
Burn-in: 0
Scale: 1
</pre>

<pre class="eq-plain">
<b>Step 1.</b> Initial point: x0 = 0.01; y0 = 0.01; z0 = 0.01.
Derivatives:
dx0 = 10*(y0 - x0) = 10*(0.01 - 0.01) = 0
dy0 = x0*(28 - z0) - y0 = 0.01*(28 - 0.01) - 0.01 = 0.2699
dz0 = x0*y0 - (8/3)*z0 ≈ 0.0001 - 0.02667 ≈ -0.02657

Predictor (Euler):
x_pred = x0 + 0.01*dx0 = 0.01
y_pred = y0 + 0.01*dy0 = 0.01 + 0.01*0.2699 ≈ 0.01270
z_pred = z0 + 0.01*dz0 ≈ 0.01 + 0.01*(-0.02657) ≈ 0.00973

Derivatives at predicted point (rounded):
dxp = 10*(y_pred - x_pred) ≈ 10*(0.01270 - 0.01) ≈ 0.0270
dyp ≈ 0.2672
dzp ≈ -0.0258

Average slopes:
dx_avg ≈ (dx0 + dxp)/2 ≈ 0.0135
dy_avg ≈ (dy0 + dyp)/2 ≈ 0.2686
dz_avg ≈ (dz0 + dzp)/2 ≈ -0.0262

New point (after Step 1):
x1 ≈ 0.0101349
y1 ≈ 0.0126855
z1 ≈ 0.0097380

<b>Step 2.</b> Starting point: x1 ≈ 0.0101349; y1 ≈ 0.0126855; z1 ≈ 0.0097380.
[compute predictor, derivatives, and average slope analogously]
New point:
x2 ≈ 0.0105128
y2 ≈ 0.0154176
z2 ≈ 0.0094832

<b>Step 3.</b> Starting point: x2 ≈ 0.0105128; y2 ≈ 0.0154176; z2 ≈ 0.0094832.
After applying the predictor and corrector:
x3 ≈ 0.0111181
y3 ≈ 0.0182607
z3 ≈ 0.0092354
</pre>

<p>
At each step, the algorithm first computes the derivative vector  
at the current point (predictor, equivalent to Euler),  
then computes it again at the predicted point and averages the two slopes.  
This produces a trajectory that better reflects the true shape of the attractor  
compared to a simple Euler method with the same time step \( \Delta t \).
</p>
