'''
Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h

'''

def calcular_tempo_viagem(distancia, velocidade):
   
    return distancia / velocidade

def main():
    # Velocidades em km/h
    velocidade_aviao = 600
    velocidade_carro = 100
    velocidade_onibus = 80

    # Solicitar a distância da viagem
    distancia = float(input("Digite a distância da viagem em quilômetros: "))

    # Calcular o tempo de viagem para cada meio de transporte
    tempo_aviao = calcular_tempo_viagem(distancia, velocidade_aviao)
    tempo_carro = calcular_tempo_viagem(distancia, velocidade_carro)
    tempo_onibus = calcular_tempo_viagem(distancia, velocidade_onibus)

    # Exibir os resultados
    print(f"\nPara uma viagem de {distancia} km:")
    print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
    print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
    print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")

if __name__ == "__main__":
    main()
