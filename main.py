
#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#El promedio del ramo se calcula con la siguiente formula.

#NC=(C1+C2+C3)3
#NF=NC⋅0.7+NL⋅0.3
#Donde NC
 #es el promedio de certámenes, NL
 #el promedio de laboratorio y NF
 #la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3


certamenFirst = float(input("Ingrese nota certamen 1: "))
certamenSecond = float(input("Ingrese nota certamen 2: "))
gradeLaboratory = float(input("Ingrese nota laboratorio: "))


NF_requerida = 60



NC_requerida = (NF_requerida - gradeLaboratory * 0.3) / 0.7


C3_necesaria = NC_requerida * 3 - certamenFirst - certamenSecond

print(f"Necesita nota {C3_necesaria:.2f} en el certamen 3")
