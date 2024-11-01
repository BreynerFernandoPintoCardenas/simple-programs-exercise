#El tiempo en segundos que toma al centro de la yema alcanzar Ty
 #°C está dado por la fórmula:

#t=M2/3cρ1/3Kπ2(4π/3)2/3ln[0.76To−TwTy−Tw],
#donde M
 #es la masa del huevo, ρ
 #su densidad, c
 #su capacidad calorífica específica y K
 #su conductividad térmica. Algunos valores típicos son:

#M=47[g]
 #para un huevo pequeño y M=67[g]
 #para uno grande,
#ρ=1.038[gcm−3]
#,
#c=3.7[Jg−1K−1]
#, y 
#K=5.4⋅10−3[Wcm−1K−1
#].
#Tw
 #es la temperatura de ebullición del agua y To
 #la temperatura original del huevo antes de meterlo al agua, ambos en grados Celsius.

#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.
import math


M = 67  
p= 1.038  
c = 3.7  
K = 5.4 * (10**-3)
Tw = 100 
Ty = 70  


To = float(input("Ingrese la temperatura original del huevo (en °C): "))



t = (M**(2/3) * c * p**(1/3))
dividiendo=(K * math.pi**2 * (4 * math.pi / 3)**(2/3))
logaritmo=math.log((0.76 *( (To - Tw) / (Ty - Tw)))) 
resultado=(t/dividiendo)
segundos=(resultado*logaritmo)
redondeando=round(segundos)

print(t)
print(dividiendo)       
print(resultado)
print(logaritmo)


print(f"""El tiempo para alcanzar la temperatura máxima de la yema es: {segundos} segundos
     y redondeada es: {redondeando}
""")  
