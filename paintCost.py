# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

oneLcoverage = 3
paintCanVolume = 18
paintCanPrice = 80.00
paintCanCoverage = paintCanVolume * oneLcoverage

area = float(input("Please, inform the paint area (m2): "))

requiredCans = math.ceil(area / paintCanCoverage)
print("You will need {} cans.".format(requiredCans))
