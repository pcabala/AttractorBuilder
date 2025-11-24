---
layout: systems
title: "Li Attractor"
video: "/assets/media/attractors/li.webm"
video_mp4: "/assets/media/attractors/li.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/li/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = a * (y - x) + d * x * z
ẏ = k * x + f * y - x * z
ż = -e * x**2 + x * y + c * z
<b>Parameters</b>:
| a = 40 | c = 11/6 | d = 0.16 | e = 0.65 | f = 20 | k = 55 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.01, y₀ = 0, z₀ = 0
Method: DP5
Tolerance: 0.000001
Min Step: 0
Max Step: 0.01
Steps: 7000
Burn-in: 1000
Scale: 0.01
</pre>

<!-- a) Context and historical background -->
<p>
The <b>Li attractor</b> was introduced by Dequan Li in 2008 as a new chaotic system
derived from a Lorenz-type framework but extended with additional quadratic coupling terms.
Using trial-and-error numerical simulations, Li discovered that a smooth
three-dimensional autonomous system containing only four quadratic terms
can produce a <i>three-scroll chaotic attractor</i>.
Unlike the Lorenz and Chen systems, which generate two symmetric wings,
the Li system exhibits an additional central scroll that forms diagonally
between the classical pair of lobes.
The original system proposed by Li (2008, p. 389) is defined as:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x}(t) = a(y(t) - x(t)) + d\,x(t)\,z(t)\)</p>
<p class="mathline">\(\dot{y}(t) = k\,x(t) + f\,y(t) - x(t)\,z(t)\)</p>
<p class="mathline">\(\dot{z}(t) = -e\,x^{2}(t) + x(t)\,y(t) + c\,z(t)\)</p>

<!-- c) Parameters and interpretation -->
<p>
In this formulation, <i>a</i> controls the linear relaxation between <i>x</i> and <i>y</i>,
while <i>d</i> introduces a nonlinear feedback term \(x z\) that bends trajectories
in phase space.
Parameters <i>k</i> and <i>f</i> provide linear excitation and damping in the <i>y</i>-equation,
<i>e</i> shapes the parabolic curvature of the \(-e x^{2}\) term,
and <i>c</i> determines vertical contraction along the <i>z</i>-axis.
For the canonical set (<i>a</i>=40, <i>k</i>=55, <i>c</i>=11/6, <i>d</i>=0.16, <i>e</i>=0.65, <i>f</i>=20),
the system generates a three-scroll chaotic attractor.
The corresponding Lyapunov exponents
(<i>L₁</i>=0.2315, <i>L₂</i>=0, <i>L₃</i>=−1.987)
confirm a dissipative chaotic regime with a fractal dimension ≈ 2.12.
</p>

<!-- d) Source -->
<p>
<b>Source:</b> Li, D. (2008).
<i>A three-scroll chaotic attractor.</i>
Physics Letters A 372 (3–4), 387–393.  
<br>
DOI:
<a href="https://doi.org/10.1016/j.physleta.2007.07.045" target="_blank">
10.1016/j.physleta.2007.07.045
</a>
</p>
