"""
    crear calculadora con
    las 4 operaciones matematicas
"""

num1 = 0
num2 = 0
result = 0
on = True
while on:
    opcion = int(input("CALCULADORA \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- Divicion \n 5.- Salir \n ELIJA UNA OPERACION  \n =>"))
    match opcion:
        case 1:
            num1 = int(input("Ingrese el primer numero \n =>"))
            num2 = int(input("Ingrese el segundo numero \n =>"))
            result = num1 + num2
            print(f"La suma es: {result}")
        case 2:
            num1 = int(input("Ingrese el primer numero \n =>"))
            num2 = int(input("Ingrese el segundo numero \n =>"))
            result = num1 - num2
            print(f"La resta es: {result}")
        case 3:
            num1 = int(input("Ingrese el primer numero \n =>"))
            num2 = int(input("Ingrese el segundo numero \n =>"))
            result = num1 * num2
            print(f"La multiplicacion es: {result}")

        case 4:
            num1 = int(input("Ingrese el primer numero \n =>"))
            num2 = int(input("Ingrese el segundo numero \n =>"))
            result = num1 / num2
            print(f"La divicion es: {result}")

        case 5:
            print("Gracias por visitar.... vuelva pronto")
            on = False
        case _:
            print("Opcion no valida")