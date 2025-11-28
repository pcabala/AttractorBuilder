---
layout: systems
title: "Atraktor Newtona-Leipnika"
video_mp4: "/assets/media/attractors/newton-leipnik.mp4"
stop_at: 11
lang: pl
alt_url: /en/systems/newton-leipnik/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = -b*x + y + 10*y*z
ẏ = -x - b*y + 5*x*z
ż =  a*z - 5*x*y
<b>Parametry:</b>
| a = 0.175 | b = 0.4 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.349, y₀ = 0, z₀ = -0.18
Metoda: RK4
Time Step (dt): 0.01
Steps: 50000
Burn-in: 0
Skala: 3 
</pre>

<p>
<b>Atraktor Newton-Leipnik</b> został wprowadzony w 1981 roku przez R.B. Leipnika
i T.A. Newtona w pracy poświęconej ruchowi sztywnego ciała ze sprzężeniem
zwrotnym. Autorzy zmodyfikowali klasyczne równania Eulera, dodając liniowy
człon regulacyjny, co doprowadziło do powstania trójwymiarowego,
kwadratowego układu dynamicznego o zaskakująco złożonym zachowaniu.
Oryginalne równania przedstawione w publikacji mają postać (1981, s. 65, równ. 10):
</p>

<p class="mathline">\( \dot{x} = -0.4\,x + y + 10\,y z \)</p>
<p class="mathline">\( \dot{y} = -x - 0.4\,y + 5\,x z \)</p>
<p class="mathline">\( \dot{z} = \alpha z - 5\,x y \)</p>

<p>
Dla parametru \(\alpha = 0.175\) układ tworzy dwa współistniejące dziwne atraktory.
To, który z nich zostanie osiągnięty, zależy tylko od warunków początkowych.
Autorzy pokazali, że wystarczy bardzo mała zmiana trzeciej współrzędnej, by trajektoria
trafiła na inny atraktor: punkt \((0.349,\,0,\,-0.160)\) prowadzi do atraktora górnego (U),
a \((0.349,\,0,\,-0.180)\) – do atraktora dolnego (L).

Oba atraktory mają wyraźnie inną geometrię. U jest szerszy i bardziej nieregularny,
natomiast L jest ciaśniejszy i bardziej uporządkowany. Współistnienie dwóch chaotycznych
struktur w takim układzie jest rzadkie. Granica między ich basenami przyciągania jest bardzo
złożona, co dobrze pokazuje silną wrażliwość systemu na minimalne zmiany punktu startowego.
Kołyszące, zawijasowe trajektorie systemu zostały przez autorów określone mianem „dipsy–doodle”.

</p>

<p><b>Źródło:</b></p>
<p class="hanging-indent">
Leipnik, R. B., & Newton, T. A. (1981). Double strange attractors in rigid body motion with linear feedback control.
<i>Physics Letters A, 86(2), 63–67.</i>
DOI: <a href="https://doi.org/10.1016/0375-9601(81)90165-1" target="_blank">
https://doi.org/10.1016/0375-9601(81)90165-1
</a>
</p>
