---
layout: systems
title: "Atraktor Arneodo"
video: "/assets/media/attractors/arneodo.webm"
video_mp4: "/assets/media/attractors/arneodo.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/arneodo/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = a*(x-y)
ẏ = -4*a*y+x*z+m*x**3
ż = -d*a*z+x*y+b*z**2
<b>Parametry:</b>
| a = 1 | b = -0.09 | d = 1.5 | m = 0.01 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 1, y₀ = 0.1, z₀ = 0.1
Metoda: Euler
Time Step (dt): 0.01
Steps: 15000
Burn-in: 1000
Skala: 0.1
</pre>

<p>
<b>Atraktor Arneodo</b> został opisany w 1981 roku przez 
Alaina Arneodo, Paula Coulleta i Christiana Tressera jako przykład nowego mechanizmu
przejścia do turbulencji. Autorzy analizowali trójwymiarowe układy równań
zachowujące symetrię
\( S: (x, y, z) \mapsto (-x, -y, z) \),
dla których charakterystyczna jest pojawiająca się sekwencja stabilnych orbit
homoklinicznych o coraz bardziej złożonej strukturze. W miarę zbliżania się
parametru sterującego do wartości krytycznej układ przechodzi przez kolejne
bifurkacje wynikające z rozszczepiania tych orbit, co prowadzi do powstania
chaotycznego atraktora. Oryginalnyy układ równań ma postać
(1981, s. 220, równ. 11):
</p>

<p class="mathline">\( \dot{x} = \alpha x - \alpha y \)</p>
<p class="mathline">\( \dot{y} = -4\alpha y + xz + \mu x^{3} \)</p>
<p class="mathline">\( \dot{z} = -\delta \alpha z + xy + \beta z^{2} \)</p>

<p>
W analizie numerycznej autorzy przyjmują stałe parametry
\(\alpha = 1.8\), \(\beta = -0.07\) oraz \(\delta = 1.5\), a następnie badają zachowanie układu
przy zmianie parametru sterującego \(\mu\). Dla \(\mu \approx 0.076071\) pojawia się para
stabilnych orbit homoklinicznych, dla \(\mu = 0.05\) obserwuje się stabilną, symetryczną
orbitę okresową, natomiast dla \(\mu = 0.034\) – parę stabilnych orbit będących swoimi
obrazami względem symetrii \(S\). Dalsze zmniejszanie \(\mu\) prowadzi – dla \(\mu = 0.02\) – do powstania
atraktora o złożonej strukturze geometrycznej.
</p>


<p><b>Źródło:</b></p>
<p class="hanging-indent">
Arneodo, A., Coullet, P., & Tresser, C. (1981). A possible new mechanism for the onset of turbulence.
<i>Physics Letters A, 81(4), 197–201.</i>
DOI: <a href="https://doi.org/10.1016/0375-9601(81)90239-5" target="_blank">
https://doi.org/10.1016/0375-9601(81)90239-5

