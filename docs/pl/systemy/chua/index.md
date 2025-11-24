---
layout: systems
title: "Atraktor Chua"
video: "/assets/media/attractors/chua.webm"
video_mp4: "/assets/media/attractors/chua.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/chua/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = k*p*(y - x - (b*x + 0.5*(a - b)*(fabs(x + 1) - fabs(x - 1))))
ẏ = k*(x - y + z)
ż = k*(-q*y - r*z)
<b>Parametry:</b>
| a = 0.1 | b= -0.48 | k = 1 | p = -1.3 | q = -0.0136 | r = -0.0297 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.1, y₀ = 0.0, z₀ = 0.0
Metoda: DP5
Tolerancja: 0.0001
Krok min: 0.0001
Krok max: 0.1
Liczba kroków: 20000
Faza rozgrzewki (burn-in): 500
Skala: 0.7
</pre>

<p>
<b>Atraktor Chua</b> jest jednym z przykładów chaosu w fizycznych 
układach elektronicznych. W badaniach nad nieliniowymi sieciami 
dynamicznymi Leona O. Chua (1983) szukał prostych obwodów ze sprzężeniem 
zwrotnym, które byłby zdolne do generowania złożonych, nieperiodycznych trajektorii. 
Na tej bazie Takashi Matsumoto w 1984 roku
przedstawił pierwszą eksperymentalną i numeryczną demonstrację
chaotycznego zachowania w rzeczywistym obwodzie RLC z nieliniowym
rezystorem Chua. Ostatecznie, układ równań stanu 
oscylatora podany przez Chua ma postać (1995, s. 3):

<p class="mathline">\( \dfrac{dx}{dt} = k \alpha \bigl(y - x - f(x)\bigr), \)</p>
<p class="mathline">\( \dfrac{dy}{dt} = k \bigl(x - y + z\bigr), \)</p>
<p class="mathline">\( \dfrac{dz}{dt} = k \bigl(-\beta y - \gamma z\bigr). \)</p>

<p>
W tym układzie nieliniowość wprowadzana jest przez
funkcję \( f(x) = b x + \tfrac{1}{2}(a - b)(|x + 1| - |x - 1|) \), która opisuje
odcinkowo-liniową charakterystykę tzw. diody Chua.
</p>


<p><b>Źrdóła:</b></p>

<p class="hanging-indent">
Matsumoto, T. (1984). A chaotic attractor from Chua’s circuit.
<i>IEEE Transactions on Circuits and Systems</i>, 31(12), 1055–1058.
<a href="https://doi.org/10.1109/TCS.1984.1085459" target="_blank">
https://doi.org/10.1109/TCS.1984.1085459
</a>
</p>

<p class="hanging-indent">
Chua, L. O. (1983). Dynamic Nonlinear Networks: State-of-the-Art.
<i>IEEE International Symposium on Circuits and Systems</i>, 12, 2–6.
<a href="https://doi.org/10.1109/TCS.1980.1084745" target="_blank">
https://doi.org/10.1109/TCS.1980.1084745
</a>
</p>

<p class="hanging-indent">
Chua, L. O. (1995). A glimpse of nonlinear phenomena from Chua’s oscillator.
<i>Philosophical Transactions of the Royal Society A</i>, 353(1701), 3–12.
<a href="https://www.jstor.org/stable/54515" target="_blank">
https://www.jstor.org/stable/54515
</a>
</p>
