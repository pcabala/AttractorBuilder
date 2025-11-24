---
layout: methods
lang: en
title: Euler Method
permalink: /en/methods/euler/
alt_url: /pl/metody/euler/
---

<p><b>Essence.</b>  
The Euler method is the simplest way to approximate the solution of a differential
equation. At each time step, it uses only the value of the derivative at the current
point \( \mathbf{x}_n \). This derivative is interpreted as a vector indicating the
direction and speed of motion.  
The method assumes that over a short interval \( \Delta t \), the point moves along
a straight line defined by this derivative. For a system
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \),
the next point is approximated as:
\( \mathbf{x}_{n+1} = \mathbf{x}_n + \Delta t\, f(\mathbf{x}_n) .\)  
This means that the point is shifted by the derivative scaled by the time step
\( \Delta t \). Since the method relies solely on information from
\( \mathbf{x}_n \), it is fast but not very accurate.
</p>

<p><b>Example.</b>  
Consider the equation  
\( \dot{x} = -2x \) with initial condition \( x_0 = 1 \)  
and time step \( \Delta t = 0.1 \).<br>
<i>Step 1</i>: compute the derivative at \( x_0 = 1 \):  
\( f(x_0) = -2 \cdot 1 = -2 \).<br>
New approximation:  
\( x_1 = x_0 + 0.1 \cdot (-2) = 0.8 \).<br>
<i>Step 2</i>: derivative at \( x_1 = 0.8 \):  
\( f(x_1) = -2 \cdot 0.8 = -1.6 \).<br>
New approximation:  
\( x_2 = 0.8 + 0.1 \cdot (-1.6) = 0.64 \).<br>
<i>Step 3</i>: derivative: \( f(x_2) = -1.28 \).<br>
New approximation:  
\( x_3 = 0.64 + 0.1 \cdot (-1.28) = 0.512 \).<br>
Further steps proceed analogously. At each step, an error is created and
accumulates, because the method assumes a linear approximation of the derivative
over the entire interval \( \Delta t \).
</p>

<p><b>Usage.</b>  
The Euler method is effective only for very small time steps \( \Delta t \) and for
systems with gentle dynamics. In chaotic systems it quickly generates large
numerical errors, leading to distorted trajectories.  
For this reason, it is treated mainly as an educational method or as a starting
point for more advanced techniques such as Heun or RK4.
</p>

<p><b>Implementation.</b>  
In the Attractor Builder add-on, each Euler step is computed by the function
<code>step_euler</code>.  
It takes the system’s right-hand side function (<code>rhs_func</code>), the current state
vector <code>p</code>, a dictionary of parameters <code>params</code>, and the time step <code>dt</code>:

<code>
def step_euler(rhs_func, p: Vector, params: dict, dt: float):
    return p + rhs_func(p, params) * dt
</code>

<p>
The function <code>rhs_func</code> returns the derivative vector
\( (\dot{x}, \dot{y}, \dot{z}) \) evaluated at the current point and for the chosen
parameters \( a, b, c \).  
Calling <code>step_euler</code> computes the next point after a single time step
\( \Delta t = dt \).  
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
Method: Euler
Time step (dt): 0.1
Number of steps: 3
Burn-in: 0
Scale: 1
</pre>

<p>
At each step, the algorithm first computes the derivatives
\( (\dot{x}, \dot{y}, \dot{z}) \), and then updates the coordinates according to
\( x_{n+1} = x_n + \Delta t\,\dot{x}_n \):
</p>

<pre class="eq-plain">
<b>Step 1.</b> Initial point:
x0 = 0.01; y0 = 0.01; z0 = 0.01.
Derivatives:
dx0 = 10*(y0 - x0) = 10*(0.01 - 0.01) = 0
dy0 = x0*(28 - z0) - y0 ≈ 0.01*(28 - 0.01) - 0.01 ≈ 0.2699
dz0 = x0*y0 - (8/3)*z0 ≈ 0.01*0.01 - (8/3)*0.01 ≈ -0.02657
New point:
x1 = x0 + 0.01*dx0 = 0.01
y1 = y0 + 0.01*dy0 ≈ 0.01270
z1 = z0 + 0.01*dz0 ≈ 0.00973

<b>Step 2.</b> Starting point:
x1 = 0.01; y1 ≈ 0.01270; z1 ≈ 0.00973.
Derivatives (rounded):
dx1 = 10*(y1 - x1) ≈ 10*(0.01270 - 0.01) ≈ 0.02699
dy1 = x1*(28 - z1) - y1 ≈ 0.01*(28 - 0.00973) - 0.01270 ≈ 0.26720
dz1 = x1*y1 - (8/3)*z1 ≈ 0.01*0.01270 - (8/3)*0.00973 ≈ -0.02583
New point:
x2 = x1 + 0.01*dx1 ≈ 0.01027
y2 = y1 + 0.01*dy1 ≈ 0.01537
z2 = z1 + 0.01*dz1 ≈ 0.00948

<b>Step 3.</b> Starting point:
x2 ≈ 0.01027; y2 ≈ 0.01537; z2 ≈ 0.00948.
Derivatives (rounded):
dx2 = 10*(y2 - x2) ≈ 10*(0.01537 - 0.01027) ≈ 0.05101
dy2 = x2*(28 - z2) - y2 ≈ 0.01027*(28 - 0.00948) - 0.01537 ≈ 0.27209
dz2 = x2*y2 - (8/3)*z2 ≈ 0.01027*0.01537 - (8/3)*0.00948 ≈ -0.02511
New point:
x3 = x2 + 0.01*dx2 ≈ 0.01078
y3 = y2 + 0.01*dy2 ≈ 0.01809
z3 = z2 + 0.01*dz2 ≈ 0.00922
</pre>

<p>
In subsequent steps the procedure is the same: at each point, the derivatives are
computed and the Euler update rule is applied to advance the trajectory by one time
step \( \Delta t \).  
This example demonstrates how the general Lorenz system translates into explicit
numerical computations within the add-on.
</p>
