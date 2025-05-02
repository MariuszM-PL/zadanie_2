import re
import math
from datetime import datetime

def is_valid_email(email: str) -> bool:
    """
    Sprawdza, czy podany adres e-mail ma poprawny format.

    :param email: Adres e-mail w formie tekstowej.
    :return: True jeśli e-mail jest poprawny, False w przeciwnym razie.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def calculate_circle_area(radius: float) -> float:
    """
    Oblicza pole koła na podstawie podanego promienia.

    :param radius: Promień koła (musi być >= 0).
    :return: Pole koła.
    :raises ValueError: Gdy promień jest ujemny.
    """
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    return math.pi * radius ** 2

def convert_date(date_str: str) -> str:
    """
    Konwertuje datę z formatu 'YYYY-MM-DD' na 'DD/MM/YYYY'.

    :param date_str: Data w formacie 'YYYY-MM-DD'.
    :return: Data w formacie 'DD/MM/YYYY'.
    :raises ValueError: Jeśli data ma niepoprawny format.
    """
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Niepoprawny format daty. Oczekiwano YYYY-MM-DD.")

def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy dany tekst jest palindromem (ignorując spacje, znaki i wielkość liter).

    :param text: Tekst do sprawdzenia.
    :return: True jeśli tekst jest palindromem, False w przeciwnym razie.
    """
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Zwraca listę zawierającą tylko liczby parzyste z podanej listy.

    :param numbers: Lista liczb całkowitych.
    :return: Lista liczb parzystych.
    """
    return [n for n in numbers if n % 2 == 0]
