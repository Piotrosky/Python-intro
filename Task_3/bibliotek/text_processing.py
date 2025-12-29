"""
Moduł do przetwarzania tekstu.
"""

import re
from collections import Counter

class TextAnalyzer:
    """
    Klasa do analizy tekstu.
    """
    
    def __init__(self, text):
        """Inicjalizuje obiekt z tekstem."""
        self.text = text
    
    def word_count(self):
        """Liczy słowa w tekście."""
        return len(self.text.split())
    
    def character_count(self):
        """Liczy znaki w tekście (bez spacji)."""
        return len(self.text.replace(" ", ""))

def remove_special_chars(text):
    """
    Usuwa znaki specjalne z tekstu.
    
    Args:
        text: Tekst do oczyszczenia
        
    Returns:
        Oczyszczony tekst
    """
    return re.sub(r'[^a-zA-Z0-9\sąćęłńóśźżĄĆĘŁŃÓŚŹŻ]', '', text)