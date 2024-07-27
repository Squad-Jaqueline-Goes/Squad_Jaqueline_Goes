'''
Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
 - equilátero: todos os lados com o mesmo valor
 - isósceles: dois lados com o mesmo valor
 - escaleno: todos os lados com medidas distintas.
'''

# entrada de dados
a = int(input("Digite o comprimento do lado A do triângulo: "))
b = int(input("Digite o comprimento do lado B do triângulo: "))
c = int(input("Digite o comprimento do lado C do triângulo: "))

if ((a == b) and (b == c)):
          print("O triângulo digitado é EQUILÁTERO")
elif ((a == b) or (a == c) or (b == c)):
          print("O triângulo digitado é ISÓSCELES")
else:
          print("O triângulo digitado é ESCALENO")