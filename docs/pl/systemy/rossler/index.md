---
layout: systems
title: "Atraktor Rösslera"
video_mp4: "/assets/media/attractors/rossler.mp4"
stop_at: 11
lang: pl
alt_url: /en/systems/rossler/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = - (y + z)
ẏ = x + a*y
ż = b + z*(x - c)
<b>Parametry:</b>
| a = 0.2 | b = 0.2 | c = 5.7 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.01, y₀ = 0, z₀ = 0  
Metoda: RK4  
Krok czasowy (dt): 0.05  
Liczba kroków: 15000  
Faza rozgrzewki (burn-in): 1000  
Skala: 0.2
</pre>

<!-- a) Kontekst i tło historyczne -->
<p>
<b>Atraktor Rösslera</b> został wprowadzony w 1976 roku przez <i>Otto E. Rösslera</i>
z Instytutu Chemii Fizycznej i Teoretycznej Uniwersytetu w Tybindze (Niemcy).
Model ten powstał jako uproszczony odpowiednik układu Lorenza, mający uchwycić
istotę deterministycznego, nieokresowego przepływu — tzw. chaosu ciągłego —
z użyciem tylko jednej nieliniowości drugiego rzędu.  
Celem Rösslera było zaprojektowanie możliwie najprostszego ciągłego układu
różniczkowego, który generuje dziwny atraktor, zachowując jedynie jeden człon nieliniowy.  
Oryginalny układ równań ma postać:
(1976, s.&nbsp;397, równanie&nbsp;2):
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x}=-(y+z),\quad \dot{y}=x+0.2\,y,\quad \dot{z}=0.2+z\,(x-5.7).\)</p>

<p>
Zawiera on tylko jeden nieliniowy człon \(z\,x\), co czyni go jednym z najprostszych
ciągłych układów dynamicznych wykazujących zachowanie chaotyczne.  
Model został pomyślany jako „model modelu” — minimalny odpowiednik układu Lorenza,
zachowujący charakterystyczny mechanizm rozciągania i zawijania trajektorii,
odpowiedzialny za powstawanie chaosu deterministycznego.
</p>

<!-- d) Źródła -->
<p><b>Źródło:</b></p>

<p class="hanging-indent">
Rössler, O. E. (1976).  
<i>An equation for continuous chaos.</i>  
<i>Physics Letters A</i>, 57(5), 397–398.  
DOI: <a href="https://doi.org/10.1016/0375-9601(76)90101-8" target="_blank">
10.1016/0375-9601(76)90101-8
</a>
</p>
