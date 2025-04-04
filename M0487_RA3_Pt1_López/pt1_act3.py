import os

# Nom del fitxer predefinit
nom_fitxer = "a.txt"

def mostrar_menu():
    print("----- Menú -----")
    print("1. Comptar el nombre de línies del fitxer")
    print("2. Comptar el nombre de paraules del fitxer")
    print("3. Comptar el nombre de lletres del fitxer")
    print("0. Sortir")
    print("----------------")

def comptar_línies(fitxer):
    fitxer.seek(0)  # Reinicia el cursor al principi del fitxer
    línies = fitxer.readlines()
    fitxer.seek(0)
    return len(línies)


def comptar_paraules(fitxer):
    fitxer.seek(0)  # Reinicia el cursor al principi del fitxer
    contingut = fitxer.read()
    paraules = contingut.split()
    fitxer.seek(0)
    return len(paraules)

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
    # Es pot modificar la variable 'nom_fitxer' per analitzar un altre fitxer
    fitxer = analitzar_fitxer(nom_fitxer)
    if not fitxer:
        return  # Si el fitxer no existeix, sortim del programa

    while True:
        mostrar_menu()
        try:
            opcio = int(input("Selecciona una opció (0-3): "))
            if opcio == 0:
                print("Sortint del programa...")
                fitxer.close()  # Tanca el fitxer abans de sortir
                break
            elif opcio == 1:
                línies = comptar_línies(fitxer)
                print(f"El fitxer té {línies} línies.")
                print(fitxer.read())
            elif opcio == 2:
                paraules = comptar_paraules(fitxer)
                print(f"El fitxer té {paraules} paraules.")
                print(fitxer.read())                
            elif opcio == 3:
                lletres = comptar_lletres(fitxer)
                print(f"El fitxer té {lletres} lletres.")
                print(fitxer.read())
            else:
                print("Error: Opció no vàlida. Torna-ho a intentar.")
        except ValueError:
            print("Error: Has introduït una opció no vàlida. Torna-ho a intentar.")

if __name__ == "__main__":
    principal()