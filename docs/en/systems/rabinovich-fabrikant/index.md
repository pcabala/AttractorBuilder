---
layout: systems
title: "Rabinovich–Fabrikant Attractor"
video: "/assets/media/attractors/rabinovich-fabrikant.webm"
video_mp4: "/assets/media/attractors/rabinovich-fabrikant.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/rabinovich-fabrikant/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = y*(z - 1 + x**2) + a*x
ẏ = x*(3*z + 1 - x**2) + a*y
ż = -2*z*(b + x*y)
<b>Parameters:</b>
| a = 0.87 | b = 1.1 |   <!-- aliases in the add-on: a≡γ, b≡ν -->
<b>Simulation settings:</b>
Initial state: x₀ = -1, y₀ = 0, z₀ = 0.5  
Method: DP5  
Tolerance: 0.00005  
Step min: 0.000001  
Step max: 0.05  
Number of steps: 7000  
Burn-in phase: 1000  
Scale: 2
</pre>

<!-- a) Context and historical background -->
<p>
<b>The Rabinovich–Fabrikant attractor</b> was introduced in 1979 by
M. I. Rabinovich and A. L. Fabrikant from the Institute of Applied Physics,
Academy of Sciences of the USSR.  
It emerged from studies on the development of modulational instability
in nonlinear media under nonequilibrium conditions.  
The authors analyzed the process of wave self-modulation and demonstrated that
even a simple three-mode model describing the interaction between a primary wave
and its satellites can produce complex, aperiodic trajectories in phase space.
The original system of equations has the following form
(1979, p.&nbsp;311, Eq.&nbsp;2):
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x}=y\,(z-1+x^{2})+\gamma\,x\)</p>
<p class="mathline">\(\dot{y}=x\,(3z+1-x^{2})+\gamma\,y\)</p>
<p class="mathline">\(\dot{z}=-2z\,(\nu+x\,y)\)</p>

<!-- c) Parameters and interpretation -->
<p>
In the original publication, the parameter \(\gamma\) represents the instability
growth rate — it defines the level of activity of the medium and the effective
amplification of oscillations in the \(x\) and \(y\) channels.  
The parameter \(\nu\) denotes the damping of the satellites, corresponding to
energy loss in the medium due to dissipative interactions.  
For small values of the ratio \(\gamma/\nu\), the system stabilizes and exhibits
periodic behavior, whereas increasing this ratio leads to the formation of
limit cycles, bifurcations, and finally deterministic chaos.  
The authors reported that for \(\gamma \approx 0.87\) and \(\nu \approx 1.1\),
the trajectories form a complex attractor with an irregular structure.
</p>

<!-- d) Sources -->
<p><b>Sources:</b></p>

<p class="hanging-indent">
Rabinovich, M. I., &amp; Fabrikant, A. L. (1979).  
<i>Stochastic self-modulation of waves in nonequilibrium media.</i>  
<i>Soviet Physics JETP</i>, 50(2), 311–316.  
PDF: <a href="http://jetp.ras.ru/cgi-bin/dn/e_050_02_0311.pdf" target="_blank">
http://jetp.ras.ru/cgi-bin/dn/e_050_02_0311.pdf
</a>
</p>
