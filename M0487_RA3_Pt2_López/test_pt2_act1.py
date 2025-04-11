import unittest
from pt2_act2 import sumar, restar, dividir, multiplicar,arrel_quadrada

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        print("Iniciant test...")
        
    def tearDown(self):
        print("Finalitzant test...")
        
    # Test de la suma
    def test_sumar(self):
        self.assertEqual(sumar(3, 4), 7)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(sumar(0, 0), 0)

    # Test de la resta
    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(5, 10), -5)
        self.assertEqual(restar(0, 0), 0)

    # Test de la multiplicación
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(0, 4), 0)
        self.assertEqual(multiplicar(-3, 4), -12)

    # Test de la divisió
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(10, 3), 10 / 3)
        self.assertEqual(dividir(0, 5), 0)
        self.assertEqual(dividir(10, 0), "Error: No es pot dividir per zero.")
    
    # Test de l'arrel quadrada
    def test_arrel_quadrada(self):
        self.assertEqual(arrel_quadrada(4), 2)
        self.assertEqual(arrel_quadrada(9), 3)
        self.assertEqual(arrel_quadrada(0), 0)
        with self.assertRaises(ValueError):
            arrel_quadrada(-4)

if __name__ == '__main__':
    unittest.main()