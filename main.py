#Círculos
#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5

radio=float(input("Enter the radius of the circle: "))
perimetro= ((radio*2)*3.14)
area=(3.14*(radio**2))

print(f"""
      the perimeter of you circle is {perimetro}
      the area of you circle is {area}  


""")
