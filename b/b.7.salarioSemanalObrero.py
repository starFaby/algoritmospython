"""
Un obrero necesita calcular su salario semanal,
el cual se obtiene de la siguiente manera: Si 
trabaja 40 horas o menos
se le paga $16 por hora. Si trabaja mas de 40
 horas se le paga $16 por 
cada una de las primeras 40 horas y $20 por 
cada hora extra.
"""

on = True
while on:
    horas = int(input("Ingresa el total de horas \n Teclea 0 para salir\n =>"))
    if horas <= 40:
        salario = horas * 16
        print(f"El salario por trabajar 40horas o menos es: {salario}")
    else:
        aux = horas - 40
        hextra = aux * 16
        hnormal = 40 * 16
        salario = hextra +hnormal
        print(f"El salario mas horas extaras es: {salario}")
    
    if horas == 0:
        on = False