"""
Pedir 10 números. Mostrar la media de los números positivos, la media de los   
números negativos y la cantidad de ceros.
"""

sumaposi=0
sumanega=0
contposi=0
contnega=0
contceros=0
arreglo = []
for item in range(10):
    aux = int(input(f"ingrese el {item} numero"))
    arreglo.append(aux)

for item in arreglo:
    if item > 0:
        sumaposi += item
        contposi += 1

    if item < 0:
        sumanega += item
        contnega += 1

    if item == 0:
        contceros += 1

print(f"media posiitvos{sumaposi/contposi}")
print(f"media negativos{sumanega/contnega}")
print(f"conteo de ceros{contceros}")
