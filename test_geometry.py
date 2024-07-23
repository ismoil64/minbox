import unittest
from geometry import figure

class FigureTest(unittest.TestCase):
    def test_triangle_square(self):
        self.assertEqual(figure.find_square(3, 4, 5), 6.0)
        self.assertEqual(figure.find_square(80, 60, 100), 2400.0)
        with self.assertRaises(ValueError):
            figure.find_square(3, 4, 6)
    
    def test_circle_square(self):
        self.assertEqual(figure.find_square(4), 50.27)
        self.assertEqual(figure.find_square(6), 113.1)

    def test_negative_vals(self):
        with self.assertRaises(ValueError):
            figure.find_square(-3, 4, 5)
        figure.find_square()

    def test_add_figure(self):
        figure.add_figure(2, lambda x, y: x * y)
        self.assertEqual(figure.find_square(3, 4), 12)