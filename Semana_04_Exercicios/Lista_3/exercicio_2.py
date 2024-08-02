'''Faça um Programa que peça as quatro notas de 5 alunos,
calcule e armazene numa lista a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.'''

aluno = 1
medias = []
media7 = 0

while aluno <= 5:
  nota1 = float(input(f'Insira a primeira nota do aluno {aluno}: '))
  nota2 = float(input(f'Insira a segunda nota do aluno {aluno}: '))
  nota3 = float(input(f'Insira a terceira nota do aluno {aluno}: '))
  nota4 = float(input(f'Insira a quarta nota do aluno {aluno}: '))
  notas = (nota1 + nota2 + nota3 + nota4)/4
  medias.append(notas)
  aluno +=1

for i in medias:
  if i >= 7.0:
    media7 += 1

print(f'O número de alunos com média maior ou igual a 7.0 é: {media7}')