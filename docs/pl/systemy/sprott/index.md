---
layout: systems
title: "Atraktory Sprotta"
video: "/assets/media/attractors/sprott.webm"
video_mp4: "/assets/media/attractors/sprott.mp4"
alpha: true
stop_at: 11
lang: pl
alt_url: /en/systems/sprott/
---

<pre class="eq-plain">
Attractor Builder (dodatek do Blendera)
<b>Równania:</b>
ẋ = -y
ẏ = x + z
ż = x*z + a*y**2 
<b>Parametry:</b>
| a = 3 |  
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.1, y₀ = 0, z₀ = 0  
Metoda: RK4  
Krok czasowy (dt): 0.01  
Liczba kroków: 30000  
Faza rozgrzewki (burn-in): 500  
Skala: 0.7
</pre>

<p>
<b>Atraktory Sprotta</b> stanowią rodzinę prostych układów chaotycznych
zaproponowanych przez Juliena C. Sprotta w 1994 r.
Autor przeanalizował ogólną postać trójwymiarowych, autonomicznych układów równań różniczkowych
z nieliniowościami kwadratowymi i odnalazł dziewiętnaście różnych przykładów wykazujących
chaos deterministyczny.  
Układy te – oznaczone literami od A do S – charakteryzują się wyjątkową prostotą:
każdy zawiera jedynie pięć lub sześć wyrazów, z jedną lub dwiema nieliniowościami.  
Poniżej przedstawiono wszystkie układy (A–S) w oryginalnej postaci (1994, s.&nbsp;649, tabela I):
</p>

<p>A: <span class="mathline">\(\dot{x}=y,\ \dot{y}=-x+y\,z,\ \dot{z}=1-y^{2}\)</span></p>
<p>B: <span class="mathline">\(\dot{x}=y\,z,\ \dot{y}=x-y,\ \dot{z}=1-x\,y\)</span></p>
<p>C: <span class="mathline">\(\dot{x}=y\,z,\ \dot{y}=x-y,\ \dot{z}=1-x^{2}\)</span></p>
<p>D: <span class="mathline">\(\dot{x}=-y,\ \dot{y}=x+z,\ \dot{z}=x\,z+3\,y^{2}\)</span></p>
<p>E: <span class="mathline">\(\dot{x}=y\,z,\ \dot{y}=x^{2}-y,\ \dot{z}=1-4\,x\)</span></p>
<p>F: <span class="mathline">\(\dot{x}=y+z,\ \dot{y}=-x+0.5\,y,\ \dot{z}=x^{2}-z\)</span></p>
<p>G: <span class="mathline">\(\dot{x}=0.4\,x+z,\ \dot{y}=x\,z-y,\ \dot{z}=-x+y\)</span></p>
<p>H: <span class="mathline">\(\dot{x}=-y+z^{2},\ \dot{y}=x+0.5\,y,\ \dot{z}=x-z\)</span></p>
<p>I: <span class="mathline">\(\dot{x}=-0.2\,y,\ \dot{y}=x+z,\ \dot{z}=x+y^{2}-z\)</span></p>
<p>J: <span class="mathline">\(\dot{x}=2\,z,\ \dot{y}=-2\,y+z,\ \dot{z}=-x+y+y^{2}\)</span></p>
<p>K: <span class="mathline">\(\dot{x}=x\,y-z,\ \dot{y}=x-y,\ \dot{z}=x+0.3\,z\)</span></p>
<p>L: <span class="mathline">\(\dot{x}=y+3.9\,z,\ \dot{y}=0.9\,x^{2}-y,\ \dot{z}=1-x\)</span></p>
<p>M: <span class="mathline">\(\dot{x}=-z,\ \dot{y}=-x^{2}-y,\ \dot{z}=1.7+1.7\,x+y\)</span></p>
<p>N: <span class="mathline">\(\dot{x}=-2\,y,\ \dot{y}=x+z^{2},\ \dot{z}=1+y-2\,z\)</span></p>
<p>O: <span class="mathline">\(\dot{x}=y,\ \dot{y}=x-z,\ \dot{z}=x+x\,z+2.7\,y\)</span></p>
<p>P: <span class="mathline">\(\dot{x}=2.7\,y+z,\ \dot{y}=-x+y^{2},\ \dot{z}=x+y\)</span></p>
<p>Q: <span class="mathline">\(\dot{x}=-z,\ \dot{y}=x-y,\ \dot{z}=3.1\,x+y^{2}+0.5\,z\)</span></p>
<p>R: <span class="mathline">\(\dot{x}=0.9-y,\ \dot{y}=0.4+z,\ \dot{z}=x\,y-z\)</span></p>
<p>S: <span class="mathline">\(\dot{x}=-x-4\,y,\ \dot{y}=x+z^{2},\ \dot{z}=1+x\)</span></p>

<p>
Przypadki A–E mają pięć wyrazów i dwie nieliniowości, natomiast F–S – sześć wyrazów i jedną.
Są to trójwymiarowe systemy dysypatywne o dziwnych atraktorach, 
które często wykazują spiralną strukturę z jednym fałdem, podobną do atraktora Rösslera.
W dodatku do Blendera podano układ równań dla atraktora D, 
który należy do grupy systemów z dwiema nieliniowościami.  
Charakteryzuje się on złożonym, spiralnym ruchem z jednym punktem skupienia
i wyraźną strukturą fałdu, przypominającą atraktor Rösslera.  
Jest to jeden z klasycznych przykładów, w których prosty zestaw równań
generuje bogate, nieregularne trajektorie w przestrzeni fazowej.
Wymienione wyżej układy generujące chaos deterministyczny zostały
szczgółowo opisane przez Sprotta w jego książce <i>Elegant Chaos: Algebraically Simple Chaotic Flows</i> (2010),
która stanowi kompleksowe opracowanie tematu prostych trójwymiarowych układów chaotycznych.
</p>

<!-- d) Źródła -->
<p><b>Źródła:</b></p>

<p class="hanging-indent">
Sprott, J. C. (1994).  
<i>Some simple chaotic flows.</i>  
<i>Physical Review E</i>, 50(2), 647–650.  
DOI: <a href="https://doi.org/10.1103/PhysRevE.50.R647" target="_blank">
https://doi.org/10.1103/PhysRevE.50.R647
</a>
</p>
<p class="hanging-indent">
Sprott, J. C. (2010).  
<i>Elegant Chaos: Algebraically Simple Chaotic Flows.</i>  
World Scientific Publishing, Singapore.  
DOI: <a href="https://doi.org/10.1142/7183" target="_blank">
https://doi.org/10.1142/7183
</a>
</p>