import unittest
from ..calculations import evaluate_npi


class TestCalculations(unittest.TestCase):
    def test_evaluate_npi_addition(self):
        result = evaluate_npi("3 4 +")
        self.assertEqual(result, 7.0)

    def test_evaluate_npi_subtraction(self):
        result = evaluate_npi("5 2 -")
        self.assertEqual(result, 3.0)

    def test_evaluate_npi_multiplication(self):
        result = evaluate_npi("2 3 *")
        self.assertEqual(result, 6.0)

    def test_evaluate_npi_division(self):
        result = evaluate_npi("8 4 /")
        self.assertEqual(result, 2.0)

    def test_evaluate_npi_complex_expression(self):
        result = evaluate_npi("3 4 + 2 * 7 /")
        self.assertEqual(result, 2.0)

if __name__ == "__main__":
    unittest.main()
