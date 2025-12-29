"""
Moduł do przetwarzania danych.
"""

import re
from datetime import datetime

def validate_email(email: str) -> bool:
    """
    Walidacja adresu email.
    
    Args:
        email: Adres email do walidacji
        
    Returns:
        True jeśli email jest poprawny
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def format_date(date_string: str) -> str:
    """
    Formatuje datę z YYYY-MM-DD na DD.MM.YYYY.
    
    Args:
        date_string: Data jako string w formacie YYYY-MM-DD
        
    Returns:
        Sformatowana data jako string
    """
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Nieprawidłowa data"