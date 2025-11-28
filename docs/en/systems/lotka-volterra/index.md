---
layout: systems
title: "Lotka–Volterra Attractor"
video_mp4: "/assets/media/attractors/lotka-volterra.mp4"
stop_at: 11
lang: en
alt_url: /pl/systemy/lotka-volterra/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = x - x*y + c*x**2 - a*z*x**2
ẏ = -y + x*y
ż = -b*z + a*z*x**2
<b>Parameters:</b>
| a = 2.9851 | b = 3.0 | c = 2.1 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.9, y₀ = 0.9, z₀ = 0.5 
Method: RK4  
Time Step: 0.01 
Steps: 15000
Burn-in: 50   
Scale: 10
</pre>

<!-- a) Context and historical background -->
<p>
The classical <b>Lotka–Volterra model</b> (1925–1926) describes the cyclic dynamics
of a predator–prey system in two dimensions. The trajectories of this system
are closed orbits around a fixed point, representing stable and periodic
oscillations of population sizes.  
In 1988, Nikola Samardzija and Lawrence D. Greller proposed a
three-dimensional generalization of this model, extending the classical
formulation by introducing an additional species and a nonlinear coupling
between variables.  
In this new version, the system generates complex oscillations,
bifurcations, and transitions to chaos.  
The original system of equations (1988, p. 466) is given as:
</p>

<!-- b) Original system of equations -->
<p class="mathline">\(\dot{X} = X - XY + CX^{2} - AZX^{2}\)</p>
<p class="mathline">\(\dot{Y} = -Y + XY\)</p>
<p class="mathline">\(\dot{Z} = -BZ + AZX^{2}\)</p>

<!-- c) Parameters and interpretation -->
<p>
The parameters <i>A</i>, <i>B</i>, and <i>C</i> are positive (<i>A, B, C &gt; 0</i>).
They control the strength of interactions between species:
<i>A</i> defines the nonlinear coupling between predators,
<i>B</i> describes the damping rate of the <i>Z</i> population,
and <i>C</i> represents the self-reinforcing growth of <i>X</i>.
The authors demonstrated that this system can produce
chaotic trajectories and a fractal torus, providing an example
of an <i>“explosive route to chaos.”</i>
</p>

<!-- d) Sources -->
<p>
<b>Sources:</b><br>
Lotka, A. J. (1925). <i>Elements of Physical Biology.</i> Williams & Wilkins, Baltimore.<br>
Samardzija, N., & Greller, L. D. (1988). <i>Explosive route to chaos through a fractal torus in a generalized Lotka–Volterra model.</i> <i>Bulletin of Mathematical Biology</i>, 50(5), 465–491. DOI: <a href="https://www.sciencedirect.com/science/article/abs/pii/S009282408880003X" target="_blank">10.1016/S0092-8240(88)80003-X</a><br>
Volterra, V. (1926). <i>Variazioni e fluttuazioni del numero d’individui in specie animali conviventi.</i> <i>Memorie della Reale Accademia Nazionale dei Lincei</i>, 2(6), 31–113.
</p>
