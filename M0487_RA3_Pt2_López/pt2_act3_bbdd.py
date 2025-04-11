import sqlite3
import os
import datetime

# Ruta absoluta al mateix directori que l'script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "grups_musica.db")

# Crea la taula si no existeix
def crear_taula():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_grup TEXT NOT NULL,
            any_inici INTEGER,
            tipus_musica TEXT,
            num_integrants INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Afegeix un nou grup
def afegir_grup(nom_grup, any_inici, tipus_musica, num_integrants):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO grups (nom_grup, any_inici, tipus_musica, num_integrants)
            VALUES (?, ?, ?, ?)
        ''', (nom_grup, any_inici, tipus_musica, num_integrants))
        conn.commit()
        conn.close()
        print(f"Grup '{nom_grup}' afegit correctament.")
    except Exception as e:
        print(f"Error al afegir el grup: {e}")

# Mostra tots els grups
def mostrar_grups():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM grups')
        grups = cursor.fetchall()
        conn.close()

        if grups:
            print("\nLlista de grups:")
            for grup in grups:
                print(f"ID: {grup[0]}, Nom: {grup[1]}, Any inici: {grup[2]}, Tipus: {grup[3]}, Integrants: {grup[4]}")
        else:
            print("\nNo hi ha grups a la base de dades.")
    except Exception as e:
        print(f"Error en mostrar els grups: {e}")

# Elimina un grup pel seu nom
def eliminar_grup(nom_grup):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM grups WHERE nom_grup = ?
        ''', (nom_grup,))
        conn.commit()
        conn.close()
        print(f"Grup '{nom_grup}' eliminat correctament.")
    except sqlite3.Error as e:
        print(f"Error al eliminar el grup: {e}")

# Actualitza un grup pel seu nom
def actualitzar_grup(nom_grup):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Comprovar si el grup existeix
        cursor.execute('SELECT * FROM grups WHERE nom_grup = ?', (nom_grup,))
        grup = cursor.fetchone()
        if grup:
            print(f"Grup trobat: {grup}")
            # Sol·licitar noves dades per actualitzar
            new_nom = input(f"Nou nom del grup (Deixa en blanc per no canviar): ") or grup[1]
            new_any_inici = input(f"Nou any d'inici (Deixa en blanc per no canviar): ")
            new_any_inici = int(new_any_inici) if new_any_inici else grup[2]
            if new_any_inici > datetime.datetime.now().year:
                print("L'any d'inici no pot ser superior a l'any actual.")
                new_any_inici = datetime.datetime.now().year
            new_tipus = input(f"Nou tipus de música (Deixa en blanc per no canviar): ") or grup[3]
            while any(c.isdigit() for c in new_tipus):  # Comprovació per evitar números en el tipus de música
                print("El tipus de música no pot contenir números.")
                new_tipus = input(f"Nou tipus de música (Deixa en blanc per no canviar): ") or grup[3]
            new_integrants = input(f"Nou nombre d'integrants (Deixa en blanc per no canviar): ")
            new_integrants = int(new_integrants) if new_integrants else grup[4]
            
            cursor.execute('''
                UPDATE grups
                SET nom_grup = ?, any_inici = ?, tipus_musica = ?, num_integrants = ?
                WHERE nom_grup = ?
            ''', (new_nom, new_any_inici, new_tipus, new_integrants, nom_grup))
            conn.commit()
            print(f"Grup '{nom_grup}' actualitzat correctament.")
        else:
            print("No s'ha trobat cap grup amb aquest nom.")
        conn.close()
    except Exception as e:
        print(f"Error al actualitzar el grup: {e}")

# Funció per validar entrades numèriques
def obtenir_dada_numerica(missatge, tipus=int):
    while True:
        try:
            dada = tipus(input(missatge))
            return dada
        except ValueError:
            print(f"Error: has d'introduir un valor vàlid (número).")

# Menú principal
def menu():
    crear_taula()
    while True:
        print("###################################################################")
        print("#################### GRUPS DE MÚSICA en CATALÀ ####################")
        print("###################################################################")
        print("\n--- Menú ---")
        print("1. Afegir un nou grup de música en català")
        print("2. Mostrar tots els grups de música en català")
        print("3. Eliminar un grup de música")
        print("4. Actualitzar un grup de música")
        print("0. Sortir")
        opcio = input("Tria una opció: ")

        if opcio == "1":
            nom = input("Nom del grup: ")
            any_inici = obtenir_dada_numerica("Any d'inici: ", int)
            if any_inici > datetime.datetime.now().year:
                print("L'any d'inici no pot ser superior a l'any actual.")
                any_inici = datetime.datetime.now().year
            tipus = input("Tipus de música (pop, rock, folk, etc.): ")
            while any(c.isdigit() for c in tipus):  # Validació per evitar números en tipus
                print("El tipus de música no pot contenir números.")
                tipus = input("Tipus de música (pop, rock, folk, etc.): ")
            integrants = obtenir_dada_numerica("Nombre d'integrants: ", int)
            afegir_grup(nom, any_inici, tipus, integrants)
        elif opcio == "2":
            mostrar_grups()
        elif opcio == "3":
            nom = input("Nom del grup a eliminar: ")
            eliminar_grup(nom)
        elif opcio == "4":
            nom = input("Nom del grup a actualitzar: ")
            actualitzar_grup(nom)
        elif opcio == "0":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Torna-ho a provar.")

if __name__ == "__main__":
    menu()
