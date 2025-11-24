---
layout: systems
title: "Atraktor Rikitakego"
video: "/assets/media/attractors/rikitake.webm"
video_mp4: "/assets/media/attractors/rikitake.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/rikitake/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = -b * x + z * y
ẏ = -b * y + (z - a) * x
ż = 1 - x * y
<b>Parametry:</b>
| a = 5 | b = 2 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 1, y₀ = 1, z₀ = 1   
Metoda: RK4  
Krok czasowy (dt): 0.01  
Liczba kroków: 15000  
Faza rozgrzewki (burn-in): 500  
Skala: 0.4
</pre>

<!-- a) Context and historical background -->
<p>
<b>Atraktor Rikitakego</b> wywodzi się z klasycznego modelu dwóch sprzężonych
dynamo-tarcz opracowanego przez Tsunejiego Rikitake w 1957 roku
w celu opisu nieregularnych odwróceń pola magnetycznego Ziemi.
Układ ten, znany jako <i>system dwóch dysków dynama</i>,
opisuje wzajemne oddziaływanie dwóch obwodów elektrycznych
sprzężonych przez momenty magnetyczne wirujących przewodników.
W ujęciu oryginalnym Rikitakego (1957, s. 90–91)
równania przyjmują postać:
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
Rikitake zauważył, że dla pewnych wartości parametrów
sprzężone równania dla prądów (<i>I₁, I₂</i>) i prędkości kątowych
(<i>Ω₁, Ω₂</i>) prowadzą do oscylacji nieregularnych — chaotycznych —
mogących modelować zmiany biegunowości pola geomagnetycznego.
Po uproszczeniu i przejściu do postaci bezwymiarowej
otrzymuje się klasyczny trójwymiarowy układ znany dziś
jako atraktor Rikitakego (McMillen, 1999, s. 1):
</p>

<!-- d) Dimensionless system -->
<p class="mathline">\(\dot{x} = -\mu x + y z\)</p>
<p class="mathline">\(\dot{y} = -\mu y + (z - a)x\)</p>
<p class="mathline">\(\dot{z} = 1 - x y\)</p>

<!-- e) Parameters and interpretation -->
<p>
W wersji używanej w dodatku Blendera parametry <i>a</i> i <i>b</i>
odpowiadają odpowiednio współczynnikowi sprzężenia pomiędzy obwodami
oraz tłumieniu (odpowiednikowi <i>μ</i>).
Dla wartości <i>a = 5</i> i <i>b = 2</i> układ generuje
charakterystyczny atraktor o dwóch wirujących płatach,
ilustrujący zjawisko niestabilnych przełączeń magnetycznych —
analogię odwróceń biegunów w polu geomagnetycznym.
</p>

<!-- f) Sources -->
<p>
<b>Źródła:</b><br>
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
