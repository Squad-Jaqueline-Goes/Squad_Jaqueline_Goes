'''
O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''

pares = 0
impares = 0

while True:
    numero = int(input("Digite um numero (0 para sair): "))
    if numero == 0:
        break

    if numero < 0:
        print('Insira somente numeros positivos!')
        continue

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
