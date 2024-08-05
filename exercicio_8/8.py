'''
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês.
'''

# entrada de dados
valor_hora = float(input("Digite o valor da sua hora trabalhada: "))

hora_trabalhada = int(input("Digite quantas horas você trabalha por dia: "))

valor_total = valor_hora * hora_trabalhada

# saida de dados
print(f" O seu salário no final do mês é de R${valor_total:.2f}")