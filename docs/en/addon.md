---
layout: addon
lang: en
permalink: /en/addon/
title:
alt_url: /pl/addon/
---


<em>The **Attractor Builder** add-on was designed as a tool for numerical integration
of differential equation systems and generating their trajectories directly inside
**Blender 4.5+**. It allows users to run custom experiments, visualize attractors,
export numerical data, and create fully animated 3D forms.
The add-on is free and intended both for researchers working with dynamical systems
and for artists who use attractors in graphics, animation, or generative art.</em>

<p style="text-align:center; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/intro.png' | relative_url }}"
       alt="Attractor Builder — panel location"
       style="width:100%; max-width:100%; border-radius: 10px;
              box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
</p>


---


<p>
<b>Installation</b><br>

<b>Recommended (Blender Extensions)</b><br>
1. Open Blender and go to: <i>Edit → Preferences → Extensions</i>.<br>
2. Search for <b>Attractor Builder</b> and click <i>Install</i>.<br>
3. Enable the extension after installation.<br><br>

<b>Manual installation (from GitHub)</b><br>
1. Download the
   <a href="https://github.com/pcabala/AttractorBuilder/releases/latest/download/attractor_builder.zip"
      style="display:inline-flex;">
      attractor_builder.zip
   </a>
   file from the GitHub repository.<br>
2. In Blender, open: <i>Edit → Preferences → Extensions</i>.<br>
3. Click <i>Install from Disk…</i> and select the downloaded <code>.zip</code> file.<br>
4. Enable the extension after installation.<br><br>

The add-on panel will appear in the N-panel → <b>Attractor</b>.<br>
</p>

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/n_panel.png' | relative_url }}"
       alt="N-panel with Attractor Builder"
       style="display:block; border-radius: 10px; width:auto; max-width:100%; height:auto;">
</p>

---

<p><b>Interface</b><br>

The <em>Default</em> tab provides access to the built-in library of systems
(Lorenz, Chen, Lü, etc.) with predefined initial parameters.
The <em>Custom</em> tab allows you to define your own equations and parameters.


<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/mode_default.png' | relative_url }}"
       alt="Attractor Builder – Default interface"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>



<p><b>Default Library.</b>
A dropdown menu containing predefined attractor systems.
After selecting a system, the corresponding equations and default parameters appear below.
<em>Equations</em>: the system’s differential equations presented as three expressions
representing the derivatives <em>ẋ</em>, <em>ẏ</em>, and <em>ż</em>.  
To ensure safety and consistency with the <em>Custom</em> mode,
only the variables <code>x</code>, <code>y</code>, <code>z</code> are allowed, as well as
the mathematical functions: <code>sin</code>, <code>cos</code>, <code>tan</code>,
<code>asin</code>, <code>acos</code>, <code>atan</code>, <code>sinh</code>, <code>cosh</code>,
<code>tanh</code>, <code>exp</code>, <code>log</code>, <code>sqrt</code>, <code>pow</code>, <code>fabs</code>.  
Standard arithmetic and unary operators are supported
(<code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>**</code>, <code>%</code>,
and unary <code>-</code> and <code>+</code>).  
<em>Parameters</em>: a list of system parameters (e.g., <em>a</em>, <em>b</em>, <em>c</em> for the Lorenz system),
which can be modified to influence the resulting trajectory.
The <em>Tips</em> button provides short hints, and <em>Copy</em> transfers the equations and current parameters
into the <em>Custom</em> mode for further editing.</p>

<p><b>Simulation Settings.</b>
A group of simulation settings: initial state, integration method, and related parameters.
<em>Initial conditions:</em>
The starting coordinates <em>x₀</em>, <em>y₀</em>, <em>z₀</em>,
from which numerical integration begins.

<em>Integration Method.</em>
A dropdown menu for selecting the numerical method (Euler, Heun, RK4, RKF45, DP5): 

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/integration_methods.png' | relative_url }}"
       alt="Attractor Builder – Integration methods"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>


<p><b>Fixed dt.</b> For fixed-step methods (Euler, Heun, RK4), the available settings are:
the time step <em>Time Step (dt)</em>,
the number of integration steps <em>Steps</em>,
the warm-up phase <em>Burn-in</em>,
and the scaling factor <em>Scale</em>.</p> 

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/fixed_dt.png' | relative_url }}"
       alt="Attractor Builder – Fixed dt"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>

 

<p><b>Adaptive dt.</b> Includes two adaptive methods (RKF45 and DP5)
in which the user does not specify a fixed time step.
Instead, the algorithm adjusts <em>dt</em> automatically based on the error tolerance
<em>Tolerance</em> and the allowed range <em>Min Step</em> and <em>Max Step</em>.</p>

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/adaptive_dt.png' | relative_url }}"
       alt="Attractor Builder – Adaptive dt"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>

<p><b>Output.</b>
The <em>Build Attractor</em> button generates a trajectory as a 
<em>Curve</em> object (specifically a <em>Poly Curve</em>)
named according to the <em>Output Name</em> field — default: <code>Attractor</code>.
Only after building the attractor does the <em>Raw data</em> section become available. 
The <em>Points</em> button creates a <em>Mesh</em> object named <code>RawPoints</code>,
allowing preview of all generated points.
The <em>Export</em> button saves the data to a CSV file for further analysis in Python,
MATLAB, or Excel.  
The CSV file contains the columns 
<code>steps</code>, <code>dt</code>, <code>x</code>, <code>y</code>, <code>z</code>.  
Row <code>0</code> corresponds to the initial conditions provided
in the <em>Initial conditions</em> section. Subsequent rows contain the points of the trajectory
obtained at consecutive integration steps.  
The <code>dt</code> column is especially important for adaptive methods where
the time step is computed dynamically.</p>


<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/output.png' | relative_url }}"
       alt="Attractor Builder – Output section"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>


<p><b>Post-Processing Tools.</b> 
This section becomes available after the attractor is generated and allows simple
post-processing of the resulting curve.  
The <em>Trim</em> tool shortens the trajectory by removing its beginning or end,
using the <em>Start</em> and <em>End</em> sliders; clicking <em>Apply Trim</em> updates the curve permanently.
The <em>Simplify</em> tool reduces the number of points of the <em>Poly Curve</em>,
making the object lighter and easier to edit; this operation is independent of trimming.
The <em>Smooth to Bezier</em> tool converts the polyline into a Bézier curve using a built-in
smoothing algorithm, whose intensity is controlled by the <em>Fidelity</em> parameter.
All three tools help prepare the trajectory for further editing, animation, or rendering.</p>

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/post_processing.png' | relative_url }}"
       alt="Attractor Builder – Post processing tools"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>


<p><b>Custom.</b> 
This mode allows defining and saving custom systems of differential equations,
which can then be integrated and visualized just like the systems from the built-in library.
It is designed for users who want to experiment with their own models,
modify existing systems, or document different parameter variants.</p>

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/mode_custom.png' | relative_url }}"
       alt="Attractor Builder – Custom mode"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>

<p><b>Custom Library.</b> 
A dropdown list showing previously saved systems together with their parameters.
Entries appear in reverse chronological order, making it easy to return to recently edited models.  
When entering your own equations, remember that the parser accepts only a safe subset of expressions:
variables <code>x</code>, <code>y</code>, <code>z</code>;
the mathematical functions 
<code>sin</code>, <code>cos</code>, <code>tan</code>, <code>asin</code>, <code>acos</code>, <code>atan</code>,
<code>sinh</code>, <code>cosh</code>, <code>tanh</code>, <code>exp</code>, <code>log</code>, <code>sqrt</code>,
<code>pow</code>, <code>fabs</code>;
and the standard arithmetic operators 
<code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>**</code>, <code>%</code>,
as well as unary <code>+</code> and <code>-</code>.  
Any other syntax will be rejected.</p>

<p>
<b>Detect Parameters.</b>  
This button analyses the entered equations, detects all symbols
(excluding <code>x</code>, <code>y</code>, <code>z</code>), and generates the corresponding parameter list.
This step is mandatory — without parameter detection and correct equation structure,
the simulation cannot be started.  
After successful detection, parameters appear in the table below, where they can be assigned
values just like in the <em>Default</em> mode.</p>


<p><b>Save/Notes/Edit/Delete.</b>  
Once parameters are detected, the system can be saved under any name, adding it to the 
<em>Custom Library</em>. All saved systems are stored in a single <code>.json</code> file inside the add-on,
so they remain available across Blender sessions.  
Users may attach notes to each saved system, such as origin descriptions,
stability observations, typical parameter values, or numerical experiment results.
The <em>Note</em> and <em>Edit</em> buttons allow viewing and editing notes,
while <em>Delete</em> removes the system together with its notes from the JSON file.</p>
