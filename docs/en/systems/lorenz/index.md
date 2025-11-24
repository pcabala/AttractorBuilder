---
layout: systems
title: "Lorenz Attractor"
video: "/assets/media/attractors/lorenz.webm"
video_mp4: "/assets/media/attractors/lorenz.mp4"
alpha: true
stop_at: 11
lang: en
alt_url: /pl/systemy/lorenz/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = a * (y - x)
ẏ = x * (b - z) - y
ż = x * y - c * z
<b>Parameters</b>:
| a = 10 | b = 28 | c = 8/3 |
<b>Simulation settings:</b>
Initial state: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Method: RK4
Time Step (dt): 0.01
Steps: 15000
Burn-in: 500
Scale: 0.1
</pre>

<!-- a) Context and historical background -->
<p>
The <b>Lorenz attractor</b> originates from a simplified model of atmospheric convection
developed by Edward N. Lorenz in 1963 at the Massachusetts Institute of Technology.
While studying a truncated system of equations for thermal fluid motion, Lorenz discovered
that deterministic equations could yield apparently irregular, non-repeating trajectories.
This finding challenged the prevailing assumption of predictability in deterministic physics
and marked the birth of modern chaos theory.
The system became one of the most recognizable examples of a <i>strange attractor</i>
and a paradigm for sensitive dependence on initial conditions — the so-called
“butterfly effect.” The original system proposed by Lorenz (1963, pp. 135) 
is given by equations:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{X} = -\sigma X + \sigma Y\)</p>
<p class="mathline">\(\dot{Y} = -XZ + rX - Y\)</p>
<p class="mathline">\(\dot{Z} = XY - bZ\)</p>

<!-- c) Parameters and interpretation -->
<p>
In this formulation, <i>σ</i> represents the Prandtl number, expressing the ratio
between momentum and thermal diffusivity, while <i>r</i> is a control parameter
analogous to a reduced Rayleigh number that measures the temperature gradient
driving convection. The coefficient <i>b</i> determines the geometric aspect ratio
and vertical contraction of the convective flow.  
In the Blender add-on notation these parameters correspond to
<i>a = σ</i>, <i>b = r</i>, and <i>c = b</i>.  
For the classical parameter set (<i>a</i>=10, <i>b</i>=28, <i>c</i>=8/3),
the system produces aperiodic but bounded oscillations, generating
the characteristic double-wing pattern of the Lorenz attractor.
Even infinitesimal differences in the initial conditions grow exponentially,
illustrating the essence of deterministic chaos.
</p>

<!-- d) Sources -->
<p><b>Source:</b></p>

<p class="hanging-indent">
Lorenz, E. N. (1963).
<i>Deterministic Nonperiodic Flow.</i>
Journal of the Atmospheric Sciences, 20(2), 130–141.
DOI: 
<a href="https://doi.org/10.1175/1520-0469(1963)020&lt;0130:DNF&gt;2.0.CO;2" target="_blank">
10.1175/1520-0469(1963)020&lt;0130:DNF&gt;2.0.CO;2
</a>
</p>
