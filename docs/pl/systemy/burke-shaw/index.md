---
layout: systems
title: "Atraktor Burke’a–Shawa"
video_mp4: "/assets/media/attractors/burke-shaw.mp4"
stop_at: 11
lang: pl
alt_url: /en/systems/burke-shaw/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = -a * (x + y)
ẏ = -y - a * x * z
ż = a * x * y + b
<b>Parametry:</b>
| a = 10 | b = 13 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.1, y₀ = 0.0, z₀ = 0.0  
Metoda: RK4  
Krok czasowy (dt): 0.01  
Liczba kroków: 15000  
Faza rozgrzewki (burn-in): 500  
Skala: 0.3
</pre>

<!-- a) Context and historical background -->
<p>
<b>Atraktor Burke’a–Shawa</b> został zaproponowany przez Roberta Shawa w 1981 roku
podczas badań nad nieliniowymi przepływami chaotycznymi prowadzonych wspólnie
z fizykiem Billem Burke’iem.
Był to przykład tzw. nieograniczonego atraktora osobliwego
(<i>unbounded strange attractor</i>),
czyli układu, który nie posiada punktów stałych
i którego trajektorie mogą rozciągać się nieskończenie wzdłuż jednej osi.
Oryginalny system równań (1981, s. 104) ma postać:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x} = -10x - 10y\)</p>
<p class="mathline">\(\dot{y} = -10xz - y,\) \(\quad V = 13\)</p>
<p class="mathline">\(\dot{z} = 10xy + V\)</p>

<!-- c) Parameters and interpretation -->
<p>
W tym układzie współczynnik <i>a</i> określa siłę sprzężenia nieliniowego
między zmiennymi <i>x</i> i <i>y</i>, natomiast parametr <i>b</i>
pełni rolę stałego przesunięcia w równaniu dla <i>z</i>,
które powoduje powolne przesuwanie trajektorii wzdłuż osi <i>z</i>.
Mimo że układ nie jest ograniczony,
jego rozwiązania tworzą lokalnie uporządkowaną strukturę o cechach chaosu,
zwaną atraktorem Burke’a–Shawa.
</p>

<!-- d) Source -->
<p>
<b>Źródło:</b> Shaw, R. (1981).
<i>Strange Attractors, Chaotic Behavior and Information Flow.</i>
<i>Zeitschrift für Naturforschung A</i>, 36(1), 80–112.  
<br>
Dostęp online:
<a href="https://www.degruyterbrill.com/document/doi/10.1515/zna-1981-0115/html?lang=en" target="_blank">
https://www.degruyterbrill.com/document/doi/10.1515/zna-1981-0115/html?lang=en
</a>
</p>

