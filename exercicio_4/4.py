'''
Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado
'''

print("Bem-vindo(a) ao sistema de classificação de alunos!")

while True:
   
    nota = float(input("Digite a nota do aluno(a) (de 0 a 10): "))
 
    if 0 <= nota <= 10:
        if nota >= 7:
            print(f"Nota {nota}: Aluno(a) aprovado!")
        else:
            print(f"Nota {nota}: Aluno(a) reprovado.")
        break  # Sai do loop se a nota for válida
    else:
        print("Valor inválido. A nota deve estar entre 0 e 10. Tente novamente.")
