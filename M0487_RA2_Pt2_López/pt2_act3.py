import string

def canvi_de_case():
    while True:
        cadena = input("Introdueix una cadena: ")  # Demana la cadena cada vegada
        print("Opcions:")
        print("1. Tot en majúscules")
        print("2. Tot en minúscules")
        print("3. Primer caràcter en majúscula i la resta en minúscula")
        print("0. Sortir")
        opcio = input("Escull una opció: ")
        
        if opcio == '1':
            print(cadena.upper())  # Mostra la cadena en majúscules
        elif opcio == '2':
            print(cadena.lower())  # Mostra la cadena en minúscules
        elif opcio == '3':
            print(cadena.capitalize())  # Mostra la cadena amb el primer caràcter en majúscula
        elif opcio == '0':
            print("Sortint del programa.")  # Termina el programa
            break
        else:
            print("Opció no vàlida, torna a provar.")  # Si l'usuari tria una opció incorrecta

canvi_de_case()