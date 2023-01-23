"""
Dadas las edades y alturas de 5 alumnos, mostrar la edad y 
la estatura media, la cantidad de alumnos mayores de 18 años, y la cantidad 
de alumnos que miden más de 1.75.
"""
alummayores=[]
alummaltos=[]
alumno = [
    {"nombre":"lynna","edad":15,"altura":150},
    {"nombre":"darlyng","edad":18,"altura":170},
    {"nombre":"erika","edad":12,"altura":140},
    {"nombre":"mary","edad":21,"altura":140},
    {"nombre":"vanesa","edad":12,"altura":140},
    ]
print("Alumnos Mayores")
for item in alumno:
    if item["edad"] >= 18:
        print(item)
    

print("Alumnos Altos")   
for item in alumno:
    if item["altura"] >= 150:
        print(item)




