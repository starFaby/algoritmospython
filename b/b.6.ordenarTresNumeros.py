"""
    Pedir tres números y mostrarlos ordenados de menor a mayor.

"""
num1 = int(input("Ingresa el primer numero"))
num2 = int(input("Ingresa el segundo numero"))
#num3 = int(input("Ingresa el tercero numero"))

if num1 > num2:
    print(f"{num2}{num1}")
if num1 < num2:
    print(f"{num1}{num2}")

   