import unittest
from abacus import calculation

class TestCalculation(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculation("add", 100, 400), 500)

    def test_subtract(self):
        self.assertEqual(calculation("sub", 200, 400), -200)
        self.assertEqual(calculation("sub", 500, 300), 200)
    
    def test_multiply(self):
        self.assertEqual(calculation("mult", 300, 900), 270000)

    def test_divide(self):
        self.assertEqual(calculation("div", 100, 400), 0.25)
        self.assertEqual(calculation("div", 700, 350), 2)
        self.assertEqual(calculation("div", 300, 175), 1.7142857142857142)

if __name__ == "__main__":
    unittest.main()