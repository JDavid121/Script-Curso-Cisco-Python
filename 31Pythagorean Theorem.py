"""
Programa que evalua el Teorema de Pitágoras
"""
#presentación
print("*********************")
print()
print("PROGRAMA QUE EVALUA EL TEOREMA DE PITÁGORAS")
print()
print("\tc=(a^2+b^2)^0.5")
print()
print("*********************")
print()
a=input("\tIngrese el valor del cateto a en m\n")
print()
b=input("\tIngrese el valor del cateto b en m\n")
print()
print("El valor del cateto a es\n",a,"m")
print()
print("El valor del cateto b es\n",b,"m")
print()
aa=float(a)             #Transformamos a de str a float
bb=float(b)             #Transformamos b de str a float
cc=(aa**2+bb**2)**(0.5) #Evaluación de la expresión T.P
print("El valor de la hipotenusa c es\n",cc,"m")
print()
print("\tFin del programa")
print("********************")
