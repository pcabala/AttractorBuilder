---
layout: systems
title: "Chua Attractor"
video: "/assets/media/attractors/chua.webm"
video_mp4: "/assets/media/attractors/chua.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/chua/
---

<pre class="eq-plain">
Attractor Builder (Blender Add-on)
<b>Equations:</b>
ẋ = k*p*(y - x - (b*x + 0.5*(a - b)*(fabs(x + 1) - fabs(x - 1))))
ẏ = k*(x - y + z)
ż = k*(-q*y - r*z)
<b>Parameters:</b>
| a = 0.1 | b = -0.48 | k = 1 | p = -1.3 | q = -0.0136 | r = -0.0297 |
<b>Simulation Settings:</b>
Initial state: x₀ = 0.1, y₀ = 0.0, z₀ = 0.0  
Method: DP5  
Tolerance: 0.0001  
Min step: 0.0001  
Max step: 0.1  
Steps: 20000  
Burn-in: 500  
Scale: 0.7
</pre>

<p>
<b>The Chua attractor</b> is one of the classic examples of chaos arising in
physical electronic systems. In his work on nonlinear dynamic networks,
Leon O. Chua (1983) sought simple feedback circuits capable of producing
complex, nonperiodic trajectories using only a single nonlinear element.
Building on this idea, Takashi Matsumoto (1984) presented the first
experimental and numerical demonstration of chaotic behavior in a real
RLC circuit containing the now-famous Chua diode. The final
dimensionless form of the oscillator proposed by Chua was introduced in
1995 and is given by the system:
</p>

<p class="mathline">\( \dfrac{dx}{dt} = k \alpha (\,y - x - f(x)\,), \)</p>
<p class="mathline">\( \dfrac{dy}{dt} = k (\,x - y + z\,), \)</p>
<p class="mathline">\( \dfrac{dz}{dt} = k (\, -\beta y - \gamma z\,). \)</p>

<p>
In this formulation, the nonlinearity is introduced through the
piecewise-linear function  
\( f(x) = b x + \tfrac{1}{2}(a - b)(|x + 1| - |x - 1|) \),  
which represents the characteristic of the so-called Chua diode.
</p>

<p><b>Sources:</b></p>

<p class="hanging-indent">
Matsumoto, T. (1984). A chaotic attractor from Chua’s circuit.  
<i>IEEE Transactions on Circuits and Systems</i>, 31(12), 1055–1058.  
<a href="https://doi.org/10.1109/TCS.1984.1085459" target="_blank">
https://doi.org/10.1109/TCS.1984.1085459
</a>
</p>

<p class="hanging-indent">
Chua, L. O. (1983). Dynamic Nonlinear Networks: State-of-the-Art.  
<i>IEEE International Symposium on Circuits and Systems</i>, 12, 2–6.  
<a href="https://doi.org/10.1109/TCS.1980.1084745" target="_blank">
https://doi.org/10.1109/TCS.1980.1084745
</a>
</p>

<p class="hanging-indent">
Chua, L. O. (1995). A glimpse of nonlinear phenomena from Chua’s oscillator.  
<i>Philosophical Transactions of the Royal Society A</i>, 353(1701), 3–12.  
<a href="https://www.jstor.org/stable/54515" target="_blank">
https://www.jstor.org/stable/54515
</a>
</p>
