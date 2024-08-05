'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
'''

while True:
    try:
        nota = float(input('Informe uma nota de 0 a 10: '))

        if 0 <= nota <= 10:
            break  # Saia do loop se a nota for válida
        else:
            print('Valor inválido. A nota deve estar entre 0 e 10.')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.')

print(f'Nota inserida: {nota:.1f}')  # Formatação para uma casa decimal, caso tenha