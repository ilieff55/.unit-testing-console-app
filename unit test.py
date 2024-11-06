import unittest
from unittest.mock import patch
import math
from error_areas import calculate_area

class TestCalculateArea(unittest.TestCase):

    @patch('builtins.input', side_effect=['square', '4'])
    def test_square(self, mock_input):
        with patch('builtins.print') as mock_print:
            calculate_area('square')
            mock_print.assert_called_with(16.0)  # Expected area for square with side 4

    @patch('builtins.input', side_effect=['rectangle', '4', '6'])
    def test_rectangle(self, mock_input):
        with patch('builtins.print') as mock_print:
            calculate_area('rectangle')
            mock_print.assert_called_with(24)  # Incorrect formula, should be 24.0

    @patch('builtins.input', side_effect=['circle', '3'])
    def test_circle(self, mock_input):
        with patch('builtins.print') as mock_print:
            calculate_area('circle')
            mock_print.assert_called_with(math.pi * 3 * 3)  # Area of circle with radius 3

    @patch('builtins.input', side_effect=['triangle', '4', '6'])
    def test_triangle(self, mock_input):
        with patch('builtins.print') as mock_print:
            calculate_area('triangle')
            mock_print.assert_called_with(12.0)  # Area of triangle with base 4 and height 6

if __name__ == '__main__':
    unittest.main()
