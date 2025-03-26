'''
actividad 3:
elabore un programa que 
permita calcular 
el salario neto
de un empleado 
despues de descontar los descuentos por
conceptos de :
salud, pension , arl
1. el problema debe solicitar el tipo de empleado:
 a - contrato termino indefinido
 b - contrato por prestacion de servicios 
 c - contrato de aprendizaje
 d - contrato de jornal (Freelance)
=> para el caso de jornal:
se debe solicitar:
- numero de horas trabajadas y el valor apagar por hora
- el total del salario se calcula de multiplicar el numero de horas por el valor a pagar por hora 

'''

contrato = input("ingrese el tipo de contrato: ")
# inicializar a una variable 
#asi se utilice mas adelante 
salario_neto = 0
if contrato == "a":
    print("eligio: contrato termino indefinido.")
elif contrato == "b":
    print ("eligio: contrato por prestacion de servicio.")
elif contrato == "c":
    print ("eligio: contrato de aprendizaje.")
    salario_minimo = int(input("ingrese el salario minimo legal vigente: "))
    salario_neto = salario_minimo - (salario_minimo * 0.25)
elif contrato == "d":
    print ("eligio: contrato por jornal.")
    numero_horas = int(input("ingrese el numero de horas: "))
    valor_horas = int(input("ingrese el valor de las horas:"))
    salario_neto = numero_horas * valor_horas
else: 
    print ("tipo de documento no existe. ")
print ("el salario neto es:", salario_neto )
print ("fin del programa")