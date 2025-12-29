"""
Testy jednostkowe dla biblioteki.
"""

import unittest
import sys
import os

# Dodajemy ścieżkę do modułów
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_utils import validate_email, format_date
from math_tools import Statistics, calculate_correlation
from text_processing import TextAnalyzer, remove_special_chars

class TestDataUtils(unittest.TestCase):
    
    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("test@"))
        self.assertFalse(validate_email("@example.com"))
    
    def test_format_date(self):
        self.assertEqual(format_date("2024-03-15"), "15.03.2024")
        self.assertEqual(format_date("niepoprawna"), "Nieprawidłowa data")

class TestMathTools(unittest.TestCase):
    
    def test_statistics_mean(self):
        stats = Statistics([1, 2, 3, 4, 5])
        self.assertEqual(stats.mean(), 3.0)
        self.assertEqual(Statistics([]).mean(), 0)
    
    def test_statistics_median(self):
        stats_odd = Statistics([1, 2, 3, 4, 5])
        stats_even = Statistics([1, 2, 3, 4])
        self.assertEqual(stats_odd.median(), 3.0)
        self.assertEqual(stats_even.median(), 2.5)
    
    def test_calculate_correlation(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        result = calculate_correlation(x, y)
        self.assertAlmostEqual(result, 1.0, places=5)
    
    def test_calculate_correlation_error(self):
        with self.assertRaises(ValueError):
            calculate_correlation([1, 2, 3], [1, 2])

class TestTextProcessing(unittest.TestCase):
    
    def test_text_analyzer(self):
        analyzer = TextAnalyzer("To jest test")
        self.assertEqual(analyzer.word_count(), 3)
        self.assertEqual(analyzer.character_count(), 10)  # "To jest test"
    
    def test_remove_special_chars(self):
        text = "Hello, World! 123"
        result = remove_special_chars(text)
        self.assertEqual(result, "Hello World 123")
        
        text_pl = "Zażółć gęślą jaźń!"
        result_pl = remove_special_chars(text_pl)
        self.assertEqual(result_pl, "Zażółć gęślą jaźń")

if __name__ == '__main__':
    unittest.main()