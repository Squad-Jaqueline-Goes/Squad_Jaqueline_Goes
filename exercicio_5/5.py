'''
<<<<<<< HEAD
Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.

'''

lado1 = int(input('Informe o comprimento do primeiro lado do trinângulo: '))
lado2 = int(input('Informe o comprimento do segundo lado do trinângulo: '))
lado3 = int(input('Informe o comprimento do terceiro lado do trinângulo: '))

if lado1 == lado2 == lado3:
  print('Equilátero. Todos os lados são iguais.')

elif lado1 == lado2 != lado3:
  print('Isósceles. Um dos lados é diferente.')

else:
  print('Escaleno. Todos os lados são diferentes.')
