'''
Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
'''

from datetime import datetime # módulo para manipulação de datas e horas

ano_atual = datetime.now().year # Obtém a data e hora atuais e extrai o ano atual
ano_nascimento = int(input('Digite o ano do seu nascimento (XXXX): '))
idade = ano_atual - ano_nascimento

if idade < 0:
    print('Você não nasceu ainda')
elif idade > 120:
    print('Provavelmente você não é tão velho assim')
else:
    print(f'A sua idade atual é: {idade}')
