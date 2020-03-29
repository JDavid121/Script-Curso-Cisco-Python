"""
Programa que convierte millas de kilometros y viceversa
"""
"""
1 milla = 1.61 km
"""
#Programa que transforma millas a kilometros
#******************************************************************
print("Programa que transforma millas a kilometros")
mile = input("Ingresar la distancia en millas\n\t")
mile=float(mile)
print("La distancia ingresada en millas es...",mile)
mile_to_kilometers = mile*1.61 # Transformación de millas a km
print(mile,"millas equivalen a",round(mile_to_kilometers,3),"kilometros")
print("Fin del programa")
print()
print("Programa que transforma kilometros a millas")
kilometer = input("Ingresar la distancia en kilometros\n\t")
kilometer=float(kilometer)
print("La distancia ingresada en kilometros es...",kilometer)
kilometers_to_mile = kilometer/1.61 #Transformación de km a millas
print(kilometer,"kilómetros euivalen a",round(kilometers_to_mile,3),"millas")
print("Fin del programa")
#Programa que transforma de grados ceisius a farhenheit
#******************************************************************
# expresión °C = (°F-32°)*(5/9)
print("Programa que transforma los grados Farhenheit a Celsius")
farhenheit=input("Ingresar los grados Farenheit\n\t")
farhenheit=float(farhenheit)
farhenheit=round(farhenheit,3) #Redondeamos la entrada a 3 decimales
print("\tLos grados farhenheit ingresados son",farhenheit,"°F")
celsius_to_farh=(farhenheit-32)*(5/9) #Transformación de grados farhenheit a celsius
celsius_to_farh=round(celsius_to_farh,3)
print("\t",farhenheit,"°F","equivalen a",celsius_to_farh,"°C")
print("Fin del programa")
print()
print("Programa que transforma los grados Celsius a Farhenheit")
celsius=input("Ingresar los grados Celsius\n\t")
celsius=float(celsius)
celsius=round(celsius,3) #Redondeando la entrada a 3 decimales.
farh_to_celsius=32+(9/5)*celsius
farh_to_celsius=round(farh_to_celsius,3)
print("\t",celsius,"°C equivalen a",farh_to_celsius,"°F")
print("Fin del programa")


