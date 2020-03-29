"""
Scenario
Evaluate the following expressión for:
x=0
x=1
x=-1
3x^3 - 2x^2 + 3x - 1

"""

x=0 #Declaración de la variable x
print("*********************************")
print()
print("\tPrograma que evalúa el valor de x en la siguiente expresión")
print()
print("\t3x^3-2x^2+3x-1")
print()
x=input("Ingrese el valor de x\n")
print()
print("El valor de x es\n",x)
print()
print("\ty=3x^3-2x^2+3x-1")
print()
x=float(x)                      #Transformamos el valor de x de str a float para hacer las operaciones matemáticas
y=3*x**3-2*x**2+3*x-1
print()
print("El valor de y es \n",y)
print()
print("Fin del programa")
