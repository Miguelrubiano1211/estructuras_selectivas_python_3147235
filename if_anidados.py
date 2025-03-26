'''

el if_anidados:
es un if dentro de otros if
syntaxis:
if condicion1:
    else:
    print("mensaje6")
no confundir el if(el if en cascada)
'''
#ejemplo_1:
#modifique el ejercicio de la edad 
#para las ssiguientes condiciones 
#1. si es mayor a 18 años
#ñerl no tiene documento no puede votar
#de lo contrario si ouede votar 
#2. si es menor de 18 años 
# no puede votar 
#utilice los if anidados 

edad = int (input("ingrese sue edad:"))
if edad >= 18:
    documento = input ("tiene documento? si/no:")
    if documento == "si":
        print ("Puede votar")
    else:
        print ("no puede votar")
else:
    print ("No puede votar, eres menor de edad")
    