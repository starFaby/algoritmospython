"""
Pedir números hasta que se introduzca uno negativo, y calcular la media.

"""
suma = 0
count = 0
on = True
while on:
    num = int(input("ingresar el numero"))
    if num > 0:
        suma += num
        count += 1
    elif num == 0:
        print("La division para cero no existe")
        on = False
    else:
        on = False

print(f"la media de numeros positivos {suma/count}")