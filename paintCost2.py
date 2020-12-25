# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

oneLcoverage = 6
paintCanVolume = 18
paintCanPrice = 80.00
paintCanCoverage = paintCanVolume * oneLcoverage
paintGallonVolume = 3.6
paintGallonPrice = 25.00
paintGallonCoverage = paintGallonVolume * oneLcoverage

area = float(input("Please, inform the paint area (m2): "))
area = area * 1.1

onlyCans = math.ceil(area / paintCanCoverage)
onlyGallons = math.ceil(area / paintGallonCoverage)
bestChoiceCans = math.ceil(area / paintCanCoverage)
if area % paintCanCoverage == 0:
    bestChoiceGallons = 0
else:
    bestChoiceGallons = (area % paintCanCoverage)

cost1 = onlyCans * paintCanPrice
cost2 = onlyGallons * paintGallonPrice
cost3 = onlyCans

print("You can choose one of the following options:")
print("1. You will need {} cans. An you will spend R${}".format(onlyCans, cost1))
print("2. You will need {} gallons. An you will spend R${}".format(onlyGallons, cost2))
print("3. You will need {} cans and {} gallons. An you will spend R${}".format(bestChoiceCans, paintCanCoverage, cost3))