---
layout: methods
lang: pl
title: Metoda Dormanda–Prince’a
permalink: /pl/metody/dp5/
alt_url: /en/methods/dp5/
---

<p><b>Istota.</b> Metoda Dormanda–Prince’a 5(4) (DP5) jest adaptacyjną 
metodą Rungego–Kutty o rzędach 5 i 4, podobnie jak RKF45, lecz z innym 
doborem współczynników. Wariant Dormanda–Prince’a został zaprojektowany 
tak, aby rozwiązanie rzędu 5 (główne) miało szczególnie mały błąd globalny, 
a rozwiązanie rzędu 4 służyło jedynie do kontroli błędu lokalnego. 
Dla układu
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \) 
metoda w jednym kroku oblicza wektory nachyleń 
\( \mathbf{k}_1, \dots, \mathbf{k}_7 \) według tablic Butchera, 
a następnie na ich podstawie wyznacza przybliżenie rzędu 5, 
oznaczane zwykle jako \( \mathbf{y}_5 \),
oraz konstruuje „towarzyszące” przybliżenie rzędu 4 przy użyciu innych wag.
Różnica między tymi dwoma przybliżeniami jest estymatą lokalnego błędu 
w danym kroku. Na podstawie tej estymaty dobierana jest nowa długość 
kroku czasowego \( \Delta t \), podobnie jak w metodzie RKF45: 
jeśli błąd jest mniejszy niż zadana tolerancja, krok jest akceptowany 
i można krok <i>wydłużyć</i>; jeśli błąd przekracza tolerancję, krok 
jest <i>odrzucany</i>, a metoda automatycznie <i>zmniejsza</i> krok czasowy.
</p>

<p><b>Zastosowanie.</b>
Metoda Dormanda–Prince’a jest jednym z najczęściej stosowanych 
schematów adaptacyjnych w praktycznych solverach ODE 
(rodzina metod spokrewnionych z popularnym „ode45” w MATLAB-ie). 
W porównaniu z RKF45, DP5 kładzie większy nacisk na to, aby 
główne rozwiązanie rzędu 5 miało jak najmniejszy błąd globalny, 
co często przekłada się na lepszą jakość trajektorii przy podobnej 
liczbie kroków. Dzięki adaptacyjnemu doborowi kroku czasowego 
metoda dobrze sprawdza się przy wizualizacji złożonych trajektorii 
atraktorów, takich jak Lorenz czy Rössler, gdzie gęstość próbkowania 
musi automatycznie dostosowywać się do lokalnej dynamiki.
</p>


<p><b>Implementacja.</b>  
W dodatku Attractor Builder każdy krok metody Dormanda–Prince’a 5(4) 
realizuje funkcja  
<code>step_dp5(rhs_func, p: Vector, params: dict, current_dt: float, tolerance: float)</code>.  
Metoda DP5, podobnie jak RKF45, wykorzystuje tzw. tablice Butchera — układ współczynników 
określających przesunięcia czasowe (macierz \( A \)) oraz wagi kombinacji liniowych 
(\( B \), \( B^* \)), 
z których otrzymywane są dwa przybliżenia rozwiązania: 
rząd 5 (główny) oraz wbudowany rząd 4.  
Pełną tablicę współczynników metody Dormanda–Prince’a 5(4) można znaleźć w  
(Hairer, Nørsett, Wanner 1993, Table&nbsp;5.2, s.&nbsp;178), natomiast ogólną definicję 
tablic Butchera opisano w Butcher (2008, rozdz.&nbsp;5, s.&nbsp;96).
Pierwszym etapem jest obliczenie wektorów nachyleń  
\( \mathbf{k}_1, \dots, \mathbf{k}_6 \) zgodnie z macierzą \( A \):
<code>
k1 = rhs_func(p, params)
k2 = rhs_func(p + current_dt * A[1][0] * k1, params)
k3 = rhs_func(p + current_dt * (A[2][0]*k1 + A[2][1]*k2), params)
k4 = rhs_func(p + current_dt * (A[3][0]*k1 + A[3][1]*k2 + A[3][2]*k3), params)
k5 = rhs_func(p + current_dt * (A[4][0]*k1 + A[4][1]*k2 + A[4][2]*k3 + A[4][3]*k4), params)
k6 = rhs_func(p + current_dt * (A[5][0]*k1 + A[5][1]*k2 + A[5][2]*k3 + A[5][3]*k4 + A[5][4]*k5), params)
</code>
Następnie z użyciem wag \( B \) wyznaczane jest przybliżenie rzędu 5:
<code>
y5 = p + current_dt * (B[0]*k1 + B[1]*k2 + B[2]*k3 + B[3]*k4 + B[4]*k5 + B[5]*k6)
</code>
Dodatkowo obliczane jest nachylenie  
<code>k7 = rhs_func(y5, params)</code>,  
wykorzystywane do estymaty błędu przy użyciu wag \( B^* \).  
Wektor błędu lokalnego ma postać:
<code>
all_k = [k1, k2, k3, k4, k5, k6, k7]
error_vec = current_dt * sum([(b - bs) * k for b, bs, k in zip(B, B_star, all_k)], Vector())
error = error_vec.length
</code>
co odpowiada różnicy pomiędzy głównym rozwiązaniem rzędu 5 a wbudowanym 
rozwiązaniem rzędu 4. Na tej podstawie obliczany jest optymalny krok czasowy:
<code>
optimal_dt = 0.9 * current_dt * (tolerance / error)**0.2
</code>

Jeżeli <code>error &lt;= tolerance</code>, krok jest akceptowany (nowy punkt 
trajektorii to <code>y5</code>). Jeśli błąd jest zbyt duży, krok zostaje odrzucony 
i wykonywana jest ponowna próba z krokiem <code>optimal_dt</code>.  
Podobnie jak w przypadku RKF45, funkcja <code>step_dp5</code> zwraca trójkę:  
<code>(nowy_punkt, proponowany_krok_dt, flaga_akceptacji)</code>.
</p>

Przykładem zastosowania może być układ Lorenza:
<pre class="eq-plain">
<b>Równania:</b>
dx/dt = a * (y - x)
dy/dt = x * (b - z) - y
dz/dt = x * y - c * z
<b>Parametry:</b>
| a = 10 | b = 28 | c = 8/3 |
<b>Ustawienia symulacji:</b>
Stan początkowy: x₀ = 0.01, y₀ = 0.01, z₀ = 0.01
Metoda: DP5
Tolerancja: 0.000001
min_dt: 0.000001
max_dt: 0.05
Zapisane kroki: 3
Burn-in: 1000
Skala: 1
</pre>
<p>
Korzystając z funkcji Raw Data → Export w dodatku Attractor Builder 
otrzymujemy surowe dane w formacie CSV z kolumnami 
<code>steps</code>, <code>dt</code>, <code>x</code>, <code>y</code>, <code>z</code>. 
Dla powyższych ustawień pierwsze cztery wiersze pliku CSV wyglądają następująco:
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
<tr><td>2</td><td>0.02895</td><td>0.01184</td><td>0.02099</td><td>0.00902</td></tr>
<tr><td>3</td><td>0.02933</td><td>0.01549</td><td>0.03131</td><td>0.00835</td></tr>
</tbody>
</table>

<p>
Pierwszy wiersz odpowiada warunkowi początkowemu 
\( (x_0, y_0, z_0) = (0.01, 0.01, 0.01) \) i ma przypisany czasowy krok 
\( dt = 0 \). W kolejnych wierszach widać, jak metoda Dormanda–Prince’a 
adaptuje krok czasowy: po pierwszym kroku <code>dt</code> rośnie z 0.01 
do około 0.029 (3 krok), co oznacza, że w tym fragmencie trajektorii ruch jest na tyle 
regularny, że można używać większego kroku bez utraty zadanej dokładności. 
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