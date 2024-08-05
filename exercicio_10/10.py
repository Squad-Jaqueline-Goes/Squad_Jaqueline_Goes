'''
Faça um programa que lê três números inteiros e os mostra em ordem
crescente.
'''

entrada_1 = int(input('Digite o primeiro numero: '))
entrada_2 = int(input('Digite o segundo numero: '))
entrada_3 = int(input('Digite o terceiro numero: '))

numeros = [entrada_1, entrada_2, entrada_3]

ordem = sorted(numeros) # Ordena a lista em ordem crescente

print('Os números em ordem crescente são: ', ordem)
