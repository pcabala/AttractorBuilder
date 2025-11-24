---
layout: systems
title: "Atraktor Rabinovicha–Fabrikanta"
video: "/assets/media/attractors/rabinovich-fabrikant.webm"
video_mp4: "/assets/media/attractors/rabinovich-fabrikant.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/rabinovich-fabrikant/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = y*(z - 1 + x**2) + a*x
ẏ = x*(3*z + 1 - x**2) + a*y
ż = -2*z*(b + x*y)
<b>Parametry:</b>
| a = 0.87 | b = 1.1 |   <!-- aliasy w dodatku: a≡γ, b≡ν -->
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = -1, y₀ = 0, z₀ = 0.5
Metoda: DP5
Tolerancja: 0.00005
Krok min: 0.000001
Krok max: 0.05
Liczba kroków: 7000
Faza rozgrzewki (burn-in): 1000
Skala: 2
</pre>

<!-- a) Kontekst i tło historyczne -->
<p>
<b>Atraktor Rabinovicha–Fabrikanta</b> został wprowadzony w 1979 roku przez
M. I. Rabinovicha i A. L. Fabrikanta z Instytutu Fizyki Stosowanej Akademii Nauk ZSRR.
Powstał podczas badań nad rozwojem niestabilności modulacyjnej w ośrodkach nieliniowych
znajdujących się w stanie nierównowagi.  
Autorzy analizowali proces samomodulacji fal i wykazali, że nawet w prostym
trójmodalnym modelu opisującym sprzężenie pomiędzy falą podstawową i jej satelitami
mogą powstawać złożone, aperiodiczne trajektorie w przestrzeni fazowej.
Oryginalny układ równań ma postać następującą (1979, s.&nbsp;311, równanie&nbsp;2):
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x}=y\,(z-1+x^{2})+\gamma\,x\)</p>
<p class="mathline">\(\dot{y}=x\,(3z+1-x^{2})+\gamma\,y\)</p>
<p class="mathline">\(\dot{z}=-2z\,(\nu+x\,y)\)</p>

<!-- c) Parametry i interpretacja -->
<p>
W oryginalnej publikacji parametr \(\gamma\) opisuje przyrost niestabilności —
określa stopień aktywności ośrodka, czyli efektywne wzmocnienie oscylacji w kanałach
\(x\) i \(y\).  
Parametr \(\nu\) reprezentuje tłumienie satelitów, odpowiadające stratom energii
w ośrodku w wyniku oddziaływań dyssypatywnych.  
Dla małych wartości \(\gamma/\nu\) układ stabilizuje się i wykazuje zachowanie okresowe,
natomiast przy wzroście tego stosunku pojawiają się cykle graniczne, bifurkacje
i ostatecznie chaos deterministyczny.  
Autorzy wskazali, że dla wartości \(\gamma \approx 0.87\) i \(\nu \approx 1.1\)
trajektorie układu tworzą złożony atraktor o nieregularnej strukturze.
</p>

<!-- d) Źródła -->
<p><b>Źródła:</b></p>

<p class="hanging-indent">
Rabinovich, M. I., &amp; Fabrikant, A. L. (1979).  
<i>Stochastic self-modulation of waves in nonequilibrium media.</i>  
<i>Soviet Physics JETP</i>, 50(2), 311–316.  
PDF: <a href="http://jetp.ras.ru/cgi-bin/dn/e_050_02_0311.pdf" target="_blank">
http://jetp.ras.ru/cgi-bin/dn/e_050_02_0311.pdf
</a>
</p>
