"""
Programa que lea un carácter
por teclado y compruebe si 
es una letra mayúscula.
"""
on = True
while on:
    letra = input("Ingresa una letra \n =>")
    if letra.isupper():
        print("Es una letra mayuscula")
        
    else:
        print(" La letra es minuscula")

    if letra == "salir":
        on = False
        print("Saliste... vuelva pronto")

    
