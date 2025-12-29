"""
Moduł narzędzi matematycznych.
"""

import math

class Statistics:
    """
    Klasa do obliczeń statystycznych.
    """
    
    def __init__(self, data):
        """Inicjalizuje obiekt z danymi."""
        self.data = data
    
    def mean(self):
        """Oblicza średnią arytmetyczną."""
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)
    
    def median(self):
        """Oblicza medianę."""
        if not self.data:
            return 0
        
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

def calculate_correlation(x, y):
    """
    Oblicza współczynnik korelacji Pearsona.
    
    Args:
        x: Pierwsza lista danych
        y: Druga lista danych
        
    Returns:
        Współczynnik korelacji
    """
    if len(x) != len(y):
        raise ValueError("Listy muszą mieć tę samą długość")
    
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) * 
                           sum((yi - mean_y) ** 2 for yi in y))
    
    if denominator == 0:
        return 0
    
    return numerator / denominator