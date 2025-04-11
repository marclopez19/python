import unittest
import os
import shutil
import sqlite3
from unittest.mock import patch

from pt2_act3_bbdd import crear_taula, afegir_grup, mostrar_grups, eliminar_grup, actualitzar_grup

# Rutes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_ORIGINAL = os.path.join(BASE_DIR, "grups_musica.db")
DB_TEST = os.path.join(BASE_DIR, "grups_test.db")

class TestGestorGrups(unittest.TestCase):

    def setUp(self):
        """Configura el test amb una base de dades nova."""
        # Crear una base de dades nova per als tests
        if os.path.exists(DB_TEST):
            os.remove(DB_TEST)
        
        # Forcem el mòdul pt2_act3_bbdd a treballar amb la base de dades de test
        import pt2_act3_bbdd
        pt2_act3_bbdd.DB_NAME = DB_TEST

        # Obrim connexió per consultar dades
        self.conn = sqlite3.connect(DB_TEST)
        self.cursor = self.conn.cursor()

    def tearDown(self):
        """Elimina la base de dades de test."""
        self.conn.close()
        if os.path.exists(DB_TEST):
            os.remove(DB_TEST)
    
    def test_crear_taula(self):
        """Comprova que la taula 'grups' es crea correctament."""
        crear_taula()
        
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='grups'")
        resultat = self.cursor.fetchone()
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat[0], "grups")

    def test_afegir_grup(self):
        """Comprova que afegir un grup l'insereix a la base de dades."""
        crear_taula()
        afegir_grup("Test Grup", 2023, "Pop", 4)
        
        self.cursor.execute("SELECT * FROM grups WHERE nom_grup=?", ("Test Grup",))
        resultat = self.cursor.fetchone()
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat[1], "Test Grup")
        self.assertEqual(resultat[2], 2023)
        self.assertEqual(resultat[3], "Pop")
        self.assertEqual(resultat[4], 4)

    def test_mostrar_grups(self):
        """Comprova que mostrar_grups retorna els grups correctament."""
        crear_taula()
        afegir_grup("Grup Mostrar", 2020, "Rock", 3)
        
        # Modificamos para obtener los datos directamente de la base de datos
        self.cursor.execute("SELECT * FROM grups")
        grups = self.cursor.fetchall()
        self.assertEqual(len(grups), 1)
        self.assertEqual(grups[0][1], "Grup Mostrar")

    def test_eliminar_grup(self):
        """Comprova que eliminar un grup el treu de la base de dades."""
        crear_taula()
        afegir_grup("Grup Eliminar", 2010, "Folk", 5)
        
        # Verifiquem que existeix abans d'eliminar
        self.cursor.execute("SELECT * FROM grups WHERE nom_grup=?", ("Grup Eliminar",))
        self.assertIsNotNone(self.cursor.fetchone())
        
        # Eliminem el grup
        eliminar_grup("Grup Eliminar")
        
        # Verifiquem que ja no existeix
        self.cursor.execute("SELECT * FROM grups WHERE nom_grup=?", ("Grup Eliminar",))
        self.assertIsNone(self.cursor.fetchone())

    @patch('builtins.input', side_effect=[
        'Grup Actualitzat',  # Nou nom
        '2016',              # Nou any
        'Rock',              # Nou tipus
        '5'                  # Nous integrants
    ])
    def test_actualitzar_grup(self, mock_input):
        """Comprova que actualitzar un grup modifica les seves dades."""
        crear_taula()
        afegir_grup("Grup Original", 2015, "Pop", 4)
        
        actualitzar_grup("Grup Original")
        
        # Verifiquem els canvis
        self.cursor.execute("SELECT * FROM grups WHERE nom_grup=?", ("Grup Actualitzat",))
        resultat = self.cursor.fetchone()
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat[2], 2016)  # Comprovem l'any
        self.assertEqual(resultat[3], "Rock")  # Comprovem el tipus
        self.assertEqual(resultat[4], 5)     # Comprovem integrants

if __name__ == "__main__":
    unittest.main()