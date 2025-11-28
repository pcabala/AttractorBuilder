---
layout: systems
title: "Atraktor Shimizu–Morioka"
video_mp4: "/assets/media/attractors/shimizu-morioka.mp4"
stop_at: 11
lang: pl
alt_url: /en/systems/shimizu-morioka/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania (wersja implementacyjna):</b>
ẋ = y
ẏ = (1 - z) * x - a * y
ż = x**2 - b * z
<b>Parametry:</b>
| a = 0.7 | b = 0.1 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.1, y₀ = 0.0, z₀ = 0.2
Metoda: RK4
Time Step (dt): 0.01
Steps: 50000
Burn-in: 500
Skala: 1.5
</pre>

<p>
<b>Atraktor Shimizu–Morioka</b> należy do klasy trójwymiarowych układów
równani nieliniowych, które zachowują kluczowe cechy dynamiki modelu Lorenza,
ale mają prostszą postać analityczną. Jego geneza wiąże się z pracami
T. Shimizu i N. Morioki nad uproszczonym modelem bifurkacji cyklu granicznego
w pobliżu przejścia do złożonych zachowań okresowych i chaotycznych.
W artykule z 1980 roku autorzy analizują dwuwymiarowy „prosty model”
pokazujący przejście od cyklu symetrycznego do pary cykli asymetrycznych,
z dynamiką bardzo podobną do tej znanej z równania Lorenza.
W dalszych badaniach A. L. Shilnikov wprowadził trójwymiarowy układ,
który obecnie powszechnie określa się mianem <i>modelu Shimizu–Morioka</i>,
wykorzystując go jako normalną postać do badania bifurkacji atraktora Lorenza.
Układ ma postać (1993, s. 338, rów. 1):
</p>

<p class="mathline">\( \dot{x} = y \)</p>
<p class="mathline">\( \dot{y} = x - \lambda y - xz \)</p>
<p class="mathline">\( \dot{z} = -\alpha z + x^{2} \)</p>

<p>
Parametry \(\lambda > 0\) i \(\alpha > 0\) pełnią rolę współczynników tłumienia:
\(\lambda\) odpowiada za dyssypację w równaniu dla \(y\),
natomiast \(\alpha\) kontroluje relaksację zmiennej \(z\).
Dla odpowiednich wartości, takich jak \(\lambda \approx 0.7\) i \(\alpha \approx 0.1\),
układ generuje złożony, niestacjonarny ruch w trójwymiarowej przestrzeni fazowej,
w którym trajektorie wielokrotnie zawijają się wokół dwóch wyróżnionych „płatów”
i nigdy się nie zamykają, tworząc dziwny atraktor o strukturze przypominającej
geometrię atraktora Lorenza.
</p>


<p><b>Źródła:</b></p>
<p class="hanging-indent">
Shimizu, T., &amp; Morioka, N. (1980). On the bifurcation of a symmetric limit cycle
to an asymmetric one in a simple model. <i>Physics Letters A, 76(3–4), 201–204.</i>
DOI: <a href="https://doi.org/10.1016/0375-9601(80)90466-1" target="_blank">
https://doi.org/10.1016/0375-9601(80)90466-1</a>
</p>
<p class="hanging-indent">
Shil'nikov, A. L. (1993). On bifurcations of the Lorenz attractor
in the Shimizu–Morioka model. <i>Physica D: Nonlinear Phenomena, 62(1–4), 338–346.</i>
DOI: <a href="https://doi.org/10.1016/0167-2789(93)90292-9" target="_blank">
https://doi.org/10.1016/0167-2789(93)90292-9</a>
</p>
