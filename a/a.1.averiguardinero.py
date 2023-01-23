"""
Guillermo tiene N dolares. Luis tiene la mitad de lo que
posee Guillermo. Juan tiene la mitad de lo que poseen
Luis y Guillermo juntos. Hacer un programa que calcule
e imprima la cantidad de dinero que tienen entre los tres.
"""
guillermo = 10
luis = 0
juan = 0

luis = guillermo / 2
juan = (guillermo + luis)/2

print(f"guillermo tiene {guillermo} luis tiene {luis} y juan posee {juan}")