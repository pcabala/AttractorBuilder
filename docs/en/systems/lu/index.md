---
layout: systems
title: "Lü Attractor"
video_mp4: "/assets/media/attractors/lu.mp4"
stop_at: 11
lang: en
alt_url: /pl/systemy/lu/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = a * (y - x)
ẏ = c * y - x * z
ż = x * y - b * z
<b>Parameters:</b>
| a = 36 | b = 3 | c = 20 |
<b>Simulation settings:</b>
Initial conditions: x₀ = 0.1, y₀ = 0.1, z₀ = 0.1
Method: RK4  
Time Step (dt): 0.005  
Steps: 10000  
Burn-in: 300  
Scale: 0.1
</pre>

<!-- a) Context and historical background -->
<p>
The <b>Lü attractor</b> was introduced in 2002 by Jian Lü and Guanrong Chen
as a new three-dimensional chaotic system that bridges the gap between
the classical Lorenz (1963) and Chen (1999) attractors.  
By continuously varying its parameters, the Lü system can exhibit
a smooth transition from Lorenz-type to Chen-type chaos,
revealing an intermediate form of chaotic behavior.
The original system of equations (Lü & Chen, 2002, p. 660) is given as:
</p>

<div class="math-left">
\[
\begin{cases}
\dot{x} = a\,(y - x),\\
\dot{y} = -x z + c\,y,\\
\dot{z} = x y - b\,z,
\end{cases}
\]
</div>

<style>
.math-left mjx-container[display="true"] { text-align: left !important; }  /* MathJax v3 */
.math-left .katex-display              { text-align: left !important; }  /* KaTeX */
</style>

<!-- b) Parameters and interpretation -->
<p>
The parameter <i>a</i> defines the coupling strength between variables <i>x</i> and <i>y</i>,
<i>b</i> controls the dissipation along the <i>z</i>-axis,
and <i>c</i> determines the amplification in the <i>y</i> direction.  
For <i>a = 36</i>, <i>b = 3</i>, and <i>c</i> in the approximate range
12.7–28.5, the system exhibits chaotic behavior,
producing a double-scroll structure reminiscent of the Lorenz attractor.
</p>

<!-- c) Source -->
<p>
<b>Source:</b> Lü, J., & Chen, G. (2002).  
<i>A new chaotic attractor coined.</i>  
<i>International Journal of Bifurcation and Chaos</i>, 12(3), 659–661.  
DOI: <a href="https://doi.org/10.1142/S0218127402004620" target="_blank">
10.1142/S0218127402004620
</a>
</p>
