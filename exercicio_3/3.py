'''
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
