---
layout: systems
title: "Burke–Shaw Attractor"
video_mp4: "/assets/media/attractors/burke-shaw.mp4"
stop_at: 11
lang: en
alt_url: /pl/systemy/burke-shaw/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = -a * (x + y)
ẏ = -y - a * x * z
ż = a * x * y + b
<b>Parameters:</b>
| a = 10 | b = 13 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.1, y₀ = 0.0, z₀ = 0.0  
Method: RK4  
Time step (dt): 0.01  
Steps: 15000  
Burn-in: 500  
Scale: 0.3
</pre>

<!-- a) Context and historical background -->
<p>
The <b>Burke–Shaw attractor</b> was proposed by Robert Shaw in 1981
during his studies on nonlinear chaotic flows conducted jointly
with physicist Bill Burke.
It represents an example of an <i>unbounded strange attractor</i> —
a system without fixed points,
whose trajectories can extend infinitely along one axis.
The original system of equations (1981, p. 104) is given by:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x} = -10x - 10y\)</p>
<p class="mathline">\(\dot{y} = -10xz - y,\) \(\quad V = 13\)</p>
<p class="mathline">\(\dot{z} = 10xy + V\)</p>

<!-- c) Parameters and interpretation -->
<p>
In this system, the coefficient <i>a</i> defines the strength
of nonlinear coupling between <i>x</i> and <i>y</i>,
while the parameter <i>b</i> acts as a constant offset
in the equation for <i>z</i>,
causing a slow drift of trajectories along the <i>z</i>-axis.
Although the flow is not bounded,
its solutions form a locally organized structure
exhibiting chaotic features,
known as the Burke–Shaw attractor.
</p>

<!-- d) Source -->
<p>
<b>Source:</b> Shaw, R. (1981).
<i>Strange Attractors, Chaotic Behavior and Information Flow.</i>
<i>Zeitschrift für Naturforschung A</i>, 36(1), 80–112.  
<br>
Online access:
<a href="https://www.degruyterbrill.com/document/doi/10.1515/zna-1981-0115/html?lang=en" target="_blank">
https://www.degruyterbrill.com/document/doi/10.1515/zna-1981-0115/html?lang=en
</a>
</p>
