---
layout: addon
lang: pl
permalink: /pl/addon/
title:
alt_url: /en/addon/
---


<em>Dodatek **Attractor Builder** został opracowany jako narzędzie umożliwiające 
numeryczną integrację układów równań różniczkowych i generowanie ich trajektorii 
bezpośrednio w środowisku **Blender 4.5+**. Pozwala wykonywać własne eksperymenty, 
wizualizować atraktory, eksportować dane, a także tworzyć animowane formy w pełnym 3D.
Dodatek jest darmowy i przeznaczony zarówno dla osób badających układy dynamiczne, 
jak i twórców wykorzystujących atraktory w grafice, animacji lub sztuce generatywnej.</em>

<p style="text-align:center; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/intro.png' | relative_url }}"
       alt="Attractor Builder — panel location"
       style="width:100%; max-width:100%; border-radius: 10px;
              box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
</p>


---


<p>
<b>Instalacja</b><br>

1. Pobierz plik  <a href="https://github.com/pcabala/AttractorBuilder/releases/latest/download/attractor_builder.zip"
      style="display:inline-flex;"> attractor_builder.zip</a>
	  z repozytorium GitHub.<br>
2. W Blenderze otwórz: Edit → Preferences → Add-ons.<br>
3. Kliknij <i>Install…</i> i wybierz pobrany plik <code>.zip</code>.<br>
4. Aktywuj dodatek i upewnij się, że znajduje się na liście.<br>
5. Panel dodatku pojawi się w zakładce N-panel → Attractors:<br>
</p>

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/n_panel.png' | relative_url }}"
       alt="N-panel with Attractor Builder"
       style="display:block; border-radius: 10px; width:auto; max-width:100%; height:auto;">
</p>

---

<p><b>Interfejs</b><br>

Zakładka <em>Default</em> korzysta z wbudowanej biblioteki układów (Lorenz, Chen, Lü itd.) 
wraz z gotowymi parametrami startowymi. Zakładka <em>Custom</em> jest przeznaczona 
do definiowania własnych równań i parametrów.


<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/mode_default.png' | relative_url }}"
       alt="Attractor Builder – Default interface"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>


<p><b>Default Library.</b>
Lista rozwijana zawiera zestaw zdefiniowanych atraktorów. 
Po wybraniu systemu poniżej automatycznie pojawia się jego zapis 
w postaci równań oraz domyślny zestaw parametrów.
<em>Equations</em>: równania różniczkowe wybranego układu, zapisane w postaci trzech wyrażeń
określających pochodne <em>ẋ</em>, <em>ẏ</em> i <em>ż</em>.  
Dla zachowania bezpieczeństwa i spójności z modułem <em>Custom</em> 
można używać wyłącznie zmiennych <code>x</code>, <code>y</code>, <code>z</code> 
oraz funkcji matematycznych: <code>sin</code>, <code>cos</code>, <code>tan</code>,
<code>asin</code>, <code>acos</code>, <code>atan</code>, <code>sinh</code>, <code>cosh</code>,
<code>tanh</code>, <code>exp</code>, <code>log</code>, <code>sqrt</code>, <code>pow</code>, <code>fabs</code>.  
Dozwolone są standardowe operatory arytmetyczne i unarne 
(<code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>**</code>, <code>%</code>, 
oraz unarne <code>-</code> i <code>+</code> przy liczbach). 
<em>Parameters</em>: lista parametrów (np. <em>a</em>, <em>b</em>, <em>c</em> dla Lorenza) 
wraz z ich wartościami, które można edytować, wpływając bezpośrednio na kształt generowanej trajektorii. 
Przycisk <em>Tips</em> odsyła do krótkich wskazówek, a <em>Copy</em> 
przenosi układ równań wraz z bieżącymi parametrami do modułu <em>Custom</em>, 
umożliwiając ich dalszą edycję i tworzenie własnych systemów.</p>

<p> <b>Simulation Settings.</b>
Blok ustawień symulacji: stan początkowy, metoda integracji oraz odpowiadające jej parametry.
<em>Initial conditions:</em>
Współrzędne początkowe punktu: <em>x₀</em>, <em>y₀</em>, <em>z₀</em>. 
Od nich rozpoczyna się numeryczna integracja trajektorii.

<em>Integration Method.</em>
Lista rozwijana z wyborem metody numerycznej (Euler, Heun, RK4, RKF45, DP5): 

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/integration_methods.png' | relative_url }}"
       alt="Attractor Builder – Integration methods"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>

<p><b>Fixed dt.</b> Dla metod o stałym kroku (Euler, Heun, RK4) dostępne są pola 
umożliwiające ustawienie: długości kroku czasowego <em>Time Step (dt)</em>, 
liczby kroków integracji <em>Steps</em>, długości fazy rozgrzewki <em>Burn-in</em> 
oraz współczynnika skalowania <em>Scale</em>.</p> 

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/fixed_dt.png' | relative_url }}"
       alt="Attractor Builder – Fixed dt"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>
 

<p><b>Adaptive dt.</b> Obejmuje dwie metody adaptacyjne (RKF45 oraz DP5), w których użytkownik 
nie określa stałego kroku czasowego. Zamiast tego algorytm dobiera <em>dt</em> automatycznie 
na podstawie tolerancji błędu <em>Tolerance</em> oraz podanego zakresu dopuszczalnych 
wartości <em>Min Step</em> i <em>Max Step</em>.</p>

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/adaptive_dt.png' | relative_url }}"
       alt="Attractor Builder – Adaptive dt"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>

<p><b>Output.</b>
Przycisk <em>Build Attractor</em> generuje trajektorię w postaci obiektu typu 
<em>Curve</em> (dokładnie: <em>Poly Curve</em>) o nazwie podanej w polu 
<em>Output Name</em> — domyślnie <code>Attractor</code>. 
Dopiero po wygenerowaniu atraktora dostępna staje się sekcja <em>Raw data</em>. 
Przycisk <em>Points</em> tworzy obiekt typu <em>Mesh</em> o nazwie <code>RawPoints</code>, 
umożliwiający podgląd wszystkich wygenerowanych punktów. 
Przycisk <em>Export</em> zapisuje te dane do pliku CSV, co pozwala na dalszą analizę wyników 
symulacji w Pythonie, MATLAB-ie lub Excelu. Plik CSV zawiera kolumny 
<code>steps</code>, <code>dt</code>, <code>x</code>, <code>y</code>, <code>z</code>. 
Pierwszy wiersz odpowiada warunkom początkowym wprowadzonym przez 
użytkownika w sekcji <em>Initial conditions</em>, a pozostałe wiersze 
zawierają współrzędne punktów trajektorii uzyskane w kolejnych krokach integracji. 
Informacja o <code>dt</code> ma szczególne znaczenie w metodach adaptacyjnych, w których 
krok czasowy jest wyznaczany przez algorytm.</p>


<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/output.png' | relative_url }}"
       alt="Attractor Builder – Output section"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>

<p><b>Post-Processing Tools.</b> 
Sekcja ta pojawia się dopiero po wygenerowaniu atraktora i umożliwia prostą
 obróbkę uzyskanej krzywej. Narzędzie <em>Trim</em> pozwala skrócić 
trajektorię, usuwając jej początkową lub końcową część poprzez ustawienie zakresu 
<em>Start</em> i <em>End</em>; po zatwierdzeniu przyciskiem <em>Apply Trim</em> obiekt zostaje 
trwale zaktualizowany. Funkcja <em>Simplify</em> umożliwia redukcję liczby punktów 
krzywej typu <em>Poly Curve</em>, co zmniejsza złożoność obiektu i ułatwia dalszą pracę; 
działa ona niezależnie od operacji przycinania. Z kolei narzędzie <em>Smooth to Bezier</em> 
konwertuje krzywą poli-liniową na krzywą Béziera, wykorzystując wbudowany algorytm 
wygładzający, a jego intensywność kontrolowana jest parametrem <em>Fidelity</em>. 
Wszystkie trzy operacje pozwalają szybko przygotować trajektorię do dalszej edycji, 
animacji lub renderingu.</p>

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/post_processing.png' | relative_url }}"
       alt="Attractor Builder – Post processing tools"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>

<p><b>Custom.</b> 
Ten tryb umożliwia definiowanie i zapisywanie własnych układów równań różniczkowych, 
które następnie można integrować i wizualizować tak samo jak systemy z biblioteki wbudowanej. 
Sekcja ta jest przeznaczona dla użytkowników chcących eksperymentować z własnymi modelami, 
modyfikować istniejące układy lub dokumentować różne warianty parametrów.</p>

<p style="text-align:left; margin: 1.4em 0;">
  <img src="{{ '/assets/media/addon/mode_custom.png' | relative_url }}"
       alt="Attractor Builder – Custom mode"
       style="display:block; width:auto; max-width:100%; height:auto;
              border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.08);">
</p>

<p><b>Custom Library.</b> 
Lista rozwijana wyświetlająca zapisane wcześniej układy wraz z ich parametrami. 
Elementy pojawiają się w kolejności od najnowszych, dzięki czemu łatwo wrócić do ostatnio edytowanych modeli. 
Wprowadzając własne równania, należy pamiętać, że parser akceptuje wyłącznie bezpieczny podzbiór wyrażeń: 
zmienne <code>x</code>, <code>y</code>, <code>z</code>; funkcje matematyczne 
<code>sin</code>, <code>cos</code>, <code>tan</code>, <code>asin</code>, <code>acos</code>, <code>atan</code>, 
<code>sinh</code>, <code>cosh</code>, <code>tanh</code>, <code>exp</code>, <code>log</code>, <code>sqrt</code>, 
<code>pow</code>, <code>fabs</code>; oraz standardowe operatory arytmetyczne: 
<code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>**</code>, <code>%</code>, 
a także unarne <code>+</code> i <code>-</code>. Użycie innych struktur składni 
spowoduje odrzucenie równania.</p>

<p>
<b>Detect Parameters.</b>  
Przycisk ten analizuje wprowadzone równania, wykrywa wszystkie występujące 
w nich symbole (z wyłączeniem <code>x</code>, <code>y</code>, <code>z</code>) i na ich podstawie tworzy listę parametrów. 
Jest to krok niezbędny — bez wykrycia parametrów i poprawnej struktury równań 
nie jest możliwe przeprowadzenie symulacji.  
Po pomyślnej detekcji parametry wyświetlane są w tabeli poniżej, gdzie można nadać im wartości 
początkowe, tak jak w trybie <em>Default</em>.</p>


<p><b>Save/Notes/Edit/Delete.</b>  
Po wykryciu parametrów układ można zapisać pod dowolną nazwą, co dodaje go do listy 
<em>Custom Library</em>. Wszystkie zapisane systemy przechowywane są w jednym pliku 
<code>.json</code> wewnątrz dodatku, dzięki czemu pozostają dostępne między sesjami Blendera.
Do każdego zapisanego układu można przypisać własne notatki, np. opis pochodzenia systemu, 
uwagi dotyczące stabilności, typowe wartości parametrów czy wyniki eksperymentów numerycznych. 
Przyciski <em>Note</em> oraz <em>Edit</em> umożliwiają odpowiednio przeglądanie i edytowanie notatek, 
natomiast <em>Delete</em> usuwa cały zapisany system wraz z odpowiadającym mu wpisem w pliku JSON.</p>
