"""
    Construir un programa que, dado un número
    total de horas, devuelve el número de
    semanas, días y horas  equivalentes. 
    Por ejemplo, dado un total de 1000 horas
    debe mostrar 5 semanas, 6 días y 16 horas.
"""
totalhoras = 1000
semanas = 0
dias = 0
horas = 0

semanas = totalhoras/168
dias = totalhoras%168/24
horas = totalhoras%24

print(f"total de semanas {semanas} total de dias es: {dias} total de horas es: {horas}")
