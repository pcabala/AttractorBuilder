---
layout: systems
title: "Atraktor Lü"
video: "/assets/media/attractors/lu.webm"
video_mp4: "/assets/media/attractors/lu.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/lu/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = a * (y - x)
ẏ = c * y - x * z
ż = x * y - b * z
<b>Parametry:</b>
| a = 36 | b = 3 | c = 20 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.1, y₀ = 0.1, z₀ = 0.1
Metoda: RK4  
Krok czasowy (dt): 0.005  
Liczba kroków: 10000  
Faza rozgrzewki (burn-in): 300  
Skala: 0.08
</pre>

<!-- a) Kontekst i tło historyczne -->
<p>
<b>Atraktor Lü</b> został wprowadzony w 2002 roku przez Jiana Lü i Guanronga Chena
jako nowy, trójwymiarowy system dynamiczny łączący cechy dwóch klasycznych
układów chaotycznych — Lorenza (1963) i Chena (1999).  
Autorzy pokazali, że poprzez odpowiedni dobór parametrów możliwe jest płynne
przejście od dynamiki typu Lorenza do typu Chena, co czyni atraktor Lü
układem pośrednim między tymi dwoma modelami. Oryginalny system równań (Lü & Chen, 2002, s. 660) ma postać:
</p>

<div class="math-left">
\[
\begin{cases}
\dot{x} = a\,(y - x)\\
\dot{y} = -x z + c\,y\\
\dot{z} = x y - b\,z
\end{cases}
\]
</div>

<style>
.math-left mjx-container[display="true"] { text-align: left !important; }  /* MathJax v3 */
.math-left .katex-display              { text-align: left !important; }  /* KaTeX */
</style>

<!-- b) Parametry i interpretacja -->
<p>
Parametr <i>a</i> określa intensywność sprzężenia pomiędzy zmiennymi <i>x</i> i <i>y</i>,
<i>b</i> kontroluje tłumienie wzdłuż osi <i>z</i>, natomiast <i>c</i> decyduje o
rozwoju niestabilności w kierunku osi <i>y</i>.  
Dla wartości <i>a = 36</i>, <i>b = 3</i> oraz <i>c</i> w zakresie od około 12,7 do 28,5
układ przejawia chaos, przy czym jego trajektoria przyjmuje postać
charakterystycznej podwójnej spirali zbliżonej do atraktora Lorenza.
</p>

<!-- c) Źródło -->
<p>
<b>Źródło:</b> Lü, J., & Chen, G. (2002).  
A new chaotic attractor coined.  
<i>International Journal of Bifurcation and Chaos</i>, 12(3), 659–661.  
DOI: <a href="https://doi.org/10.1142/S0218127402004620" target="_blank">
10.1142/S0218127402004620
</a>
</p>
