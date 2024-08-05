'''
Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''
salarioBruto = float(input('Informe o salário bruto: '))

while salarioBruto <= 0:
  print('Salario inválido, favor inserir um valor maior do que 0.')
  salarioBruto = float(input('Informe o salário bruto: '))

if salarioBruto <= 1903.98:
  print(f'Isento de imposto de renda. O salário líquido é R$ {salarioBruto}.')

elif salarioBruto > 1903.98 and salarioBruto <= 2826.65:
  aliquota = (salarioBruto*7.5)/100
  salarioLiquido = salarioBruto - aliquota
  print(f'A alíquota do Imposto de Renda é 7,5%. O salário líquido é R$ {salarioLiquido}.')

elif salarioBruto > 2826.65 and salarioBruto <= 3751.05:
  aliquota = (salarioBruto*15)/100
  salarioLiquido = salarioBruto - aliquota
  print(f'A alíquota do Imposto de Renda é 15%. O salário líquido é R$ {salarioLiquido}.')

elif salarioBruto > 3751.05 and salarioBruto <= 4664.68:
  aliquota = (salarioBruto*22.5)/100
  salarioLiquido = salarioBruto - aliquota
  print(f'A alíquota do Imposto de Renda é 22,5%. O salário líquido é R$ {salarioLiquido}.')

else:
  aliquota = (salarioBruto*27.5)/100
  salarioLiquido = salarioBruto - aliquota
  print(f'A alíquota do Imposto de Renda é 27,5%. O salário líquido é R$ {salarioLiquido}.')