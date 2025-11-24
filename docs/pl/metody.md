---
layout: methods
lang: pl
permalink: /pl/metody/
title:
alt_url: /en/methods/
---



<p>
<b>Metody numeryczne</b> pozwalają określić, jak zmienia się położenie punktu w przestrzeni w zależności od czasu. 
Trajektoria systemu powstaje poprzez przybliżanie kolejnych położeń tego punktu, 
a położenia te opisuje układ równań różniczkowych (ang. <i>ordinary differential equations</i>, ODE).
</p>

<p>
Układ równań różniczkowych ma postać \( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \), 
gdzie \( \mathbf{x} \) jest wektorem stanu (np. \( (x, y, z) \)), a funkcja \( f \) 
wyznacza kierunek i szybkość ruchu punktu w danej chwili czasu. 
Ten sam układ zapisuje się także jako 
\( \tfrac{d\mathbf{x}}{dt} = f(\mathbf{x}, t, \theta) \) lub 
\( \mathbf{x}' = f(\mathbf{x}, t, \theta) \). 
Wskazuje on, że położenie punktu nie jest dane z góry — układ określa jedynie 
jego <em>natychmiastową zmianę</em>. W wyznaczaniu trajektorii systemu zaczynamy 
od punktu początkowego \( \mathbf{x}_0 \) i śledzimy jego ruch zgodnie z tą regułą.
</p>

<p>
Rozwiązaniem układu \( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \) jest funkcja
opisująca ruch punktu: \( t \mapsto \mathbf{x}(t) \). Aby ją przybliżyć, wybieramy 
krok czasowy \( \Delta t \) i konstruujemy ciąg punktów 
\( \mathbf{x}_0, \mathbf{x}_1, \mathbf{x}_2, \ldots \), które odpowiadają chwilom 
\( t_0, t_0 + \Delta t, t_0 + 2\,\Delta t, \ldots \). 
Każda metoda numeryczna określa regułę przejścia 
\( \mathbf{x}_n \mapsto \mathbf{x}_{n+1} \). Różnią się one sposobem wyznaczania kolejnego punktu 
\( \mathbf{x}_{n+1} \) na podstawie informacji o pochodnych. 
Metody stosowane w praktyce można podzielić na dwie grupy — 
metody o stałym kroku czasowym oraz metody adaptacyjne.
</p>

<p><b>Przykład.</b> W układach trójwymiarowych punkt w przestrzeni opisuje się 
trójką liczb \( (x, y, z) \). Sytem Lorenza jest szczególnym 
przypadkiem ogólnego zapisu 
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \). 
Wektor stanu ma tutaj postać \( \mathbf{x} = (x, y, z) \), 
a funkcja \( f \) określa wartości trzech pochodnych 
\( (\dot{x}, \dot{y}, \dot{z}) \) w zależności od bieżącego położenia punktu. 
Wypisanie równań współrzędnych daje układ: \( \dot{x} = \sigma (y - x) \),
\( \dot{y} = \sigma (y - x) \), \( \dot{z} = x y - \beta z \).
W każdej chwili czasu układ ten określa natychmiastową zmianę położenia punktu 
na podstawie jego bieżącego stanu \( (x, y, z) \). Aby uzyskać trajektorię, 
stosuje się metody numeryczne, które przybliżają kolejne położenia punktu 
po upływie kroków czasowych \( \Delta t \). Podsumowując, aby obliczyć trajektorię układu
\( \dot{\mathbf{x}} = f(\mathbf{x}, t, \theta) \), zaczynamy od położenia początkowego 
\( \mathbf{x}_0 \). W tym punkcie obliczamy pochodną 
\( f(\mathbf{x}_0, t_0, \theta) \), która określa natychmiastową zmianę 
wszystkich współrzędnych.
Znając krok czasowy \( \Delta t \), możemy wyznaczyć przybliżone położenie punktu
po upływie jednej jednostki czasu numerycznego, czyli punkt 
\( \mathbf{x}_1 \). Następnie obliczamy pochodną w nowym punkcie 
i powtarzamy procedurę, uzyskując kolejne przybliżenia 
\( \mathbf{x}_2, \mathbf{x}_3, \ldots \).</p>



<p>
<b>Metody o stałym kroku czasowym</b> korzystają z niezmiennej wartości \( \Delta t \); 
po każdym kroku czasowym przesuwają punkt o tę samą długość odcinka czasu, 
niezależnie od tego, jak szybko zmienia się dynamika układu. 
Do metod o stałym kroku należą:<br>
<a href="/pl/metody/euler/">metoda Eulera</a>,<br>
<a href="/pl/metody/heun/">metoda Heuna</a>,<br>
<a href="/pl/metody/rk4/">metoda Rungego–Kutty</a>.
</p>

<p>
<b>Metody adaptacyjne</b> samodzielnie dostosowują wartość \( \Delta t \) 
w zależności od dynamiki układu; zmniejszają krok, gdy rozwiązanie zmienia się szybko, 
i zwiększają, gdy zmiany są łagodniejsze. Wykorzystują przy tym dodatkowe 
oszacowania błędu, aby kontrolować dokładność obliczeń. 
Do metod adaptacyjnych należą:<br>
<a href="/pl/metody/rkf45/">metoda RKF45</a>,<br>
<a href="/pl/metody/dp5/">metoda Dormanda–Prince'a</a>.
</p>

<br>
<p><b>Źródła:</b></p>

<p class="hanging-indent">
Atkinson, K. (1989). <i>An Introduction to Numerical Analysis</i>. Wiley.
</p>

<p class="hanging-indent">
Butcher, J. C. (2008). <i>Numerical Methods for Ordinary Differential Equations</i>.
Wiley.
</p>

<p class="hanging-indent">
Hairer, E., Nørsett, S., Wanner, G. (1993). 
<i>Solving Ordinary Differential Equations I</i>. Springer.
</p>

<p class="hanging-indent">
Sundnes, J. (2024). <i>Solving Ordinary Differential Equations in Python</i>. 
Simula SpringerBriefs on Computing. Springer.
</p>

