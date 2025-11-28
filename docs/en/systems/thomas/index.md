---
layout: systems
title: "Thomas Attractor"
video_mp4: "/assets/media/attractors/thomas.mp4"
stop_at: 11
lang: en
alt_url: /pl/systemy/thomas/
---

<pre class="eq-plain">
Attractor Builder (Blender Add-on)
<b>Equations:</b>
ẋ = - b*x + sin(y)
ẏ = - b*y + sin(z)
ż = - b*z + sin(x)
<b>Parameters:</b>
| b = 0.15 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.01, y₀ = 0.02, z₀ = 0.03
Method: RK4
Time Step (dt): 0.03
Steps: 10000
Burn-in: 500
Scale: 0.7
</pre>

<p>
The <b>Thomas attractor</b> is an example of a three-dimensional nonlinear system
in which chaotic dynamics emerge from the structure of cyclic feedback between
the variables. It was described by René Thomas in a study devoted to feedback
circuits and their role in generating complex dynamical behaviour, including
various forms of deterministic chaos. The author introduces the general form
of the system (1999, p. 1896, Eq. 2):
</p>

<p class="mathline">\( \dot{x} = -b x + f(y), \)</p>
<p class="mathline">\( \dot{y} = -b y + f(z), \)</p>
<p class="mathline">\( \dot{z} = -b z + f(x), \)</p>

<p>
where \(b > 0\) is a damping coefficient and the function \(f\) introduces the
nonlinearity responsible for chaotic behaviour. Thomas demonstrated that many
different choices of \(f\)—including \(f(u)=\sin u\)—lead to chaotic trajectories
as long as the cyclic feedback structure is preserved. For values around
\(b \approx 0.15\), the system produces complex, aperiodic motion in which the
trajectories wrap repeatedly around symmetric regions of phase space. This model
is an example of the so-called “labyrinth chaos”, a phenomenon Thomas describes
as emerging from cyclic coupling combined with nonlinear response.
</p>

<p><b>Source:</b></p>
<p class="hanging-indent">
Thomas, R. (1999). Deterministic chaos seen in terms of feedback circuits:
analysis, synthesis, “labyrinth chaos”.
<i>International Journal of Bifurcation and Chaos</i>, 9(10), 1889–1905.
<a href="https://doi.org/10.1142/S0218127499001383" target="_blank">
https://doi.org/10.1142/S0218127499001383
</a>
</p>
