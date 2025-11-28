---
layout: systems
title: "Langford Attractor"
video_mp4: "/assets/media/attractors/langford.mp4"
stop_at: 11
lang: en
alt_url: /pl/systemy/langford/
---




<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = (z - b) * x - d * y
ẏ = d * x + (z - b) * y
ż = c + a * z - (z**3)/3 - (x**2 + y**2) * (1 + e * z)
<b>Parameters</b>:
| a = 0.95 | b = 0.7 | c = 0.6 | d = 3.5 | e = 0.25 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.1, y₀ = 0.0, z₀ = 0.0
Method: RK4
Time Step (dt): 0.015
Steps: 15000
Burn-in: 300
Scale: 0.1
</pre>


<!-- a) Context and historical background -->
<p>
The <b>Langford attractor</b> is a mathematical model of a chaotic system introduced by
Canadian mathematician William F. Langford in 1984 during his numerical studies
of the interaction between <i>Hopf</i> and <i>hysteresis</i> bifurcations.
It was one of the first smooth three-dimensional systems to demonstrate
how the coupling of these bifurcations can lead to <i>torus breakdown</i>
and the onset of chaos.  
Although it is sometimes confused with the Aizawa attractor,
Langford’s work provided the first formal formulation of this
type of torus-breakdown dynamics, while Aizawa 
introduced a related simplified version of the system.
The original system proposed by Langford (1984, p. 287) is given by equations:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x} = (z - \beta)x - \omega y\)</p>
<p class="mathline">\(\dot{y} = \omega x + (z - \beta)y\)</p>
<p class="mathline">\(\dot{z} = \mu + \alpha z - \tfrac{1}{3}z^{3} - (x^{2} + y^{2})(\ell + p z) + \varepsilon z x^{3}\)</p>


<!-- c) Parameters and interpretation -->
<p>
In this formulation, the parameters <i>μ</i>, <i>α</i>, and <i>β</i> govern the
local growth rates and stability of the stationary states.
he pair <i>ℓ</i> and <i>p</i> determine the onset and geometry of the
Naimark–Sacker (secondary Hopf or torus) bifurcation,
while the frequency <i>ω</i> controls the rotational motion
in the <i>x–y</i> plane.
The parameter <i>ε</i> introduces <i>non-axisymmetric</i> perturbations
that destroy the smooth invariant torus and initiate
a cascade of bifurcations — phase locking, period doubling, and
eventually chaotic dynamics.
As <i>ε</i> increases, the attractor evolves from a smooth torus to a
fractal "thick torus" and finally to transient chaos.
</p>

<!-- d) Source -->
<p>
<b>Source:</b> Langford, W. F. (1984).
<i>Numerical Studies of Torus Bifurcations.</i>
In: <i>International Series of Numerical Mathematics</i>, Vol. 70,
Birkhäuser Verlag, Basel, pp. 285–295.
<br>
DOI:
<a href="https://doi.org/10.1007/978-3-0348-6256-1_19" target="_blank">
10.1007/978-3-0348-6256-1_19
</a>
</p>


