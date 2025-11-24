---
layout: methods
lang: pl
title: Metoda Eulera
permalink: /pl/metody/euler/
alt_url: /en/methods/euler/
---

<p><b>Istota.</b> Metoda Eulera jest najprostszym sposobem aproksymacji 
rozwiązania równania różniczkowego. W każdym kroku czasowym wykorzystuje jedynie 
wartość pochodnej w bieżącym punkcie \( \mathbf{x}_n \). Pochodną tę interpretuje 
się jako wektor wskazujący kierunek i szybkość ruchu punktu. 
Metoda zakłada więc, że w krótkim przedziale czasu \( \Delta t \) punkt porusza się 
po linii prostej wyznaczonej przez tę pochodną. Dla układu 
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \) 
przybliżenie kolejnego punktu ma postać:
\( \mathbf{x}_{n+1} = \mathbf{x}_n + \Delta t\, f(\mathbf{x}_n) .\)
Oznacza to, że punkt przesuwamy o wartość pochodnej powiększoną o długość 
kroku czasowego \( \Delta t \). Metoda korzysta wyłącznie z informacji 
z punktu \( \mathbf{x}_n \), dlatego jest szybka, lecz mało dokładna.
</p>

<p><b>Przykład.</b> Rozważamy równanie 
\( \dot{x} = -2x \) z warunkiem początkowym \( x_0 = 1 \) 
i krokiem czasowym \( \Delta t = 0.1 \).<br>  
<i>Krok 1</i>: obliczamy pochodną w punkcie \( x_0 = 1 \):  
\( f(x_0) = -2 \cdot 1 = -2 \).<br>  
Nowe przybliżenie:  
\( x_1 = x_0 + 0.1 \cdot (-2) = 0.8 \).<br>  
<i>Krok 2</i>: obliczamy pochodną w punkcie \( x_1 = 0.8 \):  
\( f(x_1) = -2 \cdot 0.8 = -1.6 \). <br>  
Nowe przybliżenie:  
\( x_2 = 0.8 + 0.1 \cdot (-1.6) = 0.64 \). <br>  
<i>Krok 3</i>: pochodna: \( f(x_2) = -1.28 \).<br>    
Nowe przybliżenie:  
\( x_3 = 0.64 + 0.1 \cdot (-1.28) = 0.512 \).<br>
Kolejne kroki przebiegają analogicznie. Przy każdym kroku błąd 
tworzy się i narasta, ponieważ przyjmujemy liniową aproksymację 
pochodnej na całym odcinku długości \( \Delta t \).
</p>

<p><b>Zastosowanie.</b> 
Metoda Eulera sprawdza się jedynie w przypadku bardzo małych kroków czasowych 
\( \Delta t \) oraz w układach o łagodnej dynamice. W systemach chaotycznych 
szybko generuje duże błędy numeryczne, co prowadzi do zniekształcenia trajektorii. 
Z tego powodu traktuje się ją głównie jako metodę edukacyjną lub jako punkt wyjścia 
do bardziej zaawansowanych metod, takich jak Heun czy RK4.
</p>

<p><b>Implementacja.</b> W dodatku Attractor Builder
każdy krok metody Eulera realizuje funkcja <code>step_euler</code>. 
Przyjmuje ona funkcję prawej strony układu (<code>rhs_func</code>), 
bieżący wektor stanu <code>p</code>, słownik parametrów <code>params</code> oraz krok czasowy <code>dt</code>:

<code>
def step_euler(rhs_func, p: Vector, params: dict, dt: float):
    return p + rhs_func(p, params) * dt
</code>

<p> Funkcja <code>rhs_func</code> zwraca wektor pochodnych
 \( (\dot{x}, \dot{y}, \dot{z}) \) obliczonych w bieżącym punkcie 
 i dla zadanych parametrów \( a, b, c \). 
 Wywołanie <code>step_euler</code> oblicza 
nowe przybliżenie położenia punktu po upływie jednego kroku czasowego \( \Delta t = dt \).
 Na przykład gdy w Attractor Builder przyjmiemy (Lorenz):
 
<pre class="eq-plain">
<b>Równania:</b>
dx/dt = a * (y - x)
dy/dt = x * (b - z) - y
dz/dt = x * y - c * z
<b>Parametry:</b>
| a = 10 | b = 28 | c = 8/3 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Metoda: Euler
Krok czasowy (dt): 0.1
Liczba kroków: 3
Faza rozgrzewki (burn-in): 0
Skala: 1
</pre>
 
<p> W każdym kroku algorytm najpierw liczy pochodne \( (\dot{x}, \dot{y}, \dot{z}) \), 
a następnie aktualizuje współrzędne zgodnie z regułą 
\( x_{n+1} = x_n + \Delta t \,\dot{x}_n \):


<pre class="eq-plain">
<b>Krok 1.</b> Punkt początkowy:
x0 = 0.01; y0 = 0.01; z0 = 0.01.
Pochodne:
dx0 = 10*(y0-x0) = 10*(0.01-0.01) = 0
dy0 = x0*(28-z0) - y0 &approx; 0.01*(28-0.01) - 0.01 &approx; 0.2699
dz0 = x0*y0 - (8/3)*z0 &approx; 0.01*0.01 - (8/3)*0.01 &approx; -0.02657
Nowy punkt:
x1 = x0 + 0.01*dx0 = 0.01
y1 = y0 + 0.01*dy0 &approx; 0.01270
z1 = z0 + 0.01*dz0 &approx; 0.00973
<b>Krok 2.</b> Punkt wyjściowy:
x1 = 0.01; y1 &approx; 0.01270; z1 &approx; 0.00973.
Pochodne (zaokrąglone):
dx1 = 10*(y1-x1) &approx; 10*(0.01270-0.01) &approx; 0.02699
dy1 = x1*(28-z1) - y1 &approx; 0.01*(28-0.00973) - 0.01270 &approx; 0.26720
dz1 = x1*y1 - (8/3)*z1 &approx; 0.01*0.01270 - (8/3)*0.00973 &approx; -0.02583
Nowy punkt:
x2 = x1 + 0.01*dx1 &approx; 0.01 + 0.01*0.02699 &approx; 0.01027
y2 = y1 + 0.01*dy1 &approx; 0.01270 + 0.01*0.26720 &approx; 0.01537
z2 = z1 + 0.01*dz1 &approx; 0.00973 + 0.01*(-0.02583) &approx; 0.00948
<b>Krok 3.</b> Punkt wyjściowy:
x2 &approx; 0.01027; y2 &approx; 0.01537; z2 &approx; 0.00948.
Pochodne (zaokrąglone):
dx2 = 10*(y2-x2) &approx; 10*(0.01537-0.01027) &approx; 0.05101
dy2 = x2*(28-z2) - y2 &approx; 0.01027*(28-0.00948) - 0.01537 &approx; 0.27209
dz2 = x2*y2 - (8/3)*z2 &approx; 0.01027*0.01537 - (8/3)*0.00948 &approx; -0.02511
Nowy punkt:
x3 = x2 + 0.01*dx2 &approx; 0.01027 + 0.01*0.05101 &approx; 0.01078
y3 = y2 + 0.01*dy2 &approx; 0.01537 + 0.01*0.27209 &approx; 0.01809
z3 = z2 + 0.01*dz2 &approx; 0.00948 + 0.01*(-0.02511) &approx; 0.00922
</pre>


<p>
W kolejnych krokach procedura jest identyczna: w każdym punkcie oblicza się 
pochodne i stosuje wzór Eulera, aby przesunąć punkt o jeden krok czasowy 
\( \Delta t \). Przykład ten pokazuje, w jaki sposób ogólny układ Lorenza 
przechodzi w konkretne obliczenia numeryczne w dodatku.
</p>
