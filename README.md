# Python-intro
Zadania z Pythona na zajęcia ze studiów

Task_1

Task_2
Coverage został użyty, ale niestety nie pokazuję testów, ponieważ Jupyter ma z tym problemy bez dodatkowej konfiguracji.
Można by to prosto rozwiązać po prostu dzieląc ten plik na 2 .py i odpalić coverage z basha

Task_3
bibliotek/
├── data_utils.py        # Moduł 1
├── math_tools.py        # Moduł 2
├── text_processing.py   # Moduł 3
└── tests/
    └── test_all.py      # Wszystkie testy w jednym pliku

Prosta biblioteka w Pythonie z funkcjami do:
- Przetwarzania danych (walidacja email, formatowanie dat)
- Obliczeń matematycznych (statystyka, korelacja)
- Przetwarzania tekstu (analiza, oczyszczanie)

## Użycie
from data_utils import validate_email
from math_tools import Statistics
from text_processing import TextAnalyzer

print(validate_email("test@example.com"))
