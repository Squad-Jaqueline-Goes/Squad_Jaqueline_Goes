#6. Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.Levando em consideração: ● avião = 600 km/h ● carro = 100 km/h ● ônibus = 80 km/h

# Função para calcular o tempo de viagem
def calcular_tempo(distancia, velocidade):
    return distancia / velocidade

# Dados de entrada
distancia = float(input("Digite a distância da viagem em quilômetros: "))

# Velocidades dos diferentes meios de transporte
velocidade_aviao = 600  # km/h
velocidade_carro = 100  # km/h
velocidade_onibus = 80  # km/h

# Cálculo do tempo para cada meio de transporte
tempo_aviao = calcular_tempo(distancia, velocidade_aviao)
tempo_carro = calcular_tempo(distancia, velocidade_carro)
tempo_onibus = calcular_tempo(distancia, velocidade_onibus)

# Impressão dos resultados
print(f"\nPara uma viagem de {distancia} km:")
print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")

# Comparativo
print("\nComparativo:")
if tempo_aviao < tempo_carro and tempo_aviao < tempo_onibus:
    print("O avião é o meio de transporte mais rápido.")
elif tempo_carro < tempo_aviao and tempo_carro < tempo_onibus:
    print("O carro é o meio de transporte mais rápido.")
else:
    print("O ônibus é o meio de transporte mais rápido.")

