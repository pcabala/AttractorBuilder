---
layout: methods
lang: en
title: Runge–Kutta–Fehlberg Method
permalink: /en/methods/rkf45/
alt_url: /pl/metody/rkf45/
---

<p><b>Essence.</b>  
The Runge–Kutta–Fehlberg method 4(5) (RKF45) is a classical example of an
<i>adaptive</i> numerical integrator for ordinary differential equations.  
It combines two Runge–Kutta formulas of different orders (4 and 5) within a
single computational scheme.  
For a system  
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \),  
each step evaluates six slope vectors  
\( \mathbf{k}_1, \dots, \mathbf{k}_6 \),  
which are used to compute two approximations of the solution:  
\( \mathbf{y}_4 \) — the 4th-order estimate, and  
\( \mathbf{y}_5 \) — the more accurate 5th-order estimate.  
Their difference \( \mathbf{y}_4 - \mathbf{y}_5 \) provides an estimate of
the local truncation error.  
Based on this error, the time step \( \Delta t \) is adjusted: if the error is
below the chosen tolerance, the step is <i>accepted</i> and the step size may
be <i>increased</i>; if not, the step is <i>rejected</i> and repeated with a
<i>smaller</i> step.  
This mechanism keeps the local error under control while minimizing the total
number of steps.
</p>

<p><b>Usage.</b>  
RKF45 is one of the most popular adaptive time-stepping schemes.  
For chaotic trajectories it typically provides a better balance between
accuracy and computational cost compared to fixed-step methods
(Euler, Heun, RK4) with a single rigid choice of  
\( \Delta t \).  
Instead of trying to manually guess a “good” fixed step, the user specifies
a tolerance (e.g. \( 10^{-5} \)) and a range of allowable step sizes,  
and the method automatically adapts the step during the simulation.
</p>

<p><b>Implementation.</b>  
In the Attractor Builder add-on, each step of the Runge–Kutta–Fehlberg 4(5)
method is executed by  
<code>step_rkf45(rhs_func, p: Vector, params: dict, current_dt: float, tolerance: float)</code>.  
The method is based on Fehlberg’s coefficient tables — a specific instance of
Butcher tableaux used to describe Runge–Kutta methods.  
The matrix \( A \) defines the time-shift coefficients that determine how the
slopes <b>k</b><sub>2</sub>, <b>k</b><sub>3</sub>, … are computed as linear
combinations of earlier slopes <b>k</b><sub>1</sub>, <b>k</b><sub>2</sub>, etc.  
The weight vectors \( B \) and \( B^* \) produce two solution estimates:
the 5th-order main approximation (weights \( B \)) and the embedded 4th-order
approximation (weights \( B^* \)).  
Their difference gives the local error estimate and determines whether the step
is accepted and how the next step size is chosen.  

The Fehlberg 4(5) tableau used here appears in  
(Hairer, Nørsett & Wanner 1993, Table 5.1, p. 177),  
while the general structure of Butcher tableaux is described in  
(Butcher 2008, p. 98).

The slopes according to the Fehlberg tableau are:

<code>
k1 = rhs_func(p, params)
k2 = rhs_func(p + A[1][0] * current_dt * k1, params)
k3 = rhs_func(p + current_dt * (A[2][0]*k1 + A[2][1]*k2), params)
k4 = rhs_func(p + current_dt * (A[3][0]*k1 + A[3][1]*k2 + A[3][2]*k3), params)
k5 = rhs_func(p + current_dt * (A[4][0]*k1 + A[4][1]*k2 + A[4][2]*k3 + A[4][3]*k4), params)
k6 = rhs_func(p + current_dt * (A[5][0]*k1 + A[5][1]*k2 + A[5][2]*k3 + A[5][3]*k4 + A[5][4]*k5), params)
</code>

<p>
From these we obtain the two solution approximations:
</p>

<code>
y4 = p + current_dt * (B_star[0]*k1 + B_star[2]*k3 + B_star[3]*k4 + B_star[4]*k5)
y5 = p + current_dt * (B[0]*k1 + B[2]*k3 + B[3]*k4 + B[4]*k5 + B[5]*k6)
</code>

<p>
Their difference  
\( e = \| \mathbf{y}_5 - \mathbf{y}_4 \| \)  
provides the local error estimate.  
If the error is below the tolerance, the step is accepted and  
\( \mathbf{y}_5 \) becomes the next point of the trajectory.  
Otherwise the step is rejected, the time step is reduced, and the solver repeats
the iteration.  
Thus \( \Delta t \) automatically adapts to the local complexity of the
trajectory: it increases in smooth regions and decreases where the dynamics
changes rapidly, preserving stability and accuracy at minimal cost.
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
Method: RKF45
Tolerance: 0.000001
min_dt: 0.000001
max_dt: 0.05
Recorded steps: 3
Burn-in: 0
Scale: 1
</pre>

<p>
Using the Raw Data → Export option in the Attractor Builder add-on, we can
examine precisely how the adaptive RKF45 method selects the time step at each
stage.  
The first four points from the exported CSV look as follows:
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
<tr><td>2</td><td>0.02685</td><td>0.01166</td><td>0.02034</td><td>0.00907</td></tr>
<tr><td>3</td><td>0.02697</td><td>0.01481</td><td>0.02956</td><td>0.00845</td></tr>
</tbody>
</table>

<p>
We clearly see that after the first step the adaptive algorithm increases the
step size from 0.01 to roughly 0.0269 in the third step.  
This indicates that in this region the trajectory is smoother, allowing the
solver to take larger steps without losing accuracy.  
Such behavior is one of the main advantages of adaptive methods over fixed-step
integrators.
</p>

<br>
<p><b>Sources:</b></p>

<p class="hanging-indent">
Butcher, J. C. (2008). <i>Numerical Methods for Ordinary Differential Equations</i>.  
Wiley.
</p>

<p class="hanging-indent">
Hairer, E., Nørsett, S., Wanner, G. (1993).  
<i>Solving Ordinary Differential Equations I</i>. Springer.
</p>
