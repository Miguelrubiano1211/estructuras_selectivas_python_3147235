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


=> para el caso de prestacion de servicio
se debe solicitar: 
- el valor de contrato 
- el numero de meses de contrato 
- la antiguedad del empleado (años)
salario neto, en este caso se calcula:
1. dividir el el valor del contrato por el numero de meses 
2. restar el 15% del valor del contrato por consepto de eps
3. restar el 10% del valor del contrato por concepto de pension 
4. si el empleador tiene una antiguedad = o superior a 10 años:
tiene una bonificacion del 0.5% sobre el salario mensual 



=> Para el caso de contrato a termino indefinido 
se debe solicitar:
- Antiguedad (años)
- Grado o escalafon (1-5)
- salario minimo legal vigente 


El salario mensual se calcula de acuerdo  a la siguiente tablaa:
- grado 1: 1.5 SM
- grado 2 : 1.7 SM
- grado 3: 2.0 SM
- grado 4: 2.5 SM
- grado 5: 3.0 SM
la bonificacion estara acorde a los siguientes rango segun la antiguedad:
- entre 1 y 5 años : 1% el salario mensual
- entre 6 y 10 años : 2% el salario mensual
- superior a 10 años : al 3% del salario mensual
- para este caso, los descuentos de ley son: 

- 25% por concepto de la eps 
- 22% por concepto de la pension
- 0.1% por concepto de la arl
'''

contrato = input("ingrese el tipo de contrato: ")
# inicializar a una variable 
#asi se utilice mas adelante 
salario_neto = 0
if contrato == "a":
    print("eligio: contrato termino indefinido.")
    antiguedad = int(input("Ingrese la antiguedad del empleado (Año):"))
    grado = int(input("Ingrese el grado del empleado:(1-5)"))
    salario_neto= int(input("Ingrese el salario neto del empleado:"))
    salario_minimo = int(input("Ingrese el salario minimo:"))
    if grado == 1:
        salario_neto = salario_minimo*1.5
    elif grado == 2:
        salario_neto = salario_minimo*1.7
    elif grado == 3:
        salario_neto = salario_minimo*2.0
    elif grado == 4:
        salario_neto = salario_minimo*2.5
    elif grado == 5:
        salario_neto = salario_minimo*3.0
    if antiguedad >= 1 and antiguedad <= 5:
        salario_neto = salario_neto + (salario_minimo*0.01)
    elif antiguedad >= 6 and antiguedad <= 10:
        salario_neto = salario_neto + (salario_minimo*0.02)
    elif antiguedad >= 10:
        salario_neto = salario_neto + (salario_minimo*0.03)
    salario_neto = salario_neto - (salario_neto*0.25) - (salario_neto*0.22) - (salario_neto*0.001)

elif contrato == "b":
    print ("eligio: contrato por prestacion de servicio.")
    valor_contrato = int (input("ingrese el valor del contrato: "))
    numero_meses = int (input("ingrese el numero de meses trabajador: "))
    antiguedad = int(input("ingrese la antiguedad del empleado en años: "))
    salario_mensual = valor_contrato / numero_meses 
    EPS = salario_mensual * 0.15
    pension = salario_mensual * 0.10 
    bonificacion = salario_mensual * 0.05 
    salario_neto = salario_mensual - EPS - pension
    if antiguedad >= 10:
        salario_neto = salario_mensual + bonificacion

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