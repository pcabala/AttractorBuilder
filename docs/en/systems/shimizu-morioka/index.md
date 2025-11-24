---
layout: systems
title: "Shimizu–Morioka Attractor"
video: "/assets/media/attractors/shimizu-morioka.webm"
video_mp4: "/assets/media/attractors/shimizu-morioka.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/shimizu-morioka/
---

<pre class="eq-plain">
Attractor Builder (Blender Add-on)
<b>Equations (implementation version):</b>
ẋ = y
ẏ = (1 - z) * x - a * y
ż = x**2 - b * z
<b>Parameters:</b>
| a = 0.7 | b = 0.1 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.1, y₀ = 0.0, z₀ = 0.2
Method: RK4
Time Step (dt): 0.01
Steps: 50000
Burn-in: 500
Scale: 1.5
</pre>

<p>
The <b>Shimizu–Morioka attractor</b> belongs to a class of three-dimensional
nonlinear dynamical systems that preserve key features of the Lorenz model
while admitting a simpler analytic structure. Its origins lie in the work of
T. Shimizu and N. Morioka, who studied a reduced two-dimensional model
describing the bifurcation of a symmetric limit cycle into a pair of asymmetric
cycles—behaviour strongly reminiscent of the transitions seen in the Lorenz
equations. In their 1980 paper the authors analyse this “simple model” in
detail, focusing on symmetry breaking and the onset of complex periodic
behaviour. In subsequent research, A. L. Shilnikov introduced a three-dimensional system
that is now widely referred to as the <i>Shimizu–Morioka model</i>, using it as a
normal form for analysing bifurcations of the Lorenz attractor. The system is
given by (1993, p. 338, Eq. 1):
</p>

<p class="mathline">\( \dot{x} = y \)</p>
<p class="mathline">\( \dot{y} = x - \lambda y - xz \)</p>
<p class="mathline">\( \dot{z} = -\alpha z + x^{2} \)</p>

<p>
The parameters \(\lambda > 0\) and \(\alpha > 0\) control the dissipative
properties of the flow: \(\lambda\) determines the damping in the \(y\)-equation,
while \(\alpha\) describes the relaxation rate of the variable \(z\).
For suitable values—typically \(\lambda \approx 0.7\) and \(\alpha \approx 0.1\)—
the system produces a non-stationary, chaotic motion in which trajectories
wrap repeatedly around two distinct lobes without ever closing, generating
a strange attractor whose geometry resembles that of the Lorenz attractor.
</p>

<p><b>Sources:</b></p>
<p class="hanging-indent">
Shimizu, T., &amp; Morioka, N. (1980). On the bifurcation of a symmetric limit cycle
to an asymmetric one in a simple model. <i>Physics Letters A, 76(3–4), 201–204.</i>
DOI: <a href="https://doi.org/10.1016/0375-9601(80)90466-1" target="_blank">
https://doi.org/10.1016/0375-9601(80)90466-1</a>
</p>
<p class="hanging-indent">
Shil'nikov, A. L. (1993). On bifurcations of the Lorenz attractor
in the Shimizu–Morioka model. <i>Physica D: Nonlinear Phenomena, 62(1–4), 338–346.</i>
DOI: <a href="https://doi.org/10.1016/0167-2789(93)90292-9" target="_blank">
https://doi.org/10.1016/0167-2789(93)90292-9</a>
</p>
