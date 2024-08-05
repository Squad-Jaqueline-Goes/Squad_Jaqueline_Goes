'''
<<<<<<< HEAD
Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
'''

carrinho_compras = {}
carrinho_compras['caneta'] = 4.9
carrinho_compras['borracha'] = 2.5
carrinho_compras['caderno'] = 44.9
carrinho_compras['lapiseira'] = 14.35

total_compra = 0

for valor in carrinho_compras.values():
    total_compra += valor

print(f'O valor total da compra foi de R${total_compra :.2f}')
=======
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
>>>>>>> main
