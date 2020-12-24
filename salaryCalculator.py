# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salary = float(input("Please, inform your hourly income: "))
hours = float(input("Please, inform the number of hours worked on this month: "))
totalSalary = salary * hours
print("This month salary is {}.".format(totalSalary))