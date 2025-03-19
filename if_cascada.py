'''
if en cascada:
estructura selectiva 
compuesta por multiples 
condicionales,seguidos
unos de otros
Sintaxis:
if condicional:
    instruccion1
    instruccion2
elif condicional2:
    instruccion3
    instruccion4
elif condicional3:
    instruccion5
    instruccion6
NOTA: cada condicional es 
MUTUAMENTE EXCLUYENTE
'''

'''
#ejemplo:
#vamos hacer un 
#pequeño traductor
#el programa debe permitir 
#leer una fruta en español
#y debe mostrar esa fruta
#en ingles
fruta_es= input ("ingrese una fruta: ")
if fruta_es == "manzana" or fruta_es == "Manzana":
    print("aple")
elif fruta_es == "naranja" or fruta_es == "Naranja":
    print("orange")
elif fruta_es == "uva" or fruta_es == "Uva":
    print("grape")
# caso por defecto
#default
else:
    print("no se encontro traduccion")
'''

precio_m = int(input("Ingrese el precio de la matricula: "))
edad = int(input("Ingrese su edad: "))
estrato = input("Ingrese su estrato: ")


if edad < 18 and estrato == "1":
      descuento = precio_m * 0.20
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
elif edad >= 18 and estrato == "1":
      descuento = precio_m * 0.15
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
elif edad < 18 and estrato == "2":
      descuento = precio_m * 0.10
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
elif edad >= 18 and estrato == "2":
      descuento = precio_m * 0.05
      precio_final = precio_m - descuento
      print("El precio final es: ", precio_final)
else:
      print("No tiene descuento")
      