---
layout: systems
title: "Atraktor Li"
video: "/assets/media/attractors/li.webm"
video_mp4: "/assets/media/attractors/li.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/li/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = a * (y - x) + d * x * z
ẏ = k * x + f * y - x * z
ż = -e * x**2 + x * y + c * z
<b>Parametry:</b>
| a = 40 | c = 11/6 | d = 0.16 | e = 0.65 | f = 20 | k = 55 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.01, y₀ = 0, z₀ = 0
Metoda: DP5
Tolerancja: 0.000001
Stem (min): 0
Step (max): 0.01
Krok czasowy (dt): 0.01
Liczba kroków: 7000
Faza rozgrzewki (burn-in): 1000
Skala: 0.01
</pre>

<!-- a) Context and historical background -->
<p>
<b>Atraktor Li</b> został zaproponowany przez Dequana Li w 2008 roku
jako nowy układ chaotyczny oparty na strukturze typu Lorenz,
rozszerzony o dodatkowe sprzężenia kwadratowe.
Na drodze prób i błędów numerycznych autor wykazał, że
gładki trójwymiarowy układ autonomiczny zawierający jedynie
cztery nieliniowe człony kwadratowe może generować
<i>trójzwojowy atraktor chaotyczny</i>.
W przeciwieństwie do układów Lorenza i Chena, które tworzą dwa symetryczne „skrzydła”,
układ Li posiada dodatkowy, trzeci zwojowy obszar położony ukośnie
pomiędzy klasycznymi dwiema strukturami.
Oryginalny system zaproponowany przez Li (2008, s. 389) ma postać:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x}(t) = a(y(t) - x(t)) + d\,x(t)\,z(t)\)</p>
<p class="mathline">\(\dot{y}(t) = k\,x(t) + f\,y(t) - x(t)\,z(t)\)</p>
<p class="mathline">\(\dot{z}(t) = -e\,x^{2}(t) + x(t)\,y(t) + c\,z(t)\)</p>

<!-- c) Parameters and interpretation -->
<p>
W tym układzie parametr <i>a</i> kontroluje liniowe sprzężenie pomiędzy <i>x</i> i <i>y</i>,
natomiast <i>d</i> wprowadza nieliniowy składnik \(x z\), który zakrzywia trajektorie
w przestrzeni fazowej.
Parametry <i>k</i> i <i>f</i> odpowiadają za liniowe wzmocnienie i tłumienie w równaniu <i>y</i>,
<i>e</i> kształtuje paraboliczny człon \(-e x^{2}\),
a <i>c</i> określa stopień pionowego ściągania trajektorii wzdłuż osi <i>z</i>.
Dla zestawu parametrów (<i>a</i>=40, <i>k</i>=55, <i>c</i>=11/6, <i>d</i>=0.16, <i>e</i>=0.65, <i>f</i>=20)
układ generuje trójzwojowy atraktor chaotyczny.
Odpowiadające mu wykładniki Lapunowa
(<i>L₁</i>=0.2315, <i>L₂</i>=0, <i>L₃</i>=−1.987)
potwierdzają dysypatywny charakter chaosu z wymiarem fraktalnym około 2.12.
</p>

<!-- d) Source -->
<p>
<b>Źródło:</b> Li, D. (2008).
<i>A three-scroll chaotic attractor.</i>
Physics Letters A, 372 (3–4), 387–393.  
<br>
DOI:
<a href="https://doi.org/10.1016/j.physleta.2007.07.045" target="_blank">
10.1016/j.physleta.2007.07.045
</a>
</p>
