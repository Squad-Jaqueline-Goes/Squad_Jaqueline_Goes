'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

print('\nM - Matutino')
print('V - Vespertino')
print('N - Noturno')
turno = input('Digite o turno que você estuda: ').upper()

if turno == 'M':
    print('\nBom Dia! Que seu dia seja produtivo e cheio de energia para os estudos!')
elif turno == 'V':
    print('\nBoa Tarde! Espero que esteja aproveitando bem o seu dia de estudos!')
elif turno == 'N':
    print('\nBoa Noite! Que você tenha um ótimo descanso após uma boa sessão de estudos!')
else:
    print('\nValor Inválido! Por favor, escolha um valor válido (M, V ou N)')
