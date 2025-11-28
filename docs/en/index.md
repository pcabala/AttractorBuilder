---
layout: home
lang: en
permalink: /en/
title:
---

<div style="
    background: #f7f7f7;
    border: 1px solid #e0e0e0;
    border-radius: 21px;
    padding: 1.2rem 1.4rem;
    margin: 1rem auto;
">
  <p style="font-style: italic; margin: 0;">
    This website is intended for anyone interested in exploring and understanding
    the behavior of nonlinear dynamical systems. It is designed both for researchers
    conducting numerical experiments and for artists and designers who use attractors
    in animation, generative art, or other creative projects. The 
    <a href="{{ '/en/systems/' | relative_url }}"><b>Systems</b></a> section presents twenty well-known nonlinear
    differential equation models that generate characteristic <i>strange attractor</i> structures.
    Each page includes a short visualization of the trajectory as well as references
    to the original publications where the system was first introduced. The
    <a href="{{ '/en/methods/' | relative_url }}"><b>Methods</b></a> section describes the numerical algorithms
    used for integrating these systems. Finally, the 
    <a href="{{ '/en/addon/' | relative_url }}"><b>Add-on</b></a> page introduces the Blender extension
    that enables generating, visualizing, and animating trajectories in 3D space.
    Installing the add-on allows you to perform your own experiments, modify system
    parameters, test custom models, and create three-dimensional forms based on
    chaotic dynamics.
  </p>
</div>



**What is an attractor?**
An attractor is a key concept in the science of dynamical systems. 
It describes a set of states toward which a system evolves over time. 
One can imagine it as a “magnet” in the space of possible behaviors, 
pulling trajectories of the system regardless of their initial positions. 
It is not a state of rest but rather a form of dynamic equilibrium: 
the motion remains confined within a certain region, yet its path never exactly repeats. 
This interplay of regularity and unpredictability gives attractors their unique character.

**From simple equations to complex behavior.**
Every dynamical system is governed by mathematical rules—most often 
by systems of differential equations. These equations, although simple in form, 
can generate behaviors of astonishing complexity. Even though each subsequent state 
of the system is precisely determined by the previous one, the overall evolution may 
appear chaotic. This tension between the deterministic simplicity of rules and the 
unpredictable complexity of outcomes lies at the very foundation of chaos theory.

**Trajectories and phase space.**
To understand how an attractor works, we visualize the system’s motion as a trajectory 
in so-called phase space. This is an abstract space in which each axis represents 
one variable describing the system’s state. When we observe the evolution of the system 
from different starting points, we notice that over time the trajectories begin to cluster 
around a certain subset of this space. That subset, which represents the geometric essence 
of the system’s dynamics, is what we call the attractor.

**Types of attractors: from points to fractals.**
Attractors can take many forms — from single points (equilibrium states) and closed curves 
(limit cycles) to complex, fractal-like structures. The most intricate among them, 
known as strange attractors, are the hallmark of deterministic chaos. They are characterized 
by extreme sensitivity to initial conditions: even the slightest change at the start leads to 
a completely different trajectory later on—a phenomenon famously known as the butterfly effect. 
Detailed mathematical descriptions and examples can be found in the Systems section.

**Hidden order in chaos.**
The study of attractors reveals that chaos is not synonymous with randomness but rather 
an expression of hidden order. Patterns that seem accidental are, in fact, the result 
of deterministic laws whose complexity prevents exact long-term prediction. 
It is at this boundary — between what is predictable and what is not — that the beauty 
and depth of dynamical systems emerge.

<p>
<b>Literature.</b> A good starting point for studying chaos theory
and strange attractors is the following selection of books:
</p>

<p class="hanging-indent">
Devaney, R. (2003). <i>An Introduction to Chaotic Dynamical Systems</i>. Westview Press.<br>
Gleick, J. (1987). <i>Chaos: Making a New Science</i>. Penguin Books.<br>
Ott, E. (1993). <i>Chaos in Dynamical Systems</i>. Cambridge University Press.<br>
Sprott, J. C. (2010). <i>Elegant Chaos</i>. World Scientific.<br>
Strogatz, S. H. (2015). <i>Nonlinear Dynamics and Chaos</i>. CRC Press.
</p>