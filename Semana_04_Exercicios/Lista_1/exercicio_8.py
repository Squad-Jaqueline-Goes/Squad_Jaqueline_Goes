'''
Cálculo de Salário: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

# multiplicando o valor ganho por hora pelo número de horas trabalhadas no mês.

salario_hora = float(input('Quanto você ganha por hora? : '))
horas_trabalhadas = float(input('O Quanto de horas trabalhadas você faz? : '))
valor = salario_hora * horas_trabalhadas
print(f'O seu salario referido do mês é: {valor:.2f}')