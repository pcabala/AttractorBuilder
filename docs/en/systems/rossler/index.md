---
layout: systems
title: "Rössler Attractor"
video: "/assets/media/attractors/rossler.webm"
video_mp4: "/assets/media/attractors/rossler.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/rossler/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = - (y + z)
ẏ = x + a*y
ż = b + z*(x - c)
<b>Parameters:</b>
| a = 0.2 | b = 0.2 | c = 5.7 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.01, y₀ = 0, z₀ = 0  
Method: RK4  
Time step (dt): 0.05  
Number of steps: 15000  
Burn-in phase: 1000  
Scale: 0.2
</pre>

<!-- a) Context and historical background -->
<p>
<b>The Rössler attractor</b> was introduced in 1976 by <i>Otto E. Rössler</i> from the
Institute for Physical and Theoretical Chemistry, University of Tübingen, Germany.
The model was conceived as a simplified analogue of the Lorenz system, aimed at
capturing the essence of deterministic nonperiodic flow — continuous chaos — with
a single quadratic nonlinearity.  
Rössler’s goal was to design the simplest possible continuous system that produces
a strange attractor while maintaining only one nonlinear term.  
The original system of equations has the following form
(1976, p.&nbsp;397, Eq.&nbsp;2):
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x}=-(y+z),\quad \dot{y}=x+0.2\,y,\quad \dot{z}=0.2+z\,(x-5.7).\)</p>

<p>
It contains only a single nonlinear term, \(z\,x\), making it one of the simplest
continuous-time systems exhibiting chaotic behavior.  
The model was conceived as a "model of a model"—a minimal analog of the Lorenz
system that retains the characteristic stretching and folding mechanism responsible
for deterministic chaos.
</p>

<!-- d) Sources -->
<p><b>Source:</b></p>

<p class="hanging-indent">
Rössler, O. E. (1976).  
An equation for continuous chaos.  
<i>Physics Letters A</i>, 57(5), 397–398.  
DOI: <a href="https://doi.org/10.1016/0375-9601(76)90101-8" target="_blank">
10.1016/0375-9601(76)90101-8
</a>
</p>
