import unittest

from app import somar, subtrair, multiplicar, dividir


class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(10, 5), 15)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(10, 5), 50)

    def test_dividir(self):
        self.assertEqual(dividir(10, 5), 2)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()
