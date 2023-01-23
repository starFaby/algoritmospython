"""
Leer 5 números, guardarlos en un arreglo y mostrarlos en el mismo orden que ingresaron.
"""
arreglo = []
for item in range(5):
    llenar = input(f"Ingresa el {item} numero ")
    arreglo.append(llenar) 


for item in arreglo:
    print(item)