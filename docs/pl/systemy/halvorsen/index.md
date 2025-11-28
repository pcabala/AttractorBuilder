---
layout: systems
title: "Atraktor Halvorsena"
video_mp4: "/assets/media/attractors/halvorsen.mp4"
stop_at: 11
lang: pl
alt_url: /en/systems/halvorsen/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = -a*x - 4*y - 4*z - y**2
ẏ = -a*y - 4*z - 4*x - z**2
ż = -a*z - 4*x - 4*y - x**2
<b>Parametry:</b>
| a = 1.4 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.01, y₀ = 0, z₀ = 0.01
Metoda: DP5
Tolerancja: 0.0001
Krok min: 0.000001
Krok max: 0.1
Liczba kroków: 10000
Faza rozgrzewki (burn-in): 300
Skala: 0.2
</pre>

<!-- a) Kontekst i tło historyczne -->
<p>
<b>Atraktor Halvorsena</b> to symetryczny, trójwymiarowy układ chaotyczny
zaproponowany przez Arne Dehli Halvorsena na grupie dyskusyjnej
<i>sci.fractals</i> w latach 90. XX wieku.  
Zyskał on zainteresowanie środowiska naukowego dzięki swojej
cyklicznej symetrii oraz estetycznej, trójskrzydłowej strukturze.
Formalna analiza systemu została później przeprowadzona i opublikowana
przez Juliena C. Sprotta w 1997 roku w notatce technicznej
<i>A Symmetric Chaotic Flow</i> (University of Wisconsin–Madison).
Oryginalny system równań (Sprott, 1997) ma postać:
</p>

<!-- b) System of equations -->
<p class="mathline">\(\dot{x} = -a x - 4y - 4z - y^{2}\)</p>
<p class="mathline">\(\dot{y} = -a y - 4z - 4x - z^{2}\)</p>
<p class="mathline">\(\dot{z} = -a z - 4x - 4y - x^{2}\)</p>

<!-- b) Parametry i interpretacja -->
<p>
Układ Halvorsena jest wyjątkowy dzięki swojej pełnej symetrii cyklicznej:
równania pozostają niezmienione przy zamianie zmiennych
\(x \rightarrow y \rightarrow z \rightarrow x\).  
Parametr <i>a</i> kontroluje tłumienie i decyduje o przejściu
od ruchu okresowego do chaosu.
Sprott wykazał, że dla <i>a ≈ 1.27</i> system przechodzi drogę do chaosu
poprzez klasyczną kaskadę podwojeń okresu, tworząc złożoną strukturę
atraktora w przestrzeni fazowej.
</p>


<!-- d) Źródło -->
<p>
<b>Źródło:</b>  
Sprott, J. C. (1997, revised 2004).  
<i>A Symmetric Chaotic Flow.</i>  
Department of Physics, University of Wisconsin–Madison.  
Dostęp online:  
<a href="https://sprott.physics.wisc.edu/chaos/symmetry.htm" target="_blank">
https://sprott.physics.wisc.edu/chaos/symmetry.htm
</a>
</p>
