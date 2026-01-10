# Raport – Laboratorium 4 (pymcdm)

## Cel
Celem ćwiczenia było zastosowanie metod wielokryterialnego podejmowania
decyzji z wykorzystaniem biblioteki `pymcdm`.

## Dane
Analizie poddano cztery alternatywy (A1–A4) oraz trzy kryteria:
- koszt (min),
- jakość (max),
- czas realizacji (min).

Macierz decyzyjna została wcześniej znormalizowana metodą min–max.

## Metody
W analizie wykorzystano metody:
- **TOPSIS** – do oceny znormalizowanej macierzy decyzyjnej,
- **SPOTIS** – do oceny danych przed normalizacją przy użyciu granic kryteriów.

## Wyniki i wnioski

Wagi kryteriów:
C1: 0.4237
C2: 0.2985
C3: 0.2778

=== Wyniki TOPSIS ===<br>
A1: 0.7218<br>
A2: 0.3707<br>
A3: 0.5055<br>
A4: 0.5440<br>
<br>
=== Wyniki SPOTIS ===<br>
A1: 0.1990<br>
A2: 0.7015<br>
A3: 0.4965<br>
A4: 0.4758<br>
<br>
Ranking TOPSIS:<br>
1. A1<br>
2. A4<br>
3. A3<br>
4. A2<br>
<br>
Ranking SPOTIS:<br>
1. A1<br>
2. A4<br>
3. A3<br>
4. A2<br>

Dla obu metod wyznaczono rankingi alternatyw. Analiza umożliwiła wybór
najlepszej alternatywy z uwzględnieniem wielu kryteriów jednocześnie.
Różnice w rankingach wynikają z odmiennych zasad działania metod
TOPSIS i SPOTIS.
