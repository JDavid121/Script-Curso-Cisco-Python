#Programa que escoge la transformación requerida:
# millas a km (A)
# km a millas (B)
#°F a °C (C)
#C a °F (D)
#En cada función se puede utilizar el mismo par de variables
def millas_km(a):
    a=float(a)
    b = a*1.61 # Transformación de millas a km
    b=round(b,3)
    return b
def km_millas(a):
    a=float(a)
    b = a/1.61 #Transformación de km a millas
    b = round(b,3)
    return b
def gfar_gcel(a):
    a=float(a)
    a=round(a,3) #Redondeamos la entrada a 3 decimales
    b=(a-32)*(5/9) #Transformación de grados farhenheit a celsius
    b=round(b,3)
    return b 
    
def gcel_gfar(a):
    a=float(a)
    a=round(a,3) #Redondeando la entrada a 3 decimales.
    b=32+(9/5)*a
    b=round(b,3)
    return b
def retardo():
    z=0    
    for i in range(1,10000,1):
        for j in range(1,3010,1):
            z=z+j
    ##print(z)
    return
        
#***************************************************
seleccion="O" #Definimos un valor inicial de seleccion
while True:
    print("********************************************")
    print()
    print("Programa de transformación de unidades")
    print()
    print("********************************************")
    print("Para transformar de km a millas, opción A")
    print("Para transformar de millas a km, opción B ")
    print("Para transformar de grados Farhenheit a grados Celsius, opción C")
    print("Para transformar de grados Celsius a grados Farhenheit, opción D")
    print("Para salir, introducir QUIT")
    print()
    print("********************************************")
    seleccion=input("Ingresar la opción requerida\t")
    if seleccion == "A":
        #Poner la función de km a millas
        print("Programa que transforma kilometros a millas")
        a = input("Ingresar la distancia en kilometros\n\t")
        print(a,"kilómetros euivalen a",km_millas(a),"millas")
        print("Fin del programa")    
    if seleccion == "B":
        #Poner la función de millas a km
        print("Programa que transforma millas a kilometros")
        a = input("Ingresar la distancia en millas\n\t")
        print(a,"millas equivalen a",millas_km(a),"kilometros")
        print("Fin del programa")
    if seleccion == "C":
        #Poner la función °F a °C
        print("Programa que transforma los grados Farhenheit a Celsius")
        a=input("Ingresar los grados Farenheit\n\t")
        print("\t",a,"°F","equivalen a",gfar_gcel(a),"°C")
        print("Fin del programa")
    if seleccion == "D":
        #Poner la función °C a °F
        print("Programa que transforma los grados Celsius a Farhenheit")
        a=input("Ingresar los grados Celsius\n\t")
        print("\t",a,"°C equivalen a",gcel_gfar(a),"°F")
        print("Fin del programa")
    if seleccion == "QUIT":    
        print("Saliendo del programa...")
        print("...")
        retardo()
        print("...")
        retardo()
        print("...")
        #retardo()
        print("Programa finalizado")
        break #Salir del lazo while
    
