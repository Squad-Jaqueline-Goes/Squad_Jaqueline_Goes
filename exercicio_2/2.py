'''
Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
'''
def reverso_numero(numero):
    # Converter o número para string
    numero_str = str(numero)
    
    # Reverter a string
    numero_reverso_str = numero_str[::-1]
    
    numero_reverso = int(numero_reverso_str)
    
    return numero_reverso

# Exemplo de uso
numero = 127
print(f"O reverso de {numero} é {reverso_numero(numero)}")
