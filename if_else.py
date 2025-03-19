'''
if_else:
determina dos caminos
de ejecucion, basados en la evaluacion
de una condicional.

if (condicion):
    instruccion1
    instruccion2    
else:   
    instruccion3 
    instruccion4 
'''
#ejemplo:
#elabore un ejemplo de python 
#que determine si una persona 
#es mayor o menos de edad 
#y por tanto, habilitada para votar
edad = 20
documento= False
if edad >= 18 and documento == True:
    print ("eres mayor de edad")
    print ("puedes votar")
else:
    print ("eres menor de edad")
    print ("o")
    print ("no puedes votar")
print ("fin del programa")