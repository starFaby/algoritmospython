"""
Programa que lea 
un número entero y
muestre si el número
es múltiplo de 10.

"""

on = True
while on:
    num = int(input("Ingrese un numero \n =>"))
    if num%10 == 0:
        print("Es divisible para 10")
    else:
        print("No es divisible para 10")

    if num == 0:
        print("Gracias por visiatar... vuelva pronto")
        on = False