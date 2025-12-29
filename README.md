# Python-intro
Zadania z Pythona na zajęcia ze studiów

Task_1

Task_2
Coverage został użyty, ale niestety nie pokazuję testów, ponieważ Jupyter ma z tym problemy bez dodatkowej konfiguracji.
<br>Można by to prosto rozwiązać po prostu dzieląc ten plik na 2 .py i odpalić coverage z basha

Task_3
bibliotek/
<br>├── data_utils.py        # Moduł 1
<br>├── math_tools.py        # Moduł 2
<br>├── text_processing.py   # Moduł 3
<br>└── tests/
<br>    └── test_all.py      # Wszystkie testy w jednym pliku

Prosta biblioteka w Pythonie z funkcjami do:
- Przetwarzania danych (walidacja email, formatowanie dat)
- Obliczeń matematycznych (statystyka, korelacja)
- Przetwarzania tekstu (analiza, oczyszczanie)

## Użycie
<br>from data_utils import validate_email
<br>from math_tools import Statistics
<br>from text_processing import TextAnalyzer

print(validate_email("test@example.com"))
