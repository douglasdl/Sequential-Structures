# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

side = float(input("Please, inform length of the square side: "))
area = pow(side, 2)
doubleArea = 2 * area 
print("R: {}".format(doubleArea))
