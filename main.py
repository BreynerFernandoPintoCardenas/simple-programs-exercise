#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

#Ingrese longitud: 45
#45 cm = 17.7165 in
#Ingrese longitud: 13
#13 cm = 5.1181 in

longitud=float(input("Enter the lenght: "))
pulgadas=2.54
conversion=(longitud/pulgadas)
print(f"""{longitud} cm = {conversion}""")

longitud=float(input("Enter the lenght: "))
conversion=(longitud/pulgadas)
print(f"""{longitud} cm = {conversion}""")
