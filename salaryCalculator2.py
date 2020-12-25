# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salary = float(input("Please, inform your hourly income: "))
hours = float(input("Please, inform the number of hours worked on this month: "))
grossSalary = salary * hours
ir = grossSalary * 0.11
inss = grossSalary * 0.08
laborUnion = grossSalary * 0.05
netSalary = grossSalary - ir - inss - laborUnion

print("+ Salário Bruto : R$ {}.".format(grossSalary))
print("- IR (11%) : R$ {}.".format(ir))
print("- INSS (8%) : R$ {}.".format(inss))
print("- Sindicato ( 5%) : R$ {}.".format(laborUnion))
print("= Salário Liquido : R$ {}.".format(netSalary))