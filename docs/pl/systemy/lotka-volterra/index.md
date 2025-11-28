---
layout: systems
title: "Atraktor Lotki–Volterry"
video_mp4: "/assets/media/attractors/lotka-volterra.mp4"
stop_at: 11
lang: pl
alt_url: /en/systems/lotka-volterra/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = x - x*y + c*x**2 - a*z*x**2
ẏ = -y + x*y
ż = -b*z + a*z*x**2
<b>Parametry:</b>
| a = 2.9851 | b = 3.0 | c = 2.1 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.9, y₀ = 0.9, z₀ = 0.5  
Metoda: RK4
Time Step: 0.01 
Steps: 15000
Burn-in: 50   
Scale: 10
</pre>

<!-- a) Kontekst i tło historyczne -->
<p>
Klasyczny <b>model Lotki–Volterry</b> (1925–1926) opisuje cykliczną dynamikę
układu drapieżnik–ofiara w dwóch wymiarach. Trajektorie tego systemu są
zamkniętymi orbitami wokół punktu stacjonarnego, co oznacza stabilne i
okresowe oscylacje populacji. W 1988 roku Nikola Samardzija i
Lawrence D. Greller zaproponowali jego uogólnienie do trzech wymiarów,
rozszerzając klasyczny model o dodatkowy gatunek i nieliniowe sprzężenie
między zmiennymi. W nowej wersji system ten generuje złożone oscylacje,
bifurkacje i przejścia do chaosu. Oryginalny system równań (1988, s. 466) ma postać:
</p>

<!-- b) Oryginalny układ równań -->


<p class="mathline">\(\dot{X} = X - XY + CX^{2} - AZX^{2}\)</p>
<p class="mathline">\(\dot{Y} = -Y + XY\)</p>
<p class="mathline">\(\dot{Z} = -BZ + AZX^{2}\)</p>

<!-- c) Parametry i interpretacja -->
<p>
Parametry <i>A</i>, <i>B</i> i <i>C</i> są dodatnie (<i>A, B, C &gt; 0</i>).
Sterują one siłą interakcji pomiędzy gatunkami:
<i>A</i> odpowiada za sprzężenie nieliniowe pomiędzy drapieżnikami,
<i>B</i> opisuje tempo tłumienia populacji <i>Z</i>,
a <i>C</i> — efekt samowzmacniania populacji <i>X</i>.
Autorzy wykazali, że system ten może prowadzić do powstawania
chaotycznych trajektorii i fraktalnego torusa, stanowiącego przykład
tzw. „eksplozywnej drogi do chaosu”.
</p>

<!-- d) Źródła -->
<p>
<b>Źródła:</b><br>
Lotka, A. J. (1925). <i>Elements of Physical Biology.</i> Williams & Wilkins, Baltimore.<br>
Samardzija, N., & Greller, L. D. (1988). <i>Explosive route to chaos through a fractal torus in a generalized Lotka–Volterra model.</i> <i>Bulletin of Mathematical Biology</i>, 50(5), 465–491. DOI: <a href="https://www.sciencedirect.com/science/article/abs/pii/S009282408880003X" target="_blank">10.1016/S0092-8240(88)80003-X</a><br>
Volterra, V. (1926). <i>Variazioni e fluttuazioni del numero d’individui in specie animali conviventi.</i> <i>Memorie della Reale Accademia Nazionale dei Lincei</i>, 2(6), 31–113.
</p>

