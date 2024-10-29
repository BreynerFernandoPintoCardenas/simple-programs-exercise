#Escriba un programa que reciba como entrada las longitudes de los dos catetos a
 #y b
 #de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
 #del triangulo, dado por el teorema de Pitágoras: c2=a2+b2

import math
#Ingrese cateto a: 7
#Ingrese cateto b: 5
#La hipotenusa es 8.6023252670426267
catetoA=float(input("Enter the cateto A: "))
catetoB=float(input("Enter the cateto B: "))
pitagoras =  math.sqrt(catetoA**2+catetoB**2)
print(f"la hipotenusa es {pitagoras}")