# Funció per comprovar si un any és de traspàs
def esAnyDeTraspas(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    return False

# Comprovació dels anys especificats
anys = [1900, 2000, 2016, 1987]
for any in anys:
    if esAnyDeTraspas(any):
        print(f"{any} és un any de traspàs.")
    else:
        print(f"{any} no és un any de traspàs.")