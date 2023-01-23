"""
Pedir el día, mes y año
de una fecha e indicar 
si la fecha es correcta.
Suponiendo todos los meses 
de 30 días.

"""
from datetime import datetime
anioactual = datetime.now()
on = True

while on:
    dia = int(input("Ingrese el dia \n =>"))
    if dia > 1 and dia < 30:
        mes = int(input("Ingrese el mes \n =>"))
        if mes > 1 and mes < 12:
            anio = int(input("Ingrese el año \n =>"))
            if  anio == anioactual.year:
                print(f"fecha correcta {dia}/{mes}/{anio}")
                on = False
            else: 
              print("Fecha Incorrecto... Ingrese de nuevo \n =>")  
        else:
            print("Mes Incorrecto... Ingrese de nuevo \n =>") 
    else:
        print("Dia Incorrecto... Ingrese de nuevo \n =>")
