---
layout: systems
title: "Chen Attractor"
video: "/assets/media/attractors/chen.webm"
video_mp4: "/assets/media/attractors/chen.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/chen/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = a * (y - x)
ẏ = (c - a) * x - x * z + c * y
ż = x * y - b * z
<b>Parameters</b>:
| a = 35 | b = 3 | c = 28 |
<b>Simulation settings:</b>
Initial state: x₀ = 0, y₀ = 1, z₀ = 1
Method: RK4
Time Step (dt): 0.005
Steps: 20000
Burn-in: 1000
Scale: 0.1
</pre>

<!-- a) Context and historical background -->
<p>
The <b>Chen attractor</b> was introduced in 1999 by Guanrong Chen and Tetsushi Ueta
as a new chaotic system discovered during research on <i>anticontrol of chaos</i> —
the process of deliberately inducing chaos in an otherwise nonchaotic system.
Although its equations closely resemble those of the Lorenz system,
the Chen system is <i>not topologically equivalent</i> to either the Lorenz or the Rössler attractors.
Its discovery provided an important example showing that small structural differences
in nonlinear dynamical equations can produce distinct types of chaotic behavior.
The original system proposed by Chen & Ueta (1999, p. 1465) is given by equations:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x} = a (y - x)\)</p>
<p class="mathline">\(\dot{y} = (c - a)x - xz + cy\)</p>
<p class="mathline">\(\dot{z} = xy - bz\)</p>

<!-- c) Parameters and interpretation -->
<p>
In this model, the parameter <i>a</i> represents the strength of the coupling
between the <i>x</i> and <i>y</i> components, <i>b</i> governs the rate of dissipation
along the <i>z</i> axis, and <i>c</i> influences both the linear amplification
and the nonlinear feedback through the <i>y</i>- and <i>xz</i>-terms.
For the classical parameter set (<i>a</i>=35, <i>b</i>=3, <i>c</i>=28),
the system exhibits a complex double-scroll chaotic attractor
resembling the Lorenz structure but with different equilibrium topology.
Despite visual similarity, no linear or nonlinear coordinate transformation
can convert the Chen system into the Lorenz system — proving
their dynamical inequivalence.
</p>

<!-- d) Source -->
<p>
<b>Źródło:</b> 
<br>
Chen, G. & Ueta, T. (1999).
<i>Yet Another Chaotic Attractor.</i>
International Journal of Bifurcation and Chaos, 9 (7), 1465–1466.
DOI:
<a href="https://doi.org/10.1142/S0218127499001024" target="_blank">
10.1142/S0218127499001024
</a>
</p>
