---
layout: systems
title: "Atraktor Nosé–Hoovera"
video: "/assets/media/attractors/nose-hoover.webm"
video_mp4: "/assets/media/attractors/nose-hoover.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/nose-hoover/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = y
ẏ = -x - z*y
ż = a * (y**2 - 1)
<b>Parametry:</b>
| a = 1.5 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 1.0, y₀ = 0.0, z₀ = 0.0  
Metoda: RK4  
Krok czasowy (dt): 0.01  
Liczba kroków: 10000  
Faza rozgrzewki (burn-in): 500  
Skala: 1
</pre>

<!-- a) Kontekst i tło historyczne -->
<p>
<b>Atraktor Nosé–Hoovera</b> powstał jako efekt uboczny
deterministycznej metody kontrolowania temperatury w symulacjach molekularnych.
Mechanizm ten, opracowany przez Shuichiego Nosé (1984) i uproszczony przez
Williama G. Hoovera (1985), służył do utrzymywania stałej temperatury
w układach dynamicznych poprzez dodanie zmiennej reprezentującej sprzężenie
ze zbiornikiem ciepła. Ku zaskoczeniu autorów, nawet w prostym przypadku
oscylatora harmonicznego taki układ może generować trajektorie chaotyczne.
Rozszerzona analiza stabilności i chaosu została opublikowana rok później
przez Hoovera, Poscha i Vesely’ego (1986), gdzie badano ewolucję układu
w przestrzeni trzech zmiennych (<i>x, y, z</i>).
Oryginalny system równań (1986, s. 4256, równ. 14) ma postać:
</p>

<!-- b) Oryginalny układ równań -->
<p class="mathline">\(\dot{q} = p,\quad \dot{p} = -\,q - \xi\,p,\quad \dot{\xi} = \alpha\,(p^{2} - 1).\)</p>

<!-- c) Parametry i interpretacja -->
<p>
W tym układzie <i>q</i> oznacza współrzędną położenia oscylatora, 
<i>p</i> – jego pęd, natomiast <i>ξ</i> pełni rolę współczynnika tarcia 
utrzymującego stałą temperaturę układu.  
Parametr sprzężenia <i>α</i> reguluje intensywność działania termostatu Nosé–Hoovera:
dla małych wartości układ zachowuje się regularnie, 
natomiast przy <i>α ≈ 1.5</i> pojawia się ruch chaotyczny.
Atraktor Nosé–Hoovera jest zatem przykładem, w którym deterministyczne
sprzężenie stabilizujące energię prowadzi do globalnej niestabilności układu.
</p>

<!-- d) Źródła -->
<p><b>Źródła:</b></p>

<p class="hanging-indent">
Nosé, S. (1984). <i>A unified formulation of the constant temperature molecular dynamics methods.</i>
<i>The Journal of Chemical Physics</i>, 81(1), 511–519.  
DOI: <a href="https://doi.org/10.1063/1.447334" target="_blank">10.1063/1.447334</a>
</p>

<p class="hanging-indent">
Hoover, W. G. (1985). <i>Canonical dynamics: Equilibrium phase-space distributions.</i>
<i>Physical Review A</i>, 31(3), 1695–1697.  
DOI: <a href="https://doi.org/10.1103/PhysRevA.31.1695" target="_blank">10.1103/PhysRevA.31.1695</a>
</p>

<p class="hanging-indent">
Posch, H. A., Hoover, W. G., & Vesely, F. J. (1986).
<i>Canonical dynamics of the Nosé oscillator: Stability, chaos, and heat flow.</i>
<i>Physical Review A</i>, 33(6), 4253–4265.  
DOI: <a href="https://doi.org/10.1103/PhysRevA.33.4253" target="_blank">10.1103/PhysRevA.33.4253</a>
</p>
