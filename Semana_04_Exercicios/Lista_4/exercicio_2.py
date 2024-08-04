''' Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721.
'''

def reverter_numero(numero):
    
    numero_str = str(numero)
    
    # Reverte a string
    numero_reverso_str = numero_str[::-1]
    
    # Converte a string revertida de volta para um número inteiro
    numero_reverso = int(numero_reverso_str)
    
    return numero_reverso


numero = 127
print(f"Reverso de {numero} é {reverter_numero(numero)}")
