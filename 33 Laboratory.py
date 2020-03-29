"""
Scenario
Miles and kilometers are units of length or distance.

Bearing in mind that 1 mile is equal to approximately 1.61 kilometers,
complete the program in the editor so that it converts:

miles to kilometers;
kilometers to miles.
Do not change anything in the existing code.
Write your code in the places indicated by ###.
Test your program with the data we've provided in the source code.

"""

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61                        #transformamos las millas a km al multiplicar las millas por 1.61
kilometers_to_miles = kilometers/1.61                   #transformamos los km a millas al dividir los km para 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
