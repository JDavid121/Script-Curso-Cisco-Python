"""
Estudio de la función Print
Ingreso de múltiples argumentos en la función print
Para ingresar múltiples argumentos en una sola función
print, se emplea una coma
La función print en cada coma, coloca un espacio

##"""

#Estudio de la función print

print("My name is","Python",end="b")    #end es un keyword argument
print("Monty Python")                   #Un keyword argument es un argumento de la función print
                                        #Un keyword argument tiene tres elementos.
                                        #Keyword define el tipo de argumento.
                                        #Un signo igual = que asigna un valor al argumento.
                                        #El valor asignado al argumento.

#Un keyword siempre se pone al final de la función print.
#Ejemplo
print("****************************************************")
print()
print("Publio Cornelio Escipión"," FUE ")
print("un general romano muy importante de la República de Roma"," Y QUE ADEMÁS ")
print("conquistó Nueva Cartago para la gloria de Roma")
print()
print("****************************************************")
print()
print("Publio Cornelio Escipión",end=" FUE ")
print("un general romano muy importante de la República de Roma",end=" Y QUE ADEMÁS ")
print("conquistó Nueva Cartago para la gloria de Roma")
print()
print("****************************************************")
print()
print("Publio Cornelio Escipión",end="\nFUE\n")
print("un general romano muy importante de la República de Roma",end="\nY QUE ADEMÁS\n")
print("conquistó Nueva Cartago para la gloria de Roma")
print()
print("****************************************************")
print()
print("Publio Cornelio Escipión",end="\n")                                   #Un keyword necesita de tres elementos
print("un general romano muy importante de la República de Roma",end="\n")
print("conquistó Nueva Cartago para la gloria de Roma")
print()
print("****************************************************")
