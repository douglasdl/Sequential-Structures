# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

Fahrenheit = float(input("Please, inform the temperature (°F): "))
Celsius = 5 * ((Fahrenheit - 32) / 9)
print("{}°F = {}°C".format(Fahrenheit, Celsius))


Fahrenheit = float(input("Please, inform the temperature (°C): "))
Celsius = (Fahrenheit * 9 / 5) + 32
print("{}°F = {}°C".format(Fahrenheit, Celsius))