# Funcions per les operacions bàsiques
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divideix(a, b):
    if b == 0:
        return "Error: Divisió per zero!"
    return a / b

# Funció per la calculadora
def calculadora():
    while True:
        print("Menú de la calculadora:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicació")
        print("4. Divisió")
        print("0. Sortir")
        
        opcio = input("Escull una opció: ")
        
        if opcio == '0':
            print("Sortint de la calculadora.")
            break
        
        try:
            num1 = float(input("Introdueix el primer nombre: "))
            num2 = float(input("Introdueix el segon nombre: "))
        except ValueError:
            print("Error: Introdueix nombres vàlids!")
            continue
        
        if opcio == '1':
            print(f"Resultat: {suma(num1, num2)}")
        elif opcio == '2':
            print(f"Resultat: {resta(num1, num2)}")
        elif opcio == '3':
            print(f"Resultat: {multiplica(num1, num2)}")
        elif opcio == '4':
            print(f"Resultat: {divideix(num1, num2)}")
        else:
            print("Opció no vàlida!")

calculadora()