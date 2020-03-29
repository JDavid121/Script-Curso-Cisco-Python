"""
Evaluación de la función print
"""

"""
    Uniones de los key argument end y sep
    El keyword argument sep es un separador entre cada argumento de la función print.
    Si no se utiliza el keyword sep, en cada argumento delimitado por , se coloca un
    espacio vacío.
    Con el keyword sep, se indica que se debe colocar para separar los argumentos de salida
    de la función print() en su ejecución.
    
"""
#Ejercicio
"""
Obtener la siguiente expresión:
Programmig***Essentials***in...Python
utilizando las dos invocaciones de la funcion print:
print("Programming","Essentials","in")
print("Python")
Modificar la primera invocación, utilizar sep y end
No modificar la segunda función
"""
print("*******************************")
print()
print("Programming","Essentials","in")
print("Python")
print()
print("*******************************")
print()
print("Programming","Essentials","in",sep="***",end="...")  #sep="***" separa cada argumento con *** en la línea
print("Python")                                             #end="..." concatena la primera línea utilizando ... con la segunda
print()                                                     # línea
print("*******************************")
