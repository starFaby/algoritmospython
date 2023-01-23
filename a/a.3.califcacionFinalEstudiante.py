"""
 La calificación final de un 
    estudiante de Informática se
    calcula con base a las calificaciones
    de cuatro aspectos de su rendimiento
    académico: participación,
    primer examen parcial, segundo examen parcial
    y examen final.   
    Sabiendo que las calificaciones 
    anteriores entran a la calificación
    final con ponderaciones del 10%, 25%, 25% y 40%,    
    Hacer un programa que calcule e 
    imprima la calificación final obtenida por un estudiante.
"""

participacion = 10
examenparcial = 8
examenparcial2 = 5
examenfinal = 6

participacion *= 0.10
examenparcial *= 0.25
examenparcial2 *= 0.25
examenfinal *= 0.40

fasefinal = participacion + examenparcial +examenparcial2 + examenfinal
print(f"NOta final es: {fasefinal}")