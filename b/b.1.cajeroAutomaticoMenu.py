"""
    Hacer un programa que simule un cajero automático 
    con un saldo inicial de 1000 dólares, con el
    siguiente menú de opciones:
    1. Ingresar dinero a la cuenta.
    2. Retirar dinero de la cuenta.
    3. Salir
"""
dinero = 1000
on = True
while on:
    num =  int(input("CAJERO AUTOMATICO\n 1.- Saldo \n 2.- Ingresar dinero \n 3.-retirar dinero \n 4.- Salir \n Ingrese una opcion \n =>"))
    match num:
        case 1:
            print("=====================")
            print(f"El Dinero es: {dinero}")
            print("=====================")

        case 2:
            dinero += int(input("Ingrese Dinero \n =>"))

        case 3:
            dinero -= int(input("Retirar Dinero \n =>"))
        
        case 4:
            print("Salio")
            on = False
        case _:
            print("error al escojer un numero")