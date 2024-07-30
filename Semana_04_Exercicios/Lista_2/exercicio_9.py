'''
O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''
num = 1
numeros_pares = 0
numeros_impares = 0

while(num != 0):
    num = int(input("Insira um número: "))
    if (num > 0):
        if (num%2 == 0):
            numeros_pares += 1
        else:
            numeros_impares += 1

print(f'Foram inseridos {numeros_pares} números pares e {numeros_impares} números ímpares.')