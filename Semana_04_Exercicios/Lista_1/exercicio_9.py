'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, 
considerando uma média de 5 calorias por minuto de exercício.
'''
# Função para calcular o total de calorias queimadas em um mês
def calcular_calorias_por_mes(horas_por_semana):
    calorias_por_minuto = 5
    minutos_por_hora = 60
    semanas_por_mes = 4  
    
    # Converter horas por semana para minutos
    minutos_por_semana = horas_por_semana * minutos_por_hora
    
    # Calcular calorias queimadas por semana
    calorias_por_semana = minutos_por_semana * calorias_por_minuto
    
    # Calcular calorias queimadas em um mês
    calorias_por_mes = calorias_por_semana * semanas_por_mes
    
    return calorias_por_mes

# Solicitar o número de horas de exercício físico por semana ao usuário
horas_por_semana = float(input("Digite o número de horas de exercício físico por semana: "))

# Calcular o total de calorias queimadas em um mês
total_calorias = calcular_calorias_por_mes(horas_por_semana)

# Exibir o resultado
print(f"Total de calorias queimadas em um mês: {total_calorias:.2f} calorias")
