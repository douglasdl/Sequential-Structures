# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

number1 = int(input("Please, inform an Integer number: "))
number2 = int(input("Please, inform an Integer number: "))
number3 = float(input("Please, inform a Real number: "))
calc1 = (number1 * 2) * (number2 / 2)
calc2 = (number1 * 3) + number3
calc3 = pow(number3, 3) 
print("1: {}".format(calc1))
print("2: {}".format(calc2))
print("3: {}".format(calc3))