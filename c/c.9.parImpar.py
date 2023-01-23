"""
Leer números hasta que se introduzca un 0. Para cada uno indicar si es par o impar.

"""
par = []
impar = []
on = True
while on:
    num = int(input("ingres un numero"))
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
    
    if num == 0:
        on = False

print("numeros pares")
for item in par:
    print(par)

print("numeros impares")
for item in impar:
    print(item)

