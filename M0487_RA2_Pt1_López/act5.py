#PAS 1
musicat=[]

#PAS 2
musicat.append('La Fumiga')
musicat.append('The Tyets')
musicat.append('Ginestà')
#print(musicat)

#PAS 3
for i in range(2):
    grup1=input("Nou grup: ")
    musicat.append(grup1)
print(musicat)

#PAS 4
for i in range(2):
    musicat.pop(3)
print(musicat)

#PAS 5
musicat.reverse()
musicat.append("La iaia")
musicat.reverse()
print(musicat)