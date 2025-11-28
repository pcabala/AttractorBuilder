---
layout: systems
title: "Hindmarsh–Rose Attractor"
video_mp4: "/assets/media/attractors/hindmarsh-rose.mp4"
stop_at: 11
lang: en
alt_url: /pl/systemy/hindmarsh-rose/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = y - a*x**3 + b*x**2 + I - z  
ẏ = c - d*x**2 - y  
ż = r*(s*(x - x1) - z)
<b>Parameters:</b>
| a = 1.0 | b = 3.0 | c = 1.0 | d = 5.0 | s = 4.0 | r = 0.006 | x1 = -1.6 | I = 3.25 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.0, y₀ = 0.0, z₀ = 0.0  
Method: RK4  
Time step (dt): 0.005  
Number of steps: 50000  
Burn-in phase: 1000  
Scale: 0.5
</pre>

<!-- a) Context and historical background -->
<p>
The <b>Hindmarsh–Rose attractor</b> originates from neurobiology and was developed
by <i>J. L. Hindmarsh</i> and <i>R. M. Rose</i> in 1984 as a model describing
the electrical activity of a single neuron.  
The system reproduces transitions between resting states,
regular spiking, and rapid series of bursts (<i>bursting</i>)
characteristic of cortical neurons.  
Its trajectories show chaotic switching between these modes,
and the model became one of the first examples of applying nonlinear dynamics
to biological excitable systems.
The original system of equations (Hindmarsh & Rose, 1984, p.&nbsp;95, Eq.&nbsp;15) is given as:
</p>

<!-- b) Original system of equations -->
<div class="math-left">
\[
\begin{cases}
\dot{x} = y - a x^{3} + b x^{2} + I - z,\\[4pt]
\dot{y} = c - d x^{2} - y,\\[4pt]
\dot{z} = r\big(s(x - x_{1}) - z\big).
\end{cases}
\]
</div>

<style>
.math-left mjx-container[display="true"] { text-align: left !important; }  /* MathJax v3 */
.math-left .katex-display              { text-align: left !important; }  /* KaTeX */
</style>

<p>
The model includes three variables:  
\(x\) — the neuron’s membrane potential,  
\(y\) — fast ionic processes responsible for spike generation,  
\(z\) — slow calcium currents modulating the overall dynamics.  
The parameter values determine the qualitative nature of the neuron’s activity:  
variation of the input current \(I\) controls the transitions between rest,
periodic firing, and chaotic <i>bursting</i>.  
The authors emphasized that even such a simple three-variable system,
through nonlinear coupling between the fast and slow ionic channels,
is sufficient to produce complex, biologically realistic patterns of neuronal activity.
</p>

<!-- d) Source -->
<p><b>Source:</b></p>

<p class="hanging-indent">
Hindmarsh, J. L., & Rose, R. M. (1984).  
<i>A model of neuronal bursting using three coupled first order differential equations.</i>  
<i>Proceedings of the Royal Society of London. Series B. Biological Sciences</i>, 221(1222), 87–102.  
DOI: <a href="https://doi.org/10.1098/rspb.1984.0024" target="_blank">
https://doi.org/10.1098/rspb.1984.0024
</a>
</p>
