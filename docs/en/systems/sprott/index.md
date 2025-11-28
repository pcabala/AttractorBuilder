---
layout: systems
title: "Sprott Attractors"
video_mp4: "/assets/media/attractors/sprott.mp4"
stop_at: 11
lang: en
alt_url: /pl/systemy/sprott/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = -y
ẏ = x + z
ż = x*z + a*y**2 
<b>Parameters:</b>
| a = 3 |  
<b>Simulation settings:</b>
Initial state: x₀ = 0.1, y₀ = 0, z₀ = 0  
Method: RK4  
Time step (dt): 0.01  
Number of steps: 30000  
Burn-in phase: 500  
Scale: 0.7
</pre>

<p>
<b>The Sprott attractors</b> form a family of simple chaotic systems
introduced by <i>Julien C. Sprott</i> in 1994.  
The author analyzed the general form of three-dimensional autonomous differential equations
with quadratic nonlinearities and identified nineteen distinct examples
exhibiting deterministic chaos.  
These systems — labeled from A to S — are remarkably simple:
each contains only five or six terms, with one or two nonlinearities.  
Below are all systems (A–S) in their original form (1994, p.&nbsp;649, Table&nbsp;I):
</p>

<p>A: <span class="mathline">\(\dot{x}=y,\ \dot{y}=-x+y\,z,\ \dot{z}=1-y^{2}\)</span></p>
<p>B: <span class="mathline">\(\dot{x}=y\,z,\ \dot{y}=x-y,\ \dot{z}=1-x\,y\)</span></p>
<p>C: <span class="mathline">\(\dot{x}=y\,z,\ \dot{y}=x-y,\ \dot{z}=1-x^{2}\)</span></p>
<p>D: <span class="mathline">\(\dot{x}=-y,\ \dot{y}=x+z,\ \dot{z}=x\,z+3\,y^{2}\)</span></p>
<p>E: <span class="mathline">\(\dot{x}=y\,z,\ \dot{y}=x^{2}-y,\ \dot{z}=1-4\,x\)</span></p>
<p>F: <span class="mathline">\(\dot{x}=y+z,\ \dot{y}=-x+0.5\,y,\ \dot{z}=x^{2}-z\)</span></p>
<p>G: <span class="mathline">\(\dot{x}=0.4\,x+z,\ \dot{y}=x\,z-y,\ \dot{z}=-x+y\)</span></p>
<p>H: <span class="mathline">\(\dot{x}=-y+z^{2},\ \dot{y}=x+0.5\,y,\ \dot{z}=x-z\)</span></p>
<p>I: <span class="mathline">\(\dot{x}=-0.2\,y,\ \dot{y}=x+z,\ \dot{z}=x+y^{2}-z\)</span></p>
<p>J: <span class="mathline">\(\dot{x}=2\,z,\ \dot{y}=-2\,y+z,\ \dot{z}=-x+y+y^{2}\)</span></p>
<p>K: <span class="mathline">\(\dot{x}=x\,y-z,\ \dot{y}=x-y,\ \dot{z}=x+0.3\,z\)</span></p>
<p>L: <span class="mathline">\(\dot{x}=y+3.9\,z,\ \dot{y}=0.9\,x^{2}-y,\ \dot{z}=1-x\)</span></p>
<p>M: <span class="mathline">\(\dot{x}=-z,\ \dot{y}=-x^{2}-y,\ \dot{z}=1.7+1.7\,x+y\)</span></p>
<p>N: <span class="mathline">\(\dot{x}=-2\,y,\ \dot{y}=x+z^{2},\ \dot{z}=1+y-2\,z\)</span></p>
<p>O: <span class="mathline">\(\dot{x}=y,\ \dot{y}=x-z,\ \dot{z}=x+x\,z+2.7\,y\)</span></p>
<p>P: <span class="mathline">\(\dot{x}=2.7\,y+z,\ \dot{y}=-x+y^{2},\ \dot{z}=x+y\)</span></p>
<p>Q: <span class="mathline">\(\dot{x}=-z,\ \dot{y}=x-y,\ \dot{z}=3.1\,x+y^{2}+0.5\,z\)</span></p>
<p>R: <span class="mathline">\(\dot{x}=0.9-y,\ \dot{y}=0.4+z,\ \dot{z}=x\,y-z\)</span></p>
<p>S: <span class="mathline">\(\dot{x}=-x-4\,y,\ \dot{y}=x+z^{2},\ \dot{z}=1+x\)</span></p>

<p>
Cases A–E contain five terms and two nonlinearities, while F–S have six terms and one.
They are three-dimensional dissipative systems with strange attractors,
often exhibiting a spiral structure with a single fold, similar to the Rössler attractor.  
In the Blender add-on, the system corresponding to attractor D is provided,
which belongs to the group of systems with two nonlinearities.  
It features a complex spiral motion with a single focus point
and a folded-band structure reminiscent of the Rössler attractor.  
This is one of the classical examples where a simple set of equations
produces rich, irregular trajectories in phase space.  
These simple systems generating deterministic chaos were later
described in detail by Sprott in his book <i>Elegant Chaos: Algebraically Simple Chaotic Flows</i> (2010),
which provides a comprehensive overview of algebraically simple three-dimensional chaotic flows.
</p>

<!-- d) Sources -->
<p><b>Sources:</b></p>

<p class="hanging-indent">
Sprott, J. C. (1994).  
<i>Some simple chaotic flows.</i>  
<i>Physical Review E</i>, 50(2), 647–650.  
DOI: <a href="https://doi.org/10.1103/PhysRevE.50.R647" target="_blank">
https://doi.org/10.1103/PhysRevE.50.R647
</a>
</p>
<p class="hanging-indent">
Sprott, J. C. (2010).  
<i>Elegant Chaos: Algebraically Simple Chaotic Flows.</i>  
World Scientific Publishing, Singapore.  
DOI: <a href="https://doi.org/10.1142/7183" target="_blank">
https://doi.org/10.1142/7183
</a>
</p>
