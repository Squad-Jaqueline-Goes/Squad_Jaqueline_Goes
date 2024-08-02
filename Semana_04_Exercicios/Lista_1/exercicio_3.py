***
 Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.
***

# Solicita ao usuário a quantidade de quilômetros
quilometros = float(input("Digite a quantidade de quilômetros: "))

# Converte para metros, centímetros e milímetros
metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

# Exibe os resultados
print(f"{quilometros} quilômetros é equivalente a:")
print(f"{metros} metros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")
