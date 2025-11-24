---
layout: systems
title: "Atraktor Hindmarsha–Rose’a"
video: "/assets/media/attractors/hindmarsh-rose.webm"
video_mp4: "/assets/media/attractors/hindmarsh-rose.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/hindmarsh-rose/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = y - a*x**3 + b*x**2 + I - z  
ẏ = c - d*x**2 - y  
ż = r*(s*(x - x1) - z)
<b>Parametry:</b>
| a = 1.0 | b = 3.0 | c = 1.0 | d = 5.0 | s = 4.0 | r = 0.006 | x1 = -1.6 | I = 3.25 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.0, y₀ = 0.0, z₀ = 0.0  
Metoda: RK4  
Krok czasowy (dt): 0.01  
Liczba kroków: 50000  
Faza rozgrzewki (burn-in): 1000  
Skala: 0.3
</pre>

<!-- a) Kontekst i tło historyczne -->
<p>
<b>Atraktor Hindmarsha–Rose’a</b> pochodzi z neurobiologii i został opracowany
przez <i>J. L. Hindmarsha</i> i <i>R. M. Rose’a</i> w 1984 r. jako model opisujący
elektryczną aktywność pojedynczego neuronu.  
Układ ten odtwarza zjawiska przejść między stanem spoczynku,
regularnymi impulsami (<i>spiking</i>) oraz seriami szybkich impulsów (<i>bursting</i>),
charakterystyczne dla neuronów kory mózgowej.  
Trajektorie atraktora ukazują chaotyczne przełączanie między tymi trybami,
a sam model jest jednym z pierwszych przykładów zastosowania dynamiki nieliniowej
do biologicznych układów pobudliwych.
Oryginalny układ równań (Hindmarsh & Rose 1984, s.&nbsp;95, równanie 15) ma postać:
</p>

<!-- b) Oryginalny układ równań -->
<div class="math-left">
\[
\begin{cases}
\dot{x} = y - a x^{3} + b x^{2} + I - z,\\[4pt]
\dot{y} = c - d x^{2} - y,\\[4pt]
\dot{z} = r\big(s(x - x_{1}) - z\big).
\end{cases}
\]
</div>

<style>
.math-left mjx-container[display="true"] { text-align: left !important; }  /* MathJax v3 */
.math-left .katex-display              { text-align: left !important; }  /* KaTeX */
</style>

<p>
Model ten obejmuje trzy zmienne:  
\(x\) — potencjał błony neuronu,  
\(y\) — szybkie procesy jonowe odpowiedzialne za powstawanie impulsu,  
\(z\) — wolne prądy wapniowe modulujące dynamikę błony.  
Wartości parametrów określają charakter aktywności neuronu:  
zmiana prądu wejściowego \(I\) reguluje przejścia między stanem spoczynku,
regularnym wyładowaniem a chaotycznym <i>burstingiem</i>.  
Autorzy podkreślili, że nawet w tak prostym trójzmiennym układzie
nieliniowe sprzężenie między szybkim a wolnym kanałem jonowym
wystarcza do generowania złożonych, realistycznych wzorców neuronalnych.
</p>

<!-- d) Źródła -->
<p><b>Źródło:</b></p>

<p class="hanging-indent">
Hindmarsh, J. L., & Rose, R. M. (1984).  
<i>A model of neuronal bursting using three coupled first order differential equations.</i>  
<i>Proceedings of the Royal Society of London. Series B. Biological Sciences</i>, 221(1222), 87–102.  
DOI: <a href="https://doi.org/10.1098/rspb.1984.0024" target="_blank">
https://doi.org/10.1098/rspb.1984.0024
</a>
</p>
