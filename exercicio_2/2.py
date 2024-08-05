'''
Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

entrada = str(input('Em qual turno você estuda?: '))

if entrada == 'M':
    print('Bom dia!')

elif entrada == 'V':
    print('Boa Tarde!')

elif entrada == 'N':
    print('Boa Noite!')

else:
    print('Invalido!')
