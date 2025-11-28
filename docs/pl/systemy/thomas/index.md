---
layout: systems
title: "Atraktor Thomasa"
video_mp4: "/assets/media/attractors/thomas.mp4"
stop_at: 11
lang: pl
alt_url: /en/systems/thomas/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = - b*x + sin(y)
ẏ = - b*y + sin(z)
ż = - b*z + sin(x)
<b>Parametry:</b>
| b = 1.5 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.02, y₀ = 0.01, z₀ = 0.03
Metoda: RK4
Time Step (dt): 0.03
Steps: 10000
Burn-in: 500
Skala: 0.7
</pre>

<p>
<b>Atraktor Thomasa</b> jest przykładem trójwymiarowego układu nieliniowego,
w którym chaotyczna dynamika wynika ze struktury sprzężeń zwrotnych między
zmiennymi. Został opisany przez René Thomasa w pracy poświęconej analizie
chaosu w układach z pętlami sprzężenia oraz konstrukcji prostych modeli
wykazujących złożone zachowanie dynamiczne.
Autor przedstawia ogólny układ (1999, s. 1896, równ. 2):
</p>

<p class="mathline">\( \dot{x} = -b x + f(y), \)</p>
<p class="mathline">\( \dot{y} = -b y + f(z), \)</p>
<p class="mathline">\( \dot{z} = -b z + f(x), \)</p>

<p>
gdzie \(b > 0\) jest współczynnikiem tłumienia, a funkcja \(f\) wprowadza
nieliniowość odpowiedzialną za powstawanie chaosu. Thomas pokazał, że wiele
różnych funkcji, tym \(f(u)=\sin u\), prowadzi do powstania trajektorii chaotycznych
pod warunkiem zachowania cyklicznego sprzężenia między zmiennymi.
Dla wartości \(b \approx 0.15\) układ ten generuje złożone, nieperiodyczne trajektorie,
które wielokrotnie oplatają się wokół symetrycznych obszarów w przestrzeni fazowej.
System ten jest przykładem tzw. „chaosu labiryntowego”, opisywanego przez Thomasa 
jako efekt wynikający z cyklicznych sprzężeń i nieliniowej odpowiedzi.
</p>

<p><b>Źródło:</b></p>
<p class="hanging-indent">
Thomas, R. (1999). Deterministic chaos seen in terms of feedback circuits:
analysis, synthesis, “labyrinth chaos”.
<i>International Journal of Bifurcation and Chaos</i>, 9(10), 1889–1905.
<a href="https://doi.org/10.1142/S0218127499001383" target="_blank">
https://doi.org/10.1142/S0218127499001383
</a>

