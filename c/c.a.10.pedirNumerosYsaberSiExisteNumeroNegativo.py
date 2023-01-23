"""
Pedir 10 números, y mostrar al final si se ha introducido alguno negativo.

"""
positivos = 0
negativos = 0
for item in range(10):
    num = int(input("ingrese numero"))
    if num > 0:
        positivos += 1
    else:
        negativos += 1

print(f"Numeros positivos {positivos}")
print(f"Numeros negativos {negativos}")
    


