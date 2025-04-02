def menu():
    print("----- Calculadora Bàsica -----")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sortir")
    print("-----------------------------")

def obtenir_numero():
    while True:
        try:
            num = float(input("Introdueix un número: "))
            return num
        except ValueError:
            print("Error: No has introduït un número vàlid. Torna-ho a intentar.")

def realitzar_operacio(opcio):
    print("Introdueix els dos números per realitzar l'operació.")
    num1 = obtenir_numero()
    num2 = obtenir_numero()

    if opcio == 1:
        return num1 + num2
    elif opcio == 2:
        return num1 - num2
    elif opcio == 3:
        return num1 * num2
    elif opcio == 4:
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Error: No es pot dividir per zero.")
            return None

def principal():
    while True:
        menu()
        try:
            opcio = int(input("Selecciona una opció (0-4): "))
            if opcio == 0:
                print("Fins aviat!")
                break
            elif opcio < 0 or opcio > 4:
                print("Error: Opció no vàlida. Torna a intentar.")
            else:
                resultat = realitzar_operacio(opcio)
                if resultat is not None:
                    print(f"El resultat és: {resultat}")
        except ValueError:
            print("Error: Has introduït una opció no vàlida. Torna-ho a intentar.")

if __name__ == "__main__":
    principal()