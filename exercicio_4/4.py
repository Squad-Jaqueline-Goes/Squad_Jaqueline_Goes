'''
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21
'''

def leitura_dinheiro_carteira():
    dinheiro_carteira = -1
    while dinheiro_carteira < 0:
        try:
            dinheiro_carteira = float(input('\nDigite quanto dinheiro você tem na carteira: R$ '))
        except ValueError as e:
            print(f'\nErro: O tipo do dado informado esta incorreto.')  
            dinheiro_carteira = -1
        if dinheiro_carteira < 0:
            print('Digite um valor válido')
    return dinheiro_carteira

def conversao_dinheiro(dinheiro_carteira):
    conversao = {'Dolar Americano': 4.91, 'Peso Argentino': 0.02, 'Dolar Australiano': 3.18, 'Dolar Canadense': 3.64, 'Franco Suico': 0.42, 'Euro': 5.36, 'Libra Esterlina': 6.21}
    print(f'\nVocê pode comprar:')
    for moeda, valor in conversao.items():
        print(F' - {moeda}: {dinheiro_carteira/valor:.2f}')


dinheiro_carteira = leitura_dinheiro_carteira()
conversao_dinheiro(dinheiro_carteira)