---
layout: systems
title: "Atraktor Lorenza"
video_mp4: "/assets/media/attractors/lorenz.mp4"
stop_at: 11
lang: pl
alt_url: /en/systems/lorenz/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = a * (y - x)
ẏ = x * (b - z) - y
ż = x * y - c * z
<b>Parametry:</b>
| a = 10 | b = 28 | c = 8/3 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Metoda: RK4
Krok czasowy (dt): 0.01
Liczba kroków: 15000
Faza rozgrzewki (burn-in): 500
Skala: 0.1
</pre>

<!-- a) Context and historical background -->
<p>
<b>Atraktor Lorenza</b> wywodzi się z uproszczonego modelu konwekcji atmosferycznej,
opracowanego przez Edwarda N. Lorenza w 1963 roku w Massachusetts Institute of Technology.
Podczas badań nad zredukowanym układem równań opisujących ruch płynu cieplnego Lorenz odkrył,
że deterministyczne równania mogą prowadzić do pozornie nieregularnych, niepowtarzalnych trajektorii.
Odkrycie to podważyło dominujące wówczas przekonanie o przewidywalności układów deterministycznych
i zapoczątkowało rozwój współczesnej teorii chaosu.
Układ ten stał się jednym z najbardziej rozpoznawalnych przykładów <i>dziwnego atraktora</i>
oraz paradygmatem wrażliwości na warunki początkowe — tzw.
„efektu motyla".
Oryginalny układ równań przedstawiony przez Lorenza (1963, s. 135) ma postać:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{X} = -\sigma X + \sigma Y\)</p>
<p class="mathline">\(\dot{Y} = -XZ + rX - Y\)</p>
<p class="mathline">\(\dot{Z} = XY - bZ\)</p>

<!-- c) Parameters and interpretation -->
<p>
W tej notacji <i>σ</i> oznacza liczbę Prandtla, wyrażającą stosunek
między dyfuzyjnością pędu a dyfuzyjnością cieplną, natomiast <i>r</i> jest parametrem sterującym,
analogicznym do zredukowanej liczby Rayleigha, która określa gradient temperatury
napędzający konwekcję. Współczynnik <i>b</i> określa geometryczny stosunek wymiarów
i pionową kompresję przepływu konwekcyjnego.  
W notacji dodatku Blendera parametry te odpowiadają symbolom
<i>a = σ</i>, <i>b = r</i> oraz <i>c = b</i>.  
Dla klasycznego zestawu parametrów (<i>a</i>=10, <i>b</i>=28, <i>c</i>=8/3)
układ generuje oscylacje aperiodyczne, lecz ograniczone, tworząc
charakterystyczną dwuskrzydłową strukturę atraktora Lorenza.
Nawet minimalne różnice w warunkach początkowych prowadzą do wykładniczego rozbiegania trajektorii,
co ilustruje istotę deterministycznego chaosu.
</p>

<!-- d) Sources -->
<p><b>Źródło:</b></p>

<p class="hanging-indent">
Lorenz, E. N. (1963).
<i>Deterministic Nonperiodic Flow.</i>
Journal of the Atmospheric Sciences, 20(2), 130–141.
DOI: 
<a href="https://doi.org/10.1175/1520-0469(1963)020&lt;0130:DNF&gt;2.0.CO;2" target="_blank">
10.1175/1520-0469(1963)020&lt;0130:DNF&gt;2.0.CO;2
</a>
</p>
