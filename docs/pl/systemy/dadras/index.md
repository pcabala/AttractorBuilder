---
layout: systems
title: "Atraktor Dadras"
video: "/assets/media/attractors/dadras.webm"
video_mp4: "/assets/media/attractors/dadras.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/dadras/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = y - a * x + b * y * z
ẏ = c * y - x * z + z
ż = d * x * y - h * z
<b>Parametry:</b>
| a = 3 | b = 2.7 | c = 1.7 | d = 2 | h = 9 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Metoda: DP5
Tolerancja: 0.0001
Krok min: 0.000001
Krok max: 0.1
Liczba kroków: 10000
Faza rozgrzewki (burn-in): 2000
Skala: 0.2
</pre>

<!-- a) Context and historical background -->
<p>
<b>Atraktor Dadrasa</b> został wprowadzony przez Sarę Dadras i Hamida Rezę Momeniego w 2009 roku
jako nowy trójwymiarowy autonomiczny układ chaotyczny, zdolny do generowania atraktorów
z <i>dwoma</i>, <i>trzema</i> oraz <i>czterema</i> zwojami poprzez zmianę jednego parametru.
Układ posiada pięć rzeczywistych punktów równowagi i wykazuje bogatą dynamikę nieliniową,
obejmującą m.in. podwojenia okresu i dodatnie wykładniki Lapunowa.
Jest układem dysypatywnym, gdy spełniony jest warunek <i>c − (h + a) &lt; 0</i>.
Oryginalny układ zaproponowany przez Dadras i Momeniego (2009, s. 3638) ma postać:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x} = y - a x + b y z\)</p>
<p class="mathline">\(\dot{y} = c y - x z + z\)</p>
<p class="mathline">\(\dot{z} = d x y - h z\)</p>

<!-- c) Parameters and interpretation -->
<p>
W tym modelu parametr <i>a</i> wprowadza liniowe tłumienie w składniku <i>x</i>,
natomiast <i>b</i> reguluje nieliniowy składnik \(y z\), który odpowiada za zawijanie trajektorii.
Parametr <i>c</i> kontroluje liniowy wzrost w równaniu <i>y</i> (z dodatkowym napędem +<i>z</i>),
<i>d</i> odpowiada za sprzężenie \(x y\) w równaniu <i>z</i>, a <i>h</i> ustala liniowe tłumienie w <i>z</i>.
Dla klasycznego zestawu parametrów (<i>a</i>=3, <i>b</i>=2.7, <i>c</i>=4.7, <i>d</i>=2, <i>h</i>=9)
układ generuje dwuzwojowy atraktor chaotyczny.
Zmiana jedynie parametru <i>c</i> pozwala uzyskać atraktor trójzwojowy (np. <i>c</i>=1.7)
lub czterozwojowy (np. <i>c</i>=3.9), co pokazuje, jak niewielkie zmiany parametrów
mogą prowadzić do zasadniczej reorganizacji topologii atraktora.
</p>

<!-- d) Source -->
<p>
<b>Źródło:</b> Dadras, S. &amp; Momeni, H. R. (2009).
<i>A novel three-dimensional autonomous chaotic system generating two, three and four-scroll attractors.</i>
Physics Letters A, 373(40), 3637–3642.
<br>
DOI:
<a href="https://doi.org/10.1016/j.physleta.2009.07.088" target="_blank">
10.1016/j.physleta.2009.07.088
</a>
</p>
