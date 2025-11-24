---
layout: methods
lang: en
permalink: /en/methods/
title:
alt_url: /pl/metody/
---

<p>
<b>Numerical methods</b> make it possible to determine how the position of a point 
in space changes over time. The trajectory of a system is obtained by approximating 
successive positions of this point, which are defined by an ordinary differential 
equation (ODE).
</p>

<p>
A system of differential equations has the form 
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \), 
where \( \mathbf{x} \) is the state vector (e.g. \( (x, y, z) \)) and 
the function \( f \) specifies the direction and speed of motion at a given moment. 
The same system can also be written as 
\( \tfrac{d\mathbf{x}}{dt} = f(\mathbf{x}, t, \theta) \) or 
\( \mathbf{x}' = f(\mathbf{x}, t, \theta) \).
This notation indicates that the position of the point is not given directly — 
the system only specifies its <em>instantaneous change</em>. To compute a trajectory, 
we start from the initial point \( \mathbf{x}_0 \) and follow its motion according 
to this rule.
</p>

<p>
The solution of \( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \) is a function 
describing the motion of the point, \( t \mapsto \mathbf{x}(t) \). To approximate it, 
we choose a time step \( \Delta t \) and construct a sequence of points 
\( \mathbf{x}_0, \mathbf{x}_1, \mathbf{x}_2, \ldots \), corresponding to the moments 
\( t_0, t_0 + \Delta t, t_0 + 2\,\Delta t, \ldots \). 
Each numerical method defines a rule for obtaining 
\( \mathbf{x}_{n+1} \) from \( \mathbf{x}_n \). 
These methods differ in how they use information about derivatives. 
Methods used in practice fall into two groups — fixed-step and adaptive methods.
</p>

<p>
<b>Example.</b> In three-dimensional systems, a point in space is represented by 
the triple \( (x, y, z) \). The Lorenz system is a particular instance of the 
general form \( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \). 
Here the state vector is \( \mathbf{x} = (x, y, z) \), and the function \( f \) 
specifies the three derivatives \( (\dot{x}, \dot{y}, \dot{z}) \) based on the 
current position. Writing out the coordinate equations gives:

\( \dot{x} = \sigma (y - x) \), 
\( \dot{y} = x (\rho - z) - y \), 
\( \dot{z} = x y - \beta z \).

At each moment the system specifies the instantaneous change of the point’s 
position based on its current state \( (x, y, z) \). To obtain a trajectory, 
numerical methods approximate successive positions after time increments 
\( \Delta t \). In summary, to compute the trajectory of 
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \), we start from the initial point 
\( \mathbf{x}_0 \), evaluate the derivative 
\( f(\mathbf{x}_0, t_0, \theta) \), and move the point accordingly. 
Using the time step \( \Delta t \), we obtain the next position \( \mathbf{x}_1 \), 
then repeat the procedure to get 
\( \mathbf{x}_2, \mathbf{x}_3, \ldots \).
</p>

<p>
<b>Fixed methods</b> use a constant step size \( \Delta t \); after each step 
the point is advanced by the same time increment, regardless of how rapidly 
the dynamics of the system change. Fixed-step methods include:<br>
<a href="/en/methods/euler/">Euler’s method</a>,<br>
<a href="/en/methods/heun/">Heun’s method</a>,<br>
<a href="/en/methods/rk4/">Runge–Kutta method</a>.
</p>

<p>
<b>Adaptive methods</b> automatically adjust the value of \( \Delta t \) depending 
on the behaviour of the system: they reduce the step when the solution varies 
rapidly and increase it when the dynamics are smoother. They use additional 
error estimates to control the accuracy of the computation. Adaptive methods include:<br>
<a href="/en/methods/rkf45/">RKF45</a>,<br>
<a href="/en/methods/dp5/">Dormand–Prince method</a>.
</p>

<br>
<p><b>Sources:</b></p>

<p class="hanging-indent">
Atkinson, K. (1989). <i>An Introduction to Numerical Analysis</i>. Wiley.
</p>

<p class="hanging-indent">
Butcher, J. C. (2008). <i>Numerical Methods for Ordinary Differential Equations</i>.
Wiley.
</p>

<p class="hanging-indent">
Hairer, E., Nørsett, S., Wanner, G. (1993). 
<i>Solving Ordinary Differential Equations I</i>. Springer.
</p>

<p class="hanging-indent">
Sundnes, J. (2024). <i>Solving Ordinary Differential Equations in Python</i>. 
Simula SpringerBriefs on Computing. Springer.
</p>
