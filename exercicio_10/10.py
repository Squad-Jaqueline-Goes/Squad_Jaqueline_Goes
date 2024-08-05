'''
Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.
Lembrando que para o retorno vamos usar print com as variáveis
criadas e este texto é somente um exemplo, utilizem a criatividade
'''

# Solicita as variáveis ao usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite a cidade onde você mora: ")
profissao = input("Digite sua profissão: ")

# Exibe a mensagem amigável usando as variáveis
print(f"\nOlá, {nome}! É um prazer te conhecer.")
print(f"Vejo que você tem {idade} anos e mora em {cidade}.")
print(f"Como é trabalhar como {profissao}? Deve ser bem interessante!")