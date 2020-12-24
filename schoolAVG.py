# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

grade1 = input("Please, inform the first grade: ")
grade2 = input("Please, inform the second grade: ")
grade3 = input("Please, inform the third grade: ")
grade4 = input("Please, inform the fourth grade: ")
avg = (float(grade1) + float(grade2) + float(grade3) + float(grade4)) / 4
print("The average is {}".format(avg))
