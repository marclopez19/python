import unittest
from pt2_act2 import sumar, restar, dividir, multiplicar, arrel_quadrada

class TestCalculadora(unittest.TestCase):

    # Test de la suma
    def test_sumar(self):
        resultado = sumar(3, 4)
        self.assertEqual(resultado, 7)

        resultado = sumar(-1, -1)
        self.assertEqual(resultado, -2)

        resultado = sumar(0, 0)
        self.assertEqual(resultado, 0)

    # Test de la resta
    def test_restar(self):
        resultado = restar(10, 5)
        self.assertEqual(resultado, 5)

        resultado = restar(5, 10)
        self.assertEqual(resultado, -5)

        resultado = restar(0, 0)
        self.assertEqual(resultado, 0)
    
    # Test de la multiplicación
    def test_multiplicar(self):
        resultado = multiplicar(3, 4)
        self.assertEqual(resultado, 12)

        resultado = multiplicar(0, 4)
        self.assertEqual(resultado, 0)

        resultado = multiplicar(-3, 4)
        self.assertEqual(resultado, -12)

    # Test de la divisió
    def test_dividir(self):
        resultado = dividir(10, 2)
        self.assertEqual(resultado, 5)

        resultado = dividir(10, 3)
        self.assertEqual(resultado, 10 / 3)

        resultado = dividir(0, 5)
        self.assertEqual(resultado, 0)

        resultado = dividir(10, 0)
        self.assertEqual(resultado, "Error: No es pot dividir per zero.")

    # Test de l'arrel quadrada
    def test_arrel_quadrada(self):
        resultado = arrel_quadrada(4)
        self.assertEqual(resultado, 2)

        resultado = arrel_quadrada(9)
        self.assertEqual(resultado, 3)

        resultado = arrel_quadrada(0)
        self.assertEqual(resultado, 0)

        with self.assertRaises(ValueError):
            arrel_quadrada(-4)

if __name__ == '__main__':
    unittest.main()