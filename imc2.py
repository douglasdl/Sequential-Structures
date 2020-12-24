# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

height = float(input("Please, inform your height: "))
sex = input("Please, inform your gender (F / M): ")
if sex == "F":
    imc = (62.1 * height) - 44.7
else:
    imc = (72.7 * height) - 58
print("IMC: {}".format(imc))
