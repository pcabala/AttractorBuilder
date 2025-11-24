---
layout: methods
lang: pl
title: Metoda Rungego–Kutty
permalink: /pl/metody/rk4/
alt_url: /en/methods/rk4/
---

<p><b>Istota.</b> Metoda Rungego–Kutty rzędu 4 (RK4) jest 
jedną z najczęściej stosowanych metod całkowania równań różniczkowych. 
Podobnie jak metoda Heuna, opiera się na uśrednianiu nachyleń, 
ale zamiast dwóch wykorzystuje aż cztery przybliżenia pochodnej w obrębie 
jednego kroku czasowego \( \Delta t \). Dla układu 
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \) 
metoda RK4 wykorzystuje cztery wektory nachylenia:


\( \mathbf{k}_1 = f(\mathbf{x}_n) \),
\( \mathbf{k}_2 = f\big(\mathbf{x}_n + \tfrac{\Delta t}{2} \mathbf{k}_1\big) \),
\( \mathbf{k}_3 = f\big(\mathbf{x}_n + \tfrac{\Delta t}{2} \mathbf{k}_2\big) \),
\( \mathbf{k}_4 = f\big(\mathbf{x}_n + \Delta t \,\mathbf{k}_3\big) \).

Następnie kolejną wartość stanu wyznacza się jako ważoną średnią tych 
nachyleń:

<p class="mathline">
\( \displaystyle 
\mathbf{x}_{n+1} = \mathbf{x}_n + \frac{\Delta t}{6}
\big( \mathbf{k}_1 + 2\mathbf{k}_2 + 2\mathbf{k}_3 + \mathbf{k}_4 \big).
\)
</p>

<p>
Intuicyjnie można traktować RK4 jako wielostopniowe „doprecyzowanie” 
kroku Eulera: kolejne nachylenia \( \mathbf{k}_2, \mathbf{k}_3, \mathbf{k}_4 \) 
sprawdzają, jak zmienia się pochodna w środku i na końcu kroku. 
Dzięki temu metoda ma rząd 4, a jej błąd globalny jest zwykle 
o rzędy wielkości mniejszy niż w metodach Eulera czy Heuna 
dla tego samego kroku \( \Delta t \).
</p>

<p><b>Przykład.</b> Rozważmy ponownie proste równanie
\( \dot{x} = -2x \) z warunkiem początkowym \( x_0 = 1 \) 
i krokiem czasowym \( \Delta t = 0.1 \). Dla każdej iteracji 
obliczamy cztery nachylenia i średnią ważoną.
W kroku pierwszym (od \( x_0 \) do \( x_1 \)) mamy
\( f(x) = -2x \), nachylenia:<br>

\( k_1 = f(x_0) = -2 \cdot 1 = -2 \),<br>
\( k_2 = f(x_0 + 0.5 \Delta t\, k_1) 
= f(1 + 0.5 \cdot 0.1 \cdot (-2)) = f(0.9) = -1.8 \),<br>
 \( k_3 = f(x_0 + 0.5 \Delta t\, k_2) 
= f(1 + 0.5 \cdot 0.1 \cdot (-1.8)) = f(0.91) = -1.82 \),<br>
 \( k_4 = f(x_0 + \Delta t\, k_3) 
= f(1 + 0.1 \cdot (-1.82)) = f(0.818) = -1.636 \),<br>
średnią ważoną nachyleń:<br>
\( \bar{k} = \tfrac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4) 
\approx \tfrac{1}{6}(-2 - 3.6 - 3.64 - 1.636) \approx -1.818 \),<br>
oraz, ostatecznie, nowy punkt:<br>
\( x_1 = x_0 + \Delta t\,\bar{k} 
\approx 1 + 0.1 \cdot (-1.818) \approx 0.8182. \)<br>

Dla porównania: metoda Eulera dałaby \( x_1 = 0.8 \), 
Heun \( x_1 = 0.82 \), a RK4 \( x_1 \approx 0.8182 \), 
czyli bliżej dokładnego rozwiązania \( x(t) = e^{-2t} \) 
( dla \( t = 0.1 \) mamy \( e^{-0.2} \approx 0.8187 \) ).
W kolejnych krokach powtarzamy tę samą procedurę: w każdym kroku 
obliczamy \( k_1, k_2, k_3, k_4 \) w oparciu o poprzednią wartość \( x_n \) 
i z nich budujemy \( x_{n+1} \). Dla danego \( \Delta t \) metoda RK4 
daje zdecydowanie mniejszy błąd niż Euler czy Heun, 
choć wymaga więcej wywołań funkcji \( f \) (cztery zamiast jednego lub dwóch).
</p>

<p><b>Zastosowanie.</b>
Metoda RK4 jest „złotym środkiem” pomiędzy dokładnością 
a złożonością obliczeniową. Sprawdza się bardzo dobrze w wielu 
zastosowaniach inżynierskich i naukowych, także w przypadku trajektorii 
chaotycznych, o ile krok \( \Delta t \) jest dobrany rozsądnie. 
Dla zbyt dużych kroków chaos nadal może „rozjechać” trajektorie, 
ale granica stabilności i jakość odwzorowania kształtu atraktora 
są znacznie lepsze niż w metodach Eulera czy Heuna. 
W praktyce RK4 jest często pierwszym wyborem, gdy zależy nam 
na dobrej jakości integracji przy stałym kroku czasowym.
</p>

<p><b>Implementacja.</b> W dodatku Attractor Builder 
każdy krok metody RK4 realizuje funkcja <code>step_rk4</code>. 
Podobnie jak w metodzie Heuna, korzystamy z funkcji prawej strony 
układu <code>rhs_func</code>, która dla zadanych współrzędnych 
<i>i</i> parametrów zwraca wektor pochodnych 
\( (\dot{x}, \dot{y}, \dot{z}) \). 
Implementacja w Pythonie (uproszczona do postaci używanej w dodatku) 
ma postać:
<code>
def step_rk4(rhs_func, p: Vector, params: dict, dt: float):
    k1 = rhs_func(p, params)
    k2 = rhs_func(p + 0.5 * dt * k1, params)
    k3 = rhs_func(p + 0.5 * dt * k2, params)
    k4 = rhs_func(p + dt * k3, params)
    return p + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
</code>

<p>
Procedura obliczeń jest zgodna z ogólnymi wzorami podanymi wyżej.
W kroku 1 obliczamy pochodną w punkcie bieżącym \( p \).
W kroku 2 przesuwamy się o pół kroku w kierunku \( k_1 \) 
i obliczamy pochodną w tym punkcie.
W kroku 3 ponownie przesuwamy się o pół kroku, tym razem w kierunku \( k_2 \),
i obliczamy pochodną.
W kroku 4 przesuwamy się o cały krok w kierunku \( k_3 \) 
i liczymy pochodną na końcu kroku.
Ostatecznie (krok 5) otrzymujemy jako kombinację liniową 
\( k_1, k_2, k_3, k_4 \), z wagami 1–2–2–1.
Na przykład, gdy w Attractor Builder przyjmiemy (Lorenz):<br>
<pre class="eq-plain">
<b>Równania:</b>
dx/dt = a * (y - x)
dy/dt = x * (b - z) - y
dz/dt = x * y - c * z
<b>Parametry:</b>
| a = 10 | b = 28 | c = 8/3 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Metoda: RK4
Krok czasowy (dt): 0.01
Liczba kroków: 3
Faza rozgrzewki (burn-in): 0
Skala: 1
</pre>

<p>
W każdym kroku algorytmu RK4 wykonywane są cztery wywołania 
<code>rhs_func</code>, generujące wektory nachyleń 
\( \mathbf{k}_1, \mathbf{k}_2, \mathbf{k}_3, \mathbf{k}_4 \). 
Następnie obliczana jest średnia ważona tych nachyleń, zgodnie ze 
schematem RK4. W efekcie kolejne punkty trajektorii 
\( (x_1, y_1, z_1), (x_2, y_2, z_2), (x_3, y_3, z_3) \)
lepiej odwzorowują rzeczywisty kształt atraktora Lorenza niż te 
uzyskane metodą Eulera lub Heuna przy tym samym kroku czasowym
\( \Delta t = 0.01 \).
Współrzędne punktów można uzyskać bezpośrednio z dodatku Attractor Builder, 
korzystając z funkcji Raw Data → Export. Wyniki obliczeń są eksportowane do pliku csv. 
W pierwszym wierszu csv znajdują się dane dotyczące stanu początkowego, 
a w kolejnych współrzędne punktów po każdym kroku integracji. 
Dla ustawień pokazanych wyżej dane wyglądają następująco:
</p>

<!-- Styl dla tabeli zgodny z eq-plain -->
<style>
.table-eq td, .table-eq th {
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
    font-size: 0.90rem;
    text-align: center;
    padding: 0.25rem 0.5rem;
}
.table-eq thead th {
    font-weight: 700;
}
</style>

<table class="table-eq">
<thead>
<tr><th>steps</th><th>dt</th><th>x</th><th>y</th><th>z</th></tr>
</thead>
<tbody>
<tr><td>0</td><td>0.00000</td><td>0.01000</td><td>0.01000</td><td>0.01000</td></tr>
<tr><td>1</td><td>0.01000</td><td>0.01013</td><td>0.01270</td><td>0.00974</td></tr>
<tr><td>2</td><td>0.01000</td><td>0.01051</td><td>0.01544</td><td>0.00948</td></tr>
<tr><td>3</td><td>0.01000</td><td>0.01111</td><td>0.01829</td><td>0.00924</td></tr>
</tbody>
</table>

<p>
Wiersz \(0\) zawiera stan początkowy 
\( (x_0, y_0, z_0) = (0.01, 0.01, 0.01) \).
Wiersze 1–3 odpowiadają punktom 
\( (x_1, y_1, z_1) \),  
\( (x_2, y_2, z_2) \),  
\( (x_3, y_3, z_3) \),  
wyznaczonym metodą RK4.  
Taka forma danych umożliwia łatwe porównywanie metod integracji, 
analizę trajektorii oraz eksport do narzędzi takich jak Python, MATLAB czy Excel.
</p>

