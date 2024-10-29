#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543
#Ingrese numero: 241
#142

numberFirst=input("Enter a number of 3 digits: ")
numberInvest=numberFirst[::-1] #para invertir 
print(f"#{numberInvest}")
numberSecond=input("Enter a number of 3 digits: ")
numberInvest=numberSecond[::-1] #para invertir 
print(f"#{numberInvest}")