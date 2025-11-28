---
layout: systems
title: "Atraktor Chena"
video_mp4: "/assets/media/attractors/chen.mp4"
stop_at: 11
lang: pl
alt_url: /en/systems/chen/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = a * (y - x)
ẏ = (c - a) * x - x * z + c * y
ż = x * y - b * z
<b>Parametry:</b>
| a = 35 | b = 3 | c = 28 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0, y₀ = 1, z₀ = 1
Metoda: RK4
Krok czasowy (dt): 0.005
Liczba kroków: 20000
Faza rozgrzewki (burn-in): 1000
Skala: 0.1
</pre>

<!-- a) Context and historical background -->
<p>
<b>Atraktor Chena</b> został wprowadzony w 1999 roku przez Guanronga Chena i Tetsushiego Uetę
jako nowy układ chaotyczny odkryty w trakcie badań nad <i>antykontrolą chaosu</i> —
procesem celowego wprowadzania chaosu do układów, które normalnie zachowują się regularnie.
Choć jego równania są bardzo podobne do układu Lorenza,
układ Chena <i>nie jest topologicznie równoważny</i> ani atraktorowi Lorenza, ani Rösslera.
Odkrycie to stanowiło ważny przykład pokazujący, że nawet niewielkie różnice strukturalne
w równaniach nieliniowych mogą prowadzić do odmiennych typów zachowania chaotycznego.
Oryginalny układ zaproponowany przez Chena i Uetę (1999, s. 1465) ma postać:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x} = a (y - x)\)</p>
<p class="mathline">\(\dot{y} = (c - a)x - xz + cy\)</p>
<p class="mathline">\(\dot{z} = xy - bz\)</p>

<!-- c) Parameters and interpretation -->
<p>
W tym modelu parametr <i>a</i> określa siłę sprzężenia pomiędzy zmiennymi <i>x</i> i <i>y</i>,
parametr <i>b</i> kontroluje tempo tłumienia wzdłuż osi <i>z</i>,
natomiast <i>c</i> wpływa zarówno na liniowe wzmocnienie,
jak i na nieliniowe sprzężenie zwrotne przez wyrażenia <i>y</i> i <i>xz</i>.
Dla klasycznego zestawu parametrów (<i>a</i>=35, <i>b</i>=3, <i>c</i>=28)
układ generuje złożony, dwuzwojowy atraktor chaotyczny,
który wizualnie przypomina atraktor Lorenza, lecz różni się topologią punktów równowagi.
Pomimo podobieństwa kształtu, nie istnieje żadna liniowa ani nieliniowa transformacja współrzędnych,
która mogłaby przekształcić układ Chena w układ Lorenza — co potwierdza ich dynamiczną nierównoważność.
</p>

<!-- d) Source -->
<p>
<b>Źródło:</b> 
<br>
Chen, G. & Ueta, T. (1999).
<i>Yet Another Chaotic Attractor.</i>
International Journal of Bifurcation and Chaos, 9 (7), 1465–1466.
DOI:
<a href="https://doi.org/10.1142/S0218127499001024" target="_blank">
10.1142/S0218127499001024
</a>
</p>
