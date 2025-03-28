x = int(input("Escriu el divident: "))
y = int(input("Escriu el divisor: "))

divisio = x / y
residu = divisio % 2

if divisio % 2 == 0:
    print("La divisió és exacta")
else:
    print("La divisió no és exacta")

print("Quocient: ",divisio)
print("Residu: ",residu)