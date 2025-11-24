---
layout: systems
title: "Halvorsen Attractor"
video: "/assets/media/attractors/halvorsen.webm"
video_mp4: "/assets/media/attractors/halvorsen.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/halvorsen/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = -a*x - 4*y - 4*z - y**2
ẏ = -a*y - 4*z - 4*x - z**2
ż = -a*z - 4*x - 4*y - x**2
<b>Parameters:</b>
| a = 1.4 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.01, y₀ = 0, z₀ = 0.01
Method: DP5
Tolerance: 0.0001
Min step: 0.000001
Max step: 0.1
Steps: 10000
Burn-in: 300
Scale: 0.2
</pre>

<!-- a) Context and historical background -->
<p>
The <b>Halvorsen attractor</b> is a symmetric three-dimensional chaotic system
originally proposed by Arne Dehli Halvorsen in the 1990s
on the Usenet discussion group <i>sci.fractals</i>.
It later gained attention when Julien C. Sprott analyzed it formally
and published his results in 1997 in the note
<i>A Symmetric Chaotic Flow</i> (University of Wisconsin–Madison).
The attractor is notable for its cyclic symmetry and elegant,
three-lobed geometry, making it both mathematically interesting
and visually appealing.
The original system of equations (Sprott, 1997, Eq. 1) is given as:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x} = -a x - 4y - 4z - y^{2}\)</p>
<p class="mathline">\(\dot{y} = -a y - 4z - 4x - z^{2}\)</p>
<p class="mathline">\(\dot{z} = -a z - 4x - 4y - x^{2}\)</p>

<!-- c) Parameters and interpretation -->
<p>
This system is characterized by its complete cyclic symmetry:
the equations remain unchanged under the transformation
\(x \rightarrow y \rightarrow z \rightarrow x\).
The single parameter <i>a</i> controls the level of damping
and determines the transition from periodic to chaotic behavior.
Sprott demonstrated that for values around <i>a ≈ 1.27</i>,
the system follows a classical period-doubling route to chaos,
producing a complex and aesthetically symmetric strange attractor.
</p>


<!-- e) Source -->
<p>
<b>Source:</b><br>
Sprott, J. C. (1997, revised 2004).  
<i>A Symmetric Chaotic Flow.</i>  
Department of Physics, University of Wisconsin–Madison.  
Online:  
<a href="https://sprott.physics.wisc.edu/chaos/symmetry.htm" target="_blank">
https://sprott.physics.wisc.edu/chaos/symmetry.htm
</a>
</p>
