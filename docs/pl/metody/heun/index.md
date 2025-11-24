---
layout: methods
lang: pl
title: Metoda Heuna
permalink: /pl/metody/heun/
alt_url: /en/methods/heun/
---

<p><b>Istota.</b> Metoda Heuna jest prostym ulepszeniem metody Eulera. 
Zamiast opierać się wyłącznie na pochodnej w punkcie początkowym 
\( \mathbf{x}_n \), wykorzystuje <i>średnie</i> nachylenie na początku 
i na końcu kroku czasowego \( \Delta t \). Dla układu 
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \) 
metoda wykonuje najpierw krok Eulera (tzw. predyktor):
 \( \mathbf{x}_{n+1}^{(p)} = \mathbf{x}_n + \Delta t\, f(\mathbf{x}_n) \), a następnie koryguje 
wynik (korektor):
\( \mathbf{x}_{n+1} = \mathbf{x}_n + \tfrac{\Delta t}{2}\big[ f(\mathbf{x}_n) + f(\mathbf{x}_{n+1}^{(p)}) \big] \).
Zamiast przyjmować stałe nachylenie na całym przedziale (jak w metodzie Eulera), 
metoda Heuna uśrednia nachylenie z początku i końca kroku. 
Dzięki temu błąd globalny jest niższy niż w metodzie Eulera, 
przy stosunkowo niewielkim koszcie obliczeniowym.
</p>

<p><b>Przykład.</b> Dla równania 
\( \dot{x} = -2x \) z warunkiem początkowym \( x_0 = 1 \) 
i krokiem czasowym \( \Delta t = 0.1 \). 
W każdym kroku wykonujemy dwa etapy: predyktor i korektor.<p> 

<i>Krok 1</i> (od \( x_0 \) do \( x_1 \)).
Pochodna w punkcie \( x_0 = 1 \): 
\( f(x_0) = -2 \cdot 1 = -2 \), (predyktor), 
przybliżenie: 
\( x_{1}^{(p)} = x_0 + 0.1 \cdot (-2) = 0.8 \),
pochodna w punkcie przewidywanym \( x_{1}^{(p)} = 0.8 \),
\( f(x_{1}^{(p)}) = -2 \cdot 0.8 = -1.6 \). 
Nowe przybliżenie (średnia z dwóch nachyleń):
\( x_1 = x_0 + \tfrac{0.1}{2}\big[ f(x_0) + f(x_{1}^{(p)}) \big] 
= 1 + 0.05 \cdot (-2 - 1.6) = 0.82. \)
</p>

<p>
<i>Krok 2</i> (od \( x_1 \) do \( x_2 \)).
Predyktor: \( f(x_1) = -2 \cdot 0.82 = -1.64 \), \( x_{2}^{(p)} = 0.82 + 0.1 \cdot (-1.64) = 0.656 \).
Korektor: \( f(x_{2}^{(p)}) = -2 \cdot 0.656 = -1.312 \),
\( x_2 = 0.82 + 0.05 \cdot (-1.64 - 1.312) \approx 0.6724. \)
</p>

<p>
W kolejnych krokach postępujemy identycznie: na początku kroku liczymy 
pochodną w \( x_n \), wykonujemy krok Eulera do punktu \( x_{n+1}^{(p)} \), 
a następnie korygujemy wynik, uśredniając pochodne w obu punktach. 
W porównaniu z metodą Eulera wartości \( x_n \) są bliższe rozwiązaniu 
dokładnemu, nawet przy takim samym kroku \( \Delta t \).
</p>

<p><b>Zastosowanie.</b> 
Metoda Heuna stanowi dobry kompromis między prostotą a dokładnością. 
Pozwala zachować większą stabilność i lepszy kształt trajektorii 
niż Euler, zwłaszcza przy umiarkowanych krokach czasowych. 
W układach chaotycznych nadal musimy uważać na wybór 
\( \Delta t \), ale dla wielu atraktorów metoda Heuna daje 
wyraźnie „czystsze” trajektorie niż Euler przy tym samym kroku.
W praktyce metodę Heuna warto stosować, gdy
metoda Eulera daje zbyt duże zniekształcenia trajektorii lub 
gdy chcemy szybko poprawić jakość integracji bez przechodzenia 
od razu do metod wyższego rzędu (np. RK4, Dormand–Prince).
</p>

<p><b>Implementacja.</b> W dodatku Attractor Builder każdy krok metody Heuna 
realizuje funkcja <code>step_heun</code>. W przeciwieństwie do metody Eulera, 
która korzysta tylko z pochodnej w punkcie bieżącym, metoda Heuna oblicza 
pochodną dwukrotnie: w punkcie bieżącym oraz w punkcie przewidywanym 
(predyktorze). Kod w dodatku ma postać:
<code>
def step_heun(rhs_func, p: Vector, params: dict, dt: float):
    p_pred = p + rhs_func(p, params) * dt
    avg_slope = 0.5 * (rhs_func(p, params) + rhs_func(p_pred, params))
    return p + avg_slope * dt
</code>
<p>
Algorytm przebiega więc następująco:
1. Obliczamy pochodną w punkcie bieżącym \( p \): 
\( f(p) = rhs\_func(p, params) \).
2. Wykonujemy krok predyktora (Euler): 
\( p^{(p)} = p + \Delta t \, f(p) \).
3. Obliczamy pochodną w punkcie przewidywanym \( p^{(p)} \): 
\( f(p^{(p)}) \).
4. Uśredniamy nachylenie: 
\( \tfrac{1}{2}[ f(p) + f(p^{(p)}) ] \).
5. Obliczamy nowy punkt: 
\( p_{n+1} = p + \Delta t \cdot \tfrac{1}{2}[ f(p) + f(p^{(p)}) ]. \)
Na przykład, gdy w Attractor Builder przyjmiemy (Lorenz):
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
Metoda: Heun
Krok czasowy (dt): 0.01
Liczba kroków: 3
Faza rozgrzewki (burn-in): 0
Skala: 1
</pre>

<pre class="eq-plain">
<b>Krok 1.</b> Punkt początkowy: x0 = 0.01; y0 = 0.01; z0 = 0.01.
Pochodne:
dx0 = 10*(y0-x0) = 10*(0.01-0.01) = 0
dy0 = x0*(28-z0) - y0 = 0.01*(28-0.01) - 0.01 = 0.2699
dz0 = x0*y0 - (8/3)*z0 ≈ 0.0001 - 0.02667 ≈ -0.02657
Predyktor (Euler):
x_pred = x0 + 0.01*dx0 = 0.01
y_pred = y0 + 0.01*dy0 = 0.01 + 0.01*0.2699 ≈ 0.01270
z_pred = z0 + 0.01*dz0 ≈ 0.01 + 0.01*(-0.02657) ≈ 0.00973
Pochodne w punkcie przewidywanym (zaokrąglone):
dxp = 10*(y_pred - x_pred) ≈ 10*(0.01270-0.01) ≈ 0.0270
dyp = x_pred*(28-z_pred) - y_pred ≈ 0.2672
dzp ≈ -0.0258
Średnie nachylenie:
dx_avg ≈ (dx0 + dxp)/2 ≈ 0.0135
dy_avg ≈ (dy0 + dyp)/2 ≈ 0.2686
dz_avg ≈ (dz0 + dzp)/2 ≈ -0.0262
Nowy punkt (po 1. kroku Heuna):
x1 = x0 + 0.01*dx_avg ≈ 0.0101349
y1 = y0 + 0.01*dy_avg ≈ 0.0126855
z1 = z0 + 0.01*dz_avg ≈ 0.0097380
<b>Krok 2.</b> Punkt wyjściowy: x1 ≈ 0.0101349; y1 ≈ 0.0126855; z1 ≈ 0.0097380.
[analogicznie obliczamy predyktor, pochodne i średnie nachylenie]
Nowy punkt:
x2 ≈ 0.0105128
y2 ≈ 0.0154176
z2 ≈ 0.0094832
<b>Krok 3.</b> Punkt wyjściowy: x2 ≈ 0.0105128; y2 ≈ 0.0154176; z2 ≈ 0.0094832.
Po wykonaniu predyktora i korektora Heuna otrzymujemy:
x3 ≈ 0.0111181
y3 ≈ 0.0182607
z3 ≈ 0.0092354
</pre>

<p>
W każdym kroku algorytm najpierw liczy wektor pochodnych w bieżącym punkcie 
(predyktor, odpowiednik Eulera), a następnie liczy go ponownie w punkcie 
przewidywanym i uśrednia oba nachylenia. 
Dzięki temu trajektoria lepiej oddaje prawdziwy kształt atraktora 
niż przy zastosowaniu prostej metody Eulera z tym samym krokiem 
\( \Delta t \).
</p>
