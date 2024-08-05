'''
<<<<<<< HEAD
Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
'''
#Cria um dicionário com contatos e números de telefone
listaTelefonica = {'Yuumi': 21997282624, 'Jinshi': 21966252432, 'Ahri': 11966504223, 'Jinx': 35966789452}

#Solicita ao usuário o nome do contato que ele deseja buscar e converte para letras minúsculas.
nome = input('Insira o nome de contato que deseja procurar: ').strip().lower()

contatoEncontrado = False

#Itera sobre as chaves do dicionário
for chave in listaTelefonica:
  if chave.lower() == nome: #Compara a chave convertida para minúsculo com a entrada do usuário.
    print(f'{chave}: {listaTelefonica[chave]}')
    contatoEncontrado = True
    break

#Se o usuário não for encontrado exibe uma mensagem.
if not contatoEncontrado:
  print('Esse contato não está na lista telefônica.')
=======
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
>>>>>>> main
