---
layout: systems
title: "Newton–Leipnik Attractor"
video: "/assets/media/attractors/newton-leipnik.webm"
video_mp4: "/assets/media/attractors/newton-leipnik.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/newton-leipnik/
---

<pre class="eq-plain">
Attractor Builder (Blender Add-on)
<b>Equations:</b>
ẋ = -b*x + y + 10*y*z
ẏ = -x - b*y + 5*x*z
ż =  a*z - 5*x*y
<b>Parameters:</b>
| a = 0.175 | b = 0.4 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.349, y₀ = 0, z₀ = -0.18
Method: RK4
Time Step (dt): 0.01
Steps: 50000
Burn-in: 0
Scale: 3
</pre>

<p>
The <b>Newton–Leipnik attractor</b> was introduced in 1981 by R.B. Leipnik and
T.A. Newton in their study of rigid body motion with linear feedback control.
By modifying the classical Euler equations and adding a linear feedback term,
the authors obtained a three–dimensional quadratic dynamical system exhibiting
surprisingly complex behavior. The original system presented in their paper
has the form (1981, p. 65, Eq. 10):
</p>

<p class="mathline">\( \dot{x} = -0.4\,x + y + 10\,y z \)</p>
<p class="mathline">\( \dot{y} = -x - 0.4\,y + 5\,x z \)</p>
<p class="mathline">\( \dot{z} = \alpha z - 5\,x y \)</p>

<p>
For the parameter \(\alpha = 0.175\), the system generates two coexisting
strange attractors. Which of them a trajectory converges to depends entirely
on the initial conditions. The authors demonstrated that even a very small
change in the third coordinate can send the trajectory to a different
attractor: the point \((0.349,\,0,\,-0.160)\) leads to the upper attractor (U),
while \((0.349,\,0,\,-0.180)\) leads to the lower attractor (L).

The two attractors have visibly different geometry. The U–attractor is broader
and more irregular, while the L–attractor is tighter and more structured.
The coexistence of two chaotic sets in such a smooth system is rare. The
boundary between their basins of attraction is highly intricate, reflecting
the system’s strong sensitivity to minimal changes in the initial state.
The oscillating, looping trajectories characteristic of this motion were
described by the authors using the evocative term “dipsy–doodle”.
</p>

<p><b>Source:</b></p>
<p class="hanging-indent">
Leipnik, R. B., & Newton, T. A. (1981). Double strange attractors in rigid body motion with linear feedback control.
<i>Physics Letters A, 86(2), 63–67.</i>
DOI: <a href="https://doi.org/10.1016/0375-9601(81)90165-1" target="_blank">
https://doi.org/10.1016/0375-9601(81)90165-1
</a>
</p>
