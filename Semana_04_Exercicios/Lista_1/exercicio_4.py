'''
Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.
'''

combustivel_consumido = float(input('Informe a quantidade de litros de combustível consumido: '))
distancia_percorrida = float(input('Informe a distância percorrida em quilômetros: '))

consumo_medio = distancia_percorrida/combustivel_consumido

print(f'O consumo médio foi de {consumo_medio:.2f}km/l')