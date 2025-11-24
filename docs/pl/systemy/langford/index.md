---
layout: systems
title: "Atraktor Langforda"
video: "/assets/media/attractors/langford.webm"
video_mp4: "/assets/media/attractors/langford.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/langford/
---

<pre class="eq-plain">
Attractor Builder (Blender add-on)
<b>Równania:</b>
ẋ = (z - b) * x - d * y
ẏ = d * x + (z - b) * y
ż = c + a * z - (z**3)/3 - (x**2 + y**2) * (1 + e * z)
<b>Parametry:</b>
| a = 0.95 | b = 0.7 | c = 0.6 | d = 3.5 | e = 0.25 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.1, y₀ = 0.0, z₀ = 0.0
Metoda: RK4
Krok czasu (dt): 0.015
Liczba kroków: 15000
Faza rozgrzewki (burn-in): 300
Skala: 0.1
</pre>

<!-- a) Kontekst i tło historyczne -->
<p>
<b>Atraktor Langforda</b> to model matematyczny układu chaotycznego wprowadzony przez
kanadyjskiego matematyka Williama F. Langforda w 1984 roku podczas numerycznych badań
nad interakcją między bifurkacjami typu <i>Hopfa</i> i <i>histerezy</i>.
Był to jeden z pierwszych gładkich, trójwymiarowych układów, które pokazały,
że sprzężenie tych bifurkacji może prowadzić do zjawiska <i>zaniku torusa</i>
(<i>torus breakdown</i>) i pojawienia się chaosu.  
Choć czasem jest mylony z atraktorem Aizawy,
to właśnie praca Langforda jako pierwsza dostarczyła formalnego opisu
tego typu dynamiki prowadzącej do zaniku torusa,
podczas gdy Aizawa wprowadził później uproszczoną wersję tego układu.
Oryginalny system zaproponowany przez Langforda (1984, s. 287) ma postać równań:
</p>

<!-- b) Układ równań -->
<p class="mathline">\(\dot{x} = (z - \beta)x - \omega y\)</p>
<p class="mathline">\(\dot{y} = \omega x + (z - \beta)y\)</p>
<p class="mathline">\(\dot{z} = \mu + \alpha z - \tfrac{1}{3}z^{3} - (x^{2} + y^{2})(\ell + p z) + \varepsilon z x^{3}\)</p>

<!-- c) Parametry i interpretacja -->
<p>
W tym ujęciu parametry <i>μ</i>, <i>α</i> i <i>β</i> określają lokalne tempo wzrostu
i stabilność stanów stacjonarnych.
Para <i>ℓ</i> i <i>p</i> wyznacza moment pojawienia się oraz geometrię
bifurkacji Naimarka–Sackera (bifurkacji wtórnej Hopfa, czyli <i>torus bifurcation</i>),
natomiast częstotliwość <i>ω</i> kontroluje ruch obrotowy w płaszczyźnie <i>x–y</i>.
Parametr <i>ε</i> wprowadza <i>nieosiowo-symetryczne</i> zaburzenia,
które niszczą gładki torus i inicjują kaskadę bifurkacji —
synchronizację fazową, podwajanie okresu, a ostatecznie
powstanidynamiki chaotycznej.
Wraz ze wzrostem <i>ε</i> atraktor ewoluuje od gładkiego torusa,
przez fraktalny „gruby torus”, aż do zanikającego (przejściowego) chaosu.
</p>

<!-- d) Źródło -->
<p>
<b>Źródło:</b> Langford, W. F. (1984).
<i>Numerical Studies of Torus Bifurcations.</i>
W: <i>Nonlinear Oscillations in Biology and Chemistry</i>,
seria <i>International Series of Numerical Mathematics</i>, t. 70,
Birkhäuser Verlag, Basel, s. 285–295.
<br>
DOI:
<a href="https://doi.org/10.1007/978-3-0348-6256-1_19" target="_blank">
10.1007/978-3-0348-6256-1_19
</a>
</p>
