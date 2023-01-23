"""
Leer un número y mostrar su cuadrado, repetir el proceso 
hasta que se introduzca un número negativo.
"""

import math
exponente = 2
on = True
while on:
    base = int(input("ingresa la base"))
    if base > 0:
        result = math.pow(base,exponente)
        print(f"El resultado es:{result} ")
    if base <= 0:
        on = False
        print("No existe valores negativos")
        print("saliste vuelva pronto")
