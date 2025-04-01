# Funció per comprovar si un nombre és primer
def esPrimer(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Comprovació de nombres primers entre 1 i 20
for num in range(1, 21):
    if esPrimer(num):
        print(num)