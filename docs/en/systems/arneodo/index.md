---
layout: systems
title: "Arneodo Attractor"
video: "/assets/media/attractors/arneodo.webm"
video_mp4: "/assets/media/attractors/arneodo.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/arneodo/
---

<pre class="eq-plain">
Attractor Builder (Blender Add-on)
<b>Equations:</b>
ẋ = a*(x-y)
ẏ = -4*a*y+x*z+m*x**3
ż = -d*a*z+x*y+b*z**2
<b>Parameters:</b>
| a = 1 | b = -0.09 | d = 1.5 | m = 0.01 |
<b>Simulation settings:</b>
Initial state: x₀ = 1, y₀ = 0.1, z₀ = 0.1
Method: Euler
Time Step (dt): 0.01
Steps: 15000
Burn-in: 1000
Scale: 0.1
</pre>

<p>
The <b>Arneodo attractor</b> was introduced in 1981 by Alain Arneodo, Paul Coullet,
and Christian Tresser as an example of a new mechanism for the onset of turbulence.
The authors studied three-dimensional differential systems that preserve the symmetry
\( S: (x, y, z) \mapsto (-x, -y, z) \),
for which a sequence of increasingly complex stable homoclinic orbits appears.
As the control parameter approaches a critical value, the system undergoes a series
of bifurcations resulting from the splitting of these homoclinic orbits, ultimately
leading to the formation of a chaotic attractor. The original system, introduced in
the 1981 paper (p. 220, Eq. 11), has the form:
</p>

<p class="mathline">\( \dot{x} = \alpha x - \alpha y \)</p>
<p class="mathline">\( \dot{y} = -4\alpha y + xz + \mu x^{3} \)</p>
<p class="mathline">\( \dot{z} = -\delta \alpha z + xy + \beta z^{2} \)</p>

<p>
In their numerical investigation, the authors fix the parameters
\(\alpha = 1.8\), \(\beta = -0.07\), and \(\delta = 1.5\), and then examine the evolution
of the system under changes in the control parameter \(\mu\). For
\(\mu \approx 0.076\) they observe a pair of stable homoclinic orbits. For
\(\mu = 0.05\) the system exhibits a stable symmetric periodic orbit, while for
\(\mu = 0.034\) a pair of stable orbits appears which are mutual images under the
symmetry \(S\). Further decreasing \(\mu\) produces — at \(\mu = 0.02\) — a complex geometric structure
that behaves as a strange attractor.
</p>

<p><b>Source:</b></p>
<p class="hanging-indent">
Arneodo, A., Coullet, P., & Tresser, C. (1981). A possible new mechanism for the onset of turbulence.
<i>Physics Letters A, 81(4), 197–201.</i>
DOI: <a href="https://doi.org/10.1016/0375-9601(81)90239-5" target="_blank">
https://doi.org/10.1016/0375-9601(81)90239-5
</a>
</p>
