---
layout: systems
title: "Nosé–Hoover Attractor"
video_mp4: "/assets/media/attractors/nose-hoover.mp4"
stop_at: 11
lang: en
alt_url: /pl/systemy/nose-hoover/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Equations:</b>
ẋ = y
ẏ = -x - z*y
ż = a * (y**2 - 1)
<b>Parameters:</b>
| a = 1.5 |
<b>Simulation settings:</b>
Initial state: x₀ = 1.0, y₀ = 0.0, z₀ = 0.0  
Method: RK4  
Time step (dt): 0.01  
Number of steps: 10000  
Burn-in phase: 500  
Scale: 1
</pre>

<!-- a) Context and historical background -->
<p>
<b>The Nosé–Hoover attractor</b> emerged as a by-product of a deterministic
method for controlling temperature in molecular dynamics simulations.
The mechanism, developed by Shuichi Nosé (1984) and simplified by
William G. Hoover (1985), was designed to maintain constant temperature
in dynamical systems by adding a variable representing coupling
to a heat bath. To the authors’ surprise, even in the simple case
of a harmonic oscillator, this system can generate chaotic trajectories.
An extended analysis of stability and chaos was published the following year
by Hoover, Posch, and Vesely (1986), who studied the system’s evolution
in the three-dimensional space (<i>x, y, z</i>).
The original system of equations (1986, p. 4256, Eq. 14) is given by:
</p>

<!-- b) Original system of equations -->
<p class="mathline">\(\dot{q} = p,\quad \dot{p} = -\,q - \xi\,p,\quad \dot{\xi} = \alpha\,(p^{2} - 1).\)</p>

<!-- c) Parameters and interpretation -->
<p>
In this system, <i>q</i> denotes the oscillator’s position coordinate,
<i>p</i> its momentum, and <i>ξ</i> acts as a friction coefficient
maintaining the system’s constant temperature.  
The coupling parameter <i>α</i> controls the intensity of the Nosé–Hoover thermostat:
for small values, the system behaves regularly,
while for <i>α ≈ 1.5</i>, chaotic motion appears.
The Nosé–Hoover attractor is thus an example where deterministic
energy-stabilizing feedback leads to global instability of the system.
</p>

<!-- d) Sources -->
<p><b>Sources:</b></p>

<p class="hanging-indent">
Nosé, S. (1984). <i>A unified formulation of the constant temperature molecular dynamics methods.</i>
<i>The Journal of Chemical Physics</i>, 81(1), 511–519.  
DOI: <a href="https://doi.org/10.1063/1.447334" target="_blank">10.1063/1.447334</a>
</p>

<p class="hanging-indent">
Hoover, W. G. (1985). <i>Canonical dynamics: Equilibrium phase-space distributions.</i>
<i>Physical Review A</i>, 31(3), 1695–1697.  
DOI: <a href="https://doi.org/10.1103/PhysRevA.31.1695" target="_blank">10.1103/PhysRevA.31.1695</a>
</p>

<p class="hanging-indent">
Posch, H. A., Hoover, W. G., & Vesely, F. J. (1986).
<i>Canonical dynamics of the Nosé oscillator: Stability, chaos, and heat flow.</i>
<i>Physical Review A</i>, 33(6), 4253–4265.  
DOI: <a href="https://doi.org/10.1103/PhysRevA.33.4253" target="_blank">10.1103/PhysRevA.33.4253</a>
</p>
