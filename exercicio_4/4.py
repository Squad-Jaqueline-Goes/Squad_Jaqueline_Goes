'''
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