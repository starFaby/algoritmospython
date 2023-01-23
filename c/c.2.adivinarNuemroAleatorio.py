"""
Realizar un juego para adivinar un número. 
Para ello generar un número aleatorio entre 0-100, y luego ir   
pidiendo números indicando “es mayor” o “es menor” según sea mayor o menor
con respecto a N. El proceso termina     cuando el usuario acierta y mostrar
el número de intentos.
"""

from random import randrange

intentos = 0
on = True
aleatorio = randrange(100)
print(aleatorio)
while on:
    intentos += 1
    num = int(input("Ingresa el numero \n => "))
    if num == aleatorio:
        print("Acertaste mijin")
        print(f"El total de intentos fue de : {intentos} ")
        on = False