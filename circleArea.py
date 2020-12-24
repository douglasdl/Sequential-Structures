# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
PI = 3.14159265358979323846
radius = float(input("Please, inform the radius of the circle: "))
area = PI * pow(radius, 2)
print("R: {}".format(area))