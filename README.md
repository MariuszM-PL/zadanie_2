# ✅ Zadanie 2 – Testowanie aplikacji w Pythonie (TDD + unittest)

## 🎯 Cel zadania

 1. Zapoznanie się z podstawami testowania aplikacji w Pythonie.
 2. Nauka podejścia Test-Driven Development (TDD).
 3. Implementacja testów jednostkowych z wykorzystaniem modułu unittest.
 4. Wykorzystanie testów do poprawy jakości kodu.
 5. Zapoznanie się z narzędziami do analizy pokrycia testowego.

---

## 📁 Struktura projektu

```
zadanie_2/
├── app.py             # Plik z funkcjami
├── test_app.py        # Plik z testami jednostkowymi
├── requirements.txt   # Zależności (opcjonalnie)
├── htmlcov/           # Folder z raportem HTML z coverage (tworzony automatycznie)
└── README.md          # Ten plik
```

---

## 🧠 Zaimplementowane funkcje (`app.py`)

1. `is_valid_email(email: str) -> bool`  
   Sprawdza, czy podany adres e-mail ma poprawny format.

2. `calculate_circle_area(radius: float) -> float`  
   Oblicza pole koła ze wzoru πr². Zgłasza wyjątek przy wartości ujemnej.

3. `convert_date(date_str: str) -> str`  
   Konwertuje datę z formatu `YYYY-MM-DD` na `DD/MM/YYYY`. Obsługuje wyjątki.

4. `is_palindrome(text: str) -> bool`  
   Sprawdza, czy tekst jest palindromem (ignorując spacje i wielkość liter).

5. `filter_even_numbers(numbers: list[int]) -> list[int]`  
   Zwraca nową listę zawierającą tylko liczby parzyste.

---

## 🧪 Uruchamianie testów

W katalogu projektu uruchom:

```bash
python -m unittest test_app.py
```

---

## 📊 Analiza pokrycia kodu (`coverage.py`)

### 1. Instalacja (jeśli nie masz):

```bash
pip install coverage
```

### 2. Uruchomienie testów z pomiarem pokrycia:

```bash
python -m coverage run -m unittest test_app.py
```

### 3. Wyświetlenie raportu w terminalu:

```bash
python -m coverage report -m
```
