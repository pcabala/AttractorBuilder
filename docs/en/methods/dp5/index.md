---
layout: methods
lang: en
title: Dormand–Prince Method
permalink: /en/methods/dp5/
alt_url: /pl/metody/dp5/
---

<p><b>Essence.</b>  
The Dormand–Prince 5(4) method (DP5) is an adaptive Runge–Kutta method of orders
5 and 4, similar in spirit to RKF45 but based on a different choice of
coefficients.  
The Dormand–Prince variant was designed so that the 5th–order solution (the
main approximation) has particularly small global error, while the 4th–order
solution is used only for estimating the local error.  
For a system  
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \),  
the method computes slope vectors  
\( \mathbf{k}_1, \dots, \mathbf{k}_7 \)  
according to the Butcher tableau, and then uses them to construct the 5th–order
approximation \( \mathbf{y}_5 \), together with a 4th–order embedded estimate.  
The difference between the two approximations provides the local error
estimate for the current step.  
Based on this estimate the time step \( \Delta t \) is adjusted, just as in
RKF45: if the error is below the tolerance, the step is accepted and  
<i>the step size may increase</i>; if the error exceeds the tolerance, the step
is rejected and the solver automatically <i>reduces</i> the step size.
</p>

<p><b>Usage.</b>  
The Dormand–Prince method is one of the most widely used adaptive schemes in
practical ODE solvers (it is the basis of MATLAB's well-known “ode45”).  
Compared with RKF45, DP5 places stronger emphasis on minimizing the global
error of the 5th–order solution, which often yields higher-quality
trajectories for a similar number of steps.  
Thanks to adaptive step-size selection, the method is well suited for
visualizing complex attractor trajectories such as Lorenz or Rössler, where
the sampling density must automatically adjust to the local dynamics.
</p>

<p><b>Implementation.</b>  
In the Attractor Builder add-on, each step of the Dormand–Prince 5(4) method  
is executed by  
<code>step_dp5(rhs_func, p: Vector, params: dict, current_dt: float, tolerance: float)</code>.  
DP5, like RKF45, uses a Butcher tableau — a structured set of coefficients
defining time-shifts (matrix \( A \)) and linear combination weights  
(\( B \), \( B^* \)) from which two solution approximations are constructed:
the 5th-order main solution and the embedded 4th-order estimate.  
The full Dormand–Prince 5(4) tableau is given in  
(Hairer, Nørsett & Wanner 1993, Table&nbsp;5.2, p.&nbsp;178),  
while the general theory of Butcher tableaux is summarized in  
(Butcher 2008, Chapter&nbsp;5, p.&nbsp;96).

The first stage computes the slopes  
\( \mathbf{k}_1, \dots, \mathbf{k}_6 \)  
according to matrix \( A \):

<code>
k1 = rhs_func(p, params)
k2 = rhs_func(p + current_dt * A[1][0] * k1, params)
k3 = rhs_func(p + current_dt * (A[2][0]*k1 + A[2][1]*k2), params)
k4 = rhs_func(p + current_dt * (A[3][0]*k1 + A[3][1]*k2 + A[3][2]*k3), params)
k5 = rhs_func(p + current_dt * (A[4][0]*k1 + A[4][1]*k2 + A[4][2]*k3 + A[4][3]*k4), params)
k6 = rhs_func(p + current_dt * (A[5][0]*k1 + A[5][1]*k2 + A[5][2]*k3 + A[5][3]*k4 + A[5][4]*k5), params)
</code>

Then the 5th–order approximation is computed using the weights \( B \):

<code>
y5 = p + current_dt * (B[0]*k1 + B[1]*k2 + B[2]*k3 + B[3]*k4 + B[4]*k5 + B[5]*k6)
</code>

Additionally we compute  
<code>k7 = rhs_func(y5, params)</code>  
which is used for the embedded 4th–order estimate via weights \( B^* \).

The local error vector is

<code>
all_k = [k1, k2, k3, k4, k5, k6, k7]
error_vec = current_dt * sum([(b - bs) * k for b, bs, k in zip(B, B_star, all_k)], Vector())
error = error_vec.length
</code>

i.e., the difference between the 5th–order main solution and the embedded
4th–order estimate.  
From this we compute the optimal next step:

<code>
optimal_dt = 0.9 * current_dt * (tolerance / error)**0.2
</code>

If <code>error &lt;= tolerance</code>, the step is accepted (the next trajectory
point is <code>y5</code>).  
If the error is too large, the step is rejected and retried with  
<code>optimal_dt</code>.  
As with RKF45, the function <code>step_dp5</code> returns the triple:  
<code>(new_point, proposed_dt, acceptance_flag)</code>.
</p>

<p><b>Example.</b> Consider the Lorenz system:</p>

<pre class="eq-plain">
<b>Equations:</b>
dx/dt = a * (y - x)
dy/dt = x * (b - z) - y
dz/dt = x * y - c * z

<b>Parameters:</b>
| a = 10 | b = 28 | c = 8/3 |

<b>Simulation settings:</b>
Initial state: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Method: DP5
Tolerance: 0.000001
min_dt: 0.000001
max_dt: 0.05
Recorded steps: 3
Burn-in: 1000
Scale: 1
</pre>

<p>
Using the Raw Data → Export function in the Attractor Builder add-on,  
we obtain CSV data with columns <code>steps</code>, <code>dt</code>, <code>x</code>, 
<code>y</code>, <code>z</code>.  
For the settings above, the first four rows of the CSV file are:
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
<tr><td>2</td><td>0.02895</td><td>0.01184</td><td>0.02099</td><td>0.00902</td></tr>
<tr><td>3</td><td>0.02933</td><td>0.01549</td><td>0.03131</td><td>0.00835</td></tr>
</tbody>
</table>

<p>
The first row corresponds to the initial state  
\( (x_0, y_0, z_0) = (0.01, 0.01, 0.01) \),  
with <code>dt = 0</code>.  
In the subsequent rows we see how the Dormand–Prince method adapts the step size:
after the first step, <code>dt</code> grows from 0.01 to about 0.029 (step 3),  
indicating that in this region the motion is sufficiently regular to allow
larger steps without violating the error tolerance.
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
