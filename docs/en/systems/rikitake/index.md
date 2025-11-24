---
layout: systems
title: "Rikitake Attractor"
video: "/assets/media/attractors/rikitake.webm"
video_mp4: "/assets/media/attractors/rikitake.mp4"
alpha: true
stop_at: 11
lang: en
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = -b * x + z * y
ẏ = -b * y + (z - a) * x
ż = 1 - x * y
<b>Parameters:</b>
| a = 5 | b = 2 |
<b>Simulation settings:</b>
Initial state: x₀ = 1, y₀ = 1, z₀ = 1  
Method: RK4  
Time step (dt): 0.01  
Steps: 20000  
Burn-in: 500  
Scale: 0.4
</pre>

<!-- a) Context and historical background -->
<p>
The <b>Rikitake attractor</b> originates from the two-disk dynamo model
proposed by Tsuneji Rikitake in 1957
to explain irregular reversals of the Earth's magnetic field.
The model describes two coupled electrical circuits
driving and influencing each other through magnetic induction.
In its original physical formulation (1957, pp. 90–91),
the system was written as follows:
</p>

<!-- b) System of equations -->
<p class="mathline">\(
L_1 \frac{dI_1}{dt} + R_1 I_1 = 2\pi M \Omega_1 I_2,
\)</p>
<p class="mathline">\(
L_2 \frac{dI_2}{dt} + R_2 I_2 = 2\pi N \Omega_2 I_1,
\)</p>
<p class="mathline">\(
G_1 \frac{d\Omega_1}{dt} = G_1 - 2\pi M I_1 I_2,
\quad
G_2 \frac{d\Omega_2}{dt} = G_2 - 2\pi N I_1 I_2.
\)</p>

<!-- c) Parameters and interpretation -->
<p>
Rikitake showed that for certain parameter values,
the coupled equations for the electric currents (<i>I₁, I₂</i>)
and angular velocities (<i>Ω₁, Ω₂</i>)
produce irregular—chaotic—oscillations
that could model geomagnetic polarity reversals.
After simplifying and nondimensionalizing the system,
the model reduces to the classical three-variable
form now known as the Rikitake attractor (McMillen, 1999, pp. 1):
</p>

<!-- d) Dimensionless system -->
<p class="mathline">\(\dot{x} = -\mu x + y z\)</p>
<p class="mathline">\(\dot{y} = -\mu y + (z - a)x\)</p>
<p class="mathline">\(\dot{z} = 1 - x y\)</p>

<!-- e) Parameters and interpretation -->
<p>
In the Blender add-on implementation,
parameters <i>a</i> and <i>b</i> correspond to the coupling strength
and damping coefficient (the analog of <i>μ</i>).
For <i>a = 5</i> and <i>b = 2</i>, the system generates
the well-known double-wing chaotic attractor,
illustrating spontaneous polarity switches—an analogy
to the Earth's geomagnetic field reversals.
</p>

<!-- f) Sources -->
<p>
<b>Sources:</b><br>
Rikitake, T. (1957).
<i>Oscillations of a System of Disk Dynamos.</i>
<i>Proceedings of the Cambridge Philosophical Society</i>, 54(1), 89–105.  
DOI:
<a href="https://doi.org/10.1017/S0305004100033223" target="_blank">
10.1017/S0305004100033223
</a>
<br>
McMillen, T. (1999).
<i>The Shape and Dynamics of the Rikitake Attractor.</i>
<i>The Nonlinear Journal</i>, 1, 1–10.
</p>
