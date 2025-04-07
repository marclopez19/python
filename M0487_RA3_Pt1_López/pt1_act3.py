import os

def mostrar_menu():
    print("\n----- Menú -----")
    print("1. Comptar el nombre de línies del fitxer")
    print("2. Comptar el nombre de paraules del fitxer")
    print("3. Comptar el nombre de lletres del fitxer")
    print("4. Canviar el fitxer a llegir")
    print("0. Sortir")
    print("----------------")

def comptar_línies(fitxer):
    fitxer.seek(0)  # Reinicia el cursor al principi del fitxer
    línies = fitxer.readlines()   # Llegeix les linies del fitxer
    fitxer.seek(0)   # Reinicia el cursor al principi del fitxer
    return len(línies)   # Retorna les linies

def comptar_paraules(fitxer):
    fitxer.seek(0)  # Reinicia el cursor al principi del fitxer
    contingut = fitxer.read()   # Guarda el contingut del fitxer dins de la variable "contingut"   
    paraules = contingut.split()   # Separa per espais les paraules per poder-les contar bé
    fitxer.seek(0)   # Reinicia el cursor al principi del fitxer
    return len(paraules)   # Retorna les paraules

def comptar_lletres(fitxer):
    fitxer.seek(0)  # Reinicia el cursor al principi del fitxer
    contingut = fitxer.read()
    lletres = [caracter for caracter in contingut if caracter.isalpha()]
    fitxer.seek(0)
    return len(lletres)

def analitzar_fitxer(nom_fitxer):
    try:
        # Obtenim la ruta absoluta del fitxer
        fitxer_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), nom_fitxer)
        fitxer = open(fitxer_path, "r")
    except FileNotFoundError:
        print(f"Error: El fitxer {nom_fitxer} no existeix.")
        return None
    else:
        print(f"Fitxer obert correctament: {fitxer.name}")
        print("Contingut del fitxer:")
        contingut = fitxer.read()
        print(contingut)  # Mostra el contingut del fitxer
        fitxer.seek(0)  # Reinicia el cursor al principi per permetre la lectura posterior
        return fitxer

def principal():
    # Permet que l'usuari introdueixi el nom del fitxer inicial
    nom_fitxer = input("Introdueix el nom del fitxer a analitzar (per defecte és 'a.txt'): ") or "a.txt"

    fitxer = analitzar_fitxer(nom_fitxer)
    if not fitxer:
        return  # Si el fitxer no existeix, sortim del programa

    while True:
        mostrar_menu()
        try:
            opcio = int(input("Selecciona una opció (0-4): "))
            if opcio == 0:
                print("Sortint del programa...")
                fitxer.close()  # Tanca el fitxer abans de sortir
                break
            elif opcio == 1:
                línies = comptar_línies(fitxer)
                print(f"El fitxer té {línies} línies.")
            elif opcio == 2:
                paraules = comptar_paraules(fitxer)
                print(f"El fitxer té {paraules} paraules.")                
            elif opcio == 3:
                lletres = comptar_lletres(fitxer)
                print(f"El fitxer té {lletres} lletres.")
            elif opcio == 4:
                fitxer.close()  # Tancar el fitxer abans de reobrir-lo en mode lectura
                # Permet que l'usuari canviï el fitxer
                nom_fitxer = input("Introdueix el nou nom del fitxer a analitzar: ")
                fitxer = analitzar_fitxer(nom_fitxer)  # Tornar a obrir el fitxer
            else:
                print("Error: Opció no vàlida. Torna-ho a intentar.")
        except ValueError:
            print("Error: Has introduït una opció no vàlida. Torna-ho a intentar.")

if __name__ == "__main__":
    principal()