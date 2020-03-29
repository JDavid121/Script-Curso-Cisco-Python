#Programa que escoge la transformación requerida:
# millas a km (A)
# km a millas (B)
#°F a °C (C)
#C a °F (D)
def millas_km(mile):
    #print("Programa que transforma millas a kilometros")
    #mile = input("Ingresar la distancia en millas\n\t")
    mile=float(mile)
    #print("La distancia ingresada en millas es...",mile)
    mile_to_kilometers = mile*1.61 # Transformación de millas a km
    #print(mile,"millas equivalen a",round(mile_to_kilometers,3),"kilometros")
    #print("Fin del programa")
    mile_to_kilometers=round(mile_to_kilometers,3)
    return mile_to_kilometers
def km_millas(kilometer):
    #print("Programa que transforma kilometros a millas")
    #kilometer = input("Ingresar la distancia en kilometros\n\t")
    kilometer=float(kilometer)
    #print("La distancia ingresada en kilometros es...",kilometer)
    kilometers_to_mile = kilometer/1.61 #Transformación de km a millas
    kilometers_to_mile=round(kilometers_to_mile,3)
    #print(kilometer,"kilómetros euivalen a",round(kilometers_to_mile,3),"millas")
    #print("Fin del programa")
    return kilometers_to_mile
def gfar_gcel(farhenheit):
    #print("Programa que transforma los grados Farhenheit a Celsius")
    #farhenheit=input("Ingresar los grados Farenheit\n\t")
    farhenheit=float(farhenheit)
    farhenheit=round(farhenheit,3) #Redondeamos la entrada a 3 decimales
    #print("\tLos grados farhenheit ingresados son",farhenheit,"°F")
    celsius_to_farh=(farhenheit-32)*(5/9) #Transformación de grados farhenheit a celsius
    celsius_to_farh=round(celsius_to_farh,3)
    return celsius_to_farh 
    #print("\t",farhenheit,"°F","equivalen a",celsius_to_farh,"°C")
    #print("Fin del programa")
def gcel_gfar(celsius):
    #print("Programa que transforma los grados Celsius a Farhenheit")
    #celsius=input("Ingresar los grados Celsius\n\t")
    celsius=float(celsius)
    celsius=round(celsius,3) #Redondeando la entrada a 3 decimales.
    farh_to_celsius=32+(9/5)*celsius
    farh_to_celsius=round(farh_to_celsius,3)
    return farh_to_celsius 
    #print("\t",celsius,"°C equivalen a",farh_to_celsius,"°F")
    #print("Fin del programa")

print("********************************************")
print()
print("Programa de transformación de unidades")
print("Para transformar de km a millas, opción A")
print("Para transformar de millas a km, opción B ")
print("Para transformar de grados Farhenheit a grados Celsius, opción C")
print("Para transformar de grados Celsius a grados Farhenheit, opción D")
print()
print("********************************************")
seleccion=input("Ingresar la opción requerida")
if seleccion == "A":
    #Poner la función de km a millas
    print("Programa que transforma kilometros a millas")
    kilometer = input("Ingresar la distancia en kilometros\n\t")
    km_millas(kilometer)
    print(kilometer,"kilómetros euivalen a",km_millas(kilometer),"millas")
    print("Fin del programa")
    
    
if seleccion == "B":
    #Poner la función de millas a km
    print("Programa que transforma millas a kilometros")
    mile = input("Ingresar la distancia en millas\n\t")
    print(mile,"millas equivalen a",millas_km(mile),"kilometros")
    print("Fin del programa")


if seleccion == "C":
    #Poner la función °F a °C
    print("Programa que transforma los grados Farhenheit a Celsius")
    farhenheit=input("Ingresar los grados Farenheit\n\t")
    print("\t",farhenheit,"°F","equivalen a",gfar_gcel(farhenheit),"°C")
    print("Fin del programa")

    
if seleccion == "D":
    #Poner la función °C a °F
    print("Programa que transforma los grados Celsius a Farhenheit")
    celsius=input("Ingresar los grados Celsius\n\t")
    print("\t",celsius,"°C equivalen a",gcel_gfar(celsius),"°F")
    print("Fin del programa")
    
