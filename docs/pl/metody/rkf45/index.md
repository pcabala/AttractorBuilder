---
layout: methods
lang: pl
title: Metoda Rungego–Kutty–Fehlberga
permalink: /pl/metody/rkf45/
alt_url: /en/methods/rkf45/
---

<p><b>Istota.</b> Metoda Rungego–Kutty–Fehlberga 4(5) (RKF45) jest 
przykładem <i>adaptacyjnej</i> metody całkowania równań 
różniczkowych zwyczajnych. Łączy w sobie dwie metody Rungego–Kutty 
różnego rzędu (4 oraz 5) w jednym schemacie obliczeniowym. Dla układu
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \) 
w jednym kroku obliczane są kolejne wektory nachyleń 
\( \mathbf{k}_1, \dots, \mathbf{k}_6 \), które następnie służą do 
wyznaczenia dwóch przybliżeń rozwiązania: 
\( \mathbf{y}_4 \) – przybliżenie 4 rzędu oraz
\( \mathbf{y}_5 \) – przybliżenie 5 rzędu (dokładniejsze).
Różnica \( \mathbf{y}_4 - \mathbf{y}_5 \) służy jako estymata błędu 
lokalnego w danym kroku. Na tej podstawie dobierana jest nowa długość
kroku czasowego \( \Delta t \): jeśli błąd jest mniejszy niż zadana 
tolerancja, krok jest akceptowany i czas może zostać <i>wydłużony</i>; 
jeśli błąd jest zbyt duży, krok jest <i>odrzucany</i>, a czas jest 
<i>skracany</i>. Dzięki temu zachowujemy kontrolę nad lokalnym błędem 
przy możliwie małej liczbie kroków.
</p>

<p><b>Zastosowanie.</b>
Metoda RKF45 jest jednym z najpopularniejszych schematów dla 
adaptacyjnego kroku czasowego. Dla trajektorii chaotycznych 
pozwala zwykle osiągnąć lepszy kompromis między dokładnością 
a czasem obliczeń niż metody o stałym kroku (Euler, Heun, RK4) 
z jedną, sztywno dobraną wartością \( \Delta t \). 
Zamiast żmudnie wyszukiwać „dobry” stały krok czasowy, 
użytkownik wybiera tolerancję błędu (np. \( 10^{-5} \)) 
oraz minimalny i maksymalny dopuszczalny krok, a metoda 
samoczynnie dostosowuje krok w trakcie symulacji.
</p>

<p><b>Implementacja.</b>  
W dodatku Attractor Builder każdy krok metody Rungego–Kutty–Fehlberga 4(5) 
realizuje funkcja 
<code>step_rkf45(rhs_func, p: Vector, params: dict, current_dt: float, tolerance: float)</code>. 
Metoda ta korzysta z tzw. tablic współczynników Fehlberga — szczególnego przypadku 
tablic Butchera opisujących metody Rungego–Kutty. 
Macierz \( A \) określa współczynniki przesunięć czasowych, czyli sposób, 
w jaki kolejne nachylenia <b>k</b><sub>2</sub>, <b>k</b><sub>3</sub>, … 
są obliczane z kombinacji liniowych wcześniejszych nachyleń 
<b>k</b><sub>1</sub>, <b>k</b><sub>2</sub> itd. 
Z kolei wektory wag \( B \) i \( B^* \) służą do budowy dwóch przybliżeń rozwiązania:  
głównego (rząd 5) oraz wbudowanego (rząd 4). 
Różnica między tymi przybliżeniami stanowi estymatę błędu lokalnego i decyduje o tym, 
czy krok czasowy zostanie zaakceptowany oraz jaką wartość przyjmie krok w kolejnym etapie.  
Tablicę Fehlberga 4(5), na której oparta jest implementacja RKF45, można znaleźć w  
(Hairer, Nørsett, Wanner 1993, Table&nbsp;5.1, s.&nbsp;177), natomiast ogólną definicję 
tablic Butchera przedstawiono w (Butcher 2008, s.&nbsp;98).

Zgodnie z tablicą Fehlberga nachylenia obliczane są następująco:


<code>
k1 = rhs_func(p, params)
k2 = rhs_func(p + A[1][0] * current_dt * k1, params)
k3 = rhs_func(p + current_dt * (A[2][0]*k1 + A[2][1]*k2), params)
k4 = rhs_func(p + current_dt * (A[3][0]*k1 + A[3][1]*k2 + A[3][2]*k3), params)
k5 = rhs_func(p + current_dt * (A[4][0]*k1 + A[4][1]*k2 + A[4][2]*k3 + A[4][3]*k4), params)
k6 = rhs_func(p + current_dt * (A[5][0]*k1 + A[5][1]*k2 + A[5][2]*k3 + A[5][3]*k4 + A[5][4]*k5), params)
</code>






<p><b>Implementacja.</b> W dodatku Attractor Builder każdy krok metody 
Rungego–Kutty–Fehlberga 4(5) realizuje funkcja 
<code>step_rkf45(rhs_func, p: Vector, params: dict, current_dt: float, tolerance: float)</code>. 
Metoda Fehlberga opiera się na tzw. tablicach Butchera: macierz 
\( A \) określa współczynniki przesunięć czasowych, czyli sposób, w jaki kolejne 
nachylenia <b>k</b><sub>2</sub>, <b>k</b><sub>3</sub>, …, są obliczane z kombinacji liniowych 
wcześniejszych nachyleń <b>k</b><sub>1</sub>, <b>k</b><sub>2</sub>, itd. 
Z kolei wektory wag \( B \) i \( B^* \) służą do budowy dwóch przybliżeń rozwiązania: 
przybliżenia rzędu 5 (głównego), otrzymywanego jako kombinacja liniowa nachyleń z wagami \( B \), 
oraz wbudowanego przybliżenia rzędu 4, wyznaczanego przy użyciu wag \( B^* \). 
Różnica między tymi dwoma rozwiązaniami stanowi estymatę lokalnego błędu i decyduje o tym, 
czy krok czasowy zostanie zaakceptowany, oraz jaką wartość przyjmie krok w następnym iteracji.
Opis metody Fehlberga i związanych z nią tablic Butchera można znaleźć 
w (Butcher, 2008) oraz w (Hairer, Nørsett, Wanner, 1993).
Zgodnie z tablicami Fehlberga nachylenia obliczane są następująco:
<code>
k1 = rhs_func(p, params)
k2 = rhs_func(p + A[1][0] * current_dt * k1, params)
k3 = rhs_func(p + current_dt * (A[2][0]*k1 + A[2][1]*k2), params)
k4 = rhs_func(p + current_dt * (A[3][0]*k1 + A[3][1]*k2 + A[3][2]*k3), params)
k5 = rhs_func(p + current_dt * (A[4][0]*k1 + A[4][1]*k2 + A[4][2]*k3 + A[4][3]*k4), params)
k6 = rhs_func(p + current_dt * (A[5][0]*k1 + A[5][1]*k2 + A[5][2]*k3 + A[5][3]*k4 + A[5][4]*k5), params)
</code>

<p>
Na ich podstawie otrzymujemy dwa przybliżenia rozwiązania:
<code>
y4 = p + current_dt * (B_star[0]*k1 + B_star[2]*k3 + B_star[3]*k4 + B_star[4]*k5)
y5 = p + current_dt * (B[0]*k1 + B[2]*k3 + B[3]*k4 + B[4]*k5 + B[5]*k6)
</code>
Różnica między nimi,
\( e = \| \mathbf{y}_5 - \mathbf{y}_4 \| \),
jest estymatą lokalnego błędu. 
Jeżeli błąd ten jest mniejszy od zadanej tolerancji, krok jest akceptowany,
a nowy punkt trajektorii to \( \mathbf{y}_5 \). 
W przeciwnym razie krok zostaje odrzucony, a algorytm zmniejsza krok czasowy 
i ponawia próbę.
Dzięki temu krok czasowy \( \Delta t \) dostosowuje się automatycznie do
lokalnej złożoności trajektorii: rośnie, gdy ruch jest łagodny,
i maleje w obszarach gwałtownych zmian, co pozwala zachować stabilność 
i wysoką dokładność przy minimalnym koszcie obliczeniowym.
</p>


<pre class="eq-plain">
<b>Równania:</b>
dx/dt = a * (y - x)
dy/dt = x * (b - z) - y
dz/dt = x * y - c * z
<b>Parametry:</b>
| a = 10 | b = 28 | c = 8/3 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Metoda: RKF45
Tolerancja: 0.000001
min_dt: 0.000001
max_dt: 0.05
Zapisane kroki: 3
Burn-in: 0
Skala: 1
</pre>

<p>
Korzystając z funkcji Raw Data → Export dodateku Attracotr Builder, możemy dokładnie śledzić, 
jak adaptacyjna metoda RKF45 dobiera krok na każdym etapie integracji. 
Pierwsze cztery punkty uzyskane bezpośrednio z eksportu CSV wyglądają następująco:</p>

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
<tr><td>2</td><td>0.02685</td><td>0.01166</td><td>0.02034</td><td>0.00907</td></tr>
<tr><td>3</td><td>0.02697</td><td>0.01481</td><td>0.02956</td><td>0.00845</td></tr>
</tbody>
</table>

<p>
Widzimy wyraźnie, że po pierwszym kroku adaptacyjny algorytm zwiększa 
krok czasowy z 0.01 do około 0.0269 w trzecim kroku, 
co oznacza, że w tym fragmencie trajektorii 
ruch jest bardziej regularny i metoda może używać większego kroku bez utraty 
dokładności. Takie zachowanie stanowi 
główną przewagę metod adaptacyjnych nad metodami o stałym kroku.
</p>

<br>
<p><b>Źródła:</b></p>

<p class="hanging-indent">
Butcher, J. C. (2008). <i>Numerical Methods for Ordinary Differential Equations</i>.
Wiley.
</p>

<p class="hanging-indent">
Hairer, E., Nørsett, S., Wanner, G. (1993). 
<i>Solving Ordinary Differential Equations I</i>. Springer.
</p>