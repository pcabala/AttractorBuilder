---
layout: systems
title: "Dadras Attractor"
video_mp4: "/assets/media/attractors/dadras.mp4"
stop_at: 11
lang: en
alt_url: /pl/systemy/dadras/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = y - a * x + b * y * z
ẏ = c * y - x * z + z
ż = d * x * y - h * z
<b>Parameters</b>:
| a = 3 | b = 2.7 | c = 1.7 | d = 2 | h = 9 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Method: DP5
Tolerance: 0.0001
Min step: 0.000001
Max step: 0.1
Steps: 10000
Burn-in: 2000
Scale: 0.2
</pre>

<!-- a) Context and historical background -->
<p>
The <b>Dadras attractor</b> was introduced by Sara Dadras and Hamid Reza Momeni (2009) as a new
three-dimensional autonomous chaotic system capable of generating <i>two</i>, <i>three</i>, and
<i>four</i>-scroll attractors by varying a single parameter. The system features five real
equilibria and rich nonlinear dynamics (including period-doubling and positive Lyapunov
exponents) and is dissipative for <i>c − (h + a) &lt; 0</i>. The original system proposed by
Dadras &amp; Momeni (2009, p. 3638) is given by equations:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x} = y - a x + b y z\)</p>
<p class="mathline">\(\dot{y} = c y - x z + z\)</p>
<p class="mathline">\(\dot{z} = d x y - h z\)</p>

<!-- c) Parameters and interpretation -->
<p>
Here <i>a</i> introduces linear damping in the <i>x</i>-component, while <i>b</i> scales the multiplicative
nonlinearity \(y z\) that folds trajectories. The parameter <i>c</i> controls linear growth in
<i>y</i> (with an additional +<i>z</i> drive), <i>d</i> couples \(x y\) into the <i>z</i>-equation, and <i>h</i>
sets linear damping in <i>z</i>. For the classical set (<i>a</i>=3, <i>b</i>=2.7, <i>c</i>=4.7, <i>d</i>=2, <i>h</i>=9)
the system produces a two-scroll chaotic attractor; changing <i>c</i> alone yields a three-scroll
(e.g., <i>c</i>=1.7) or four-scroll (e.g., <i>c</i>=3.9) structure, illustrating how small parameter
variations reorganize the attractor’s topology.
</p>

<!-- d) Source -->
<p>
<b>Source:</b> Dadras, S. &amp; Momeni, H. R. (2009).
<i>A novel three-dimensional autonomous chaotic system generating two, three and four-scroll attractors.</i>
Physics Letters A, 373(40), 3637–3642.
<br>
DOI:
<a href="https://doi.org/10.1016/j.physleta.2009.07.088" target="_blank">
10.1016/j.physleta.2009.07.088
</a>
</p>
