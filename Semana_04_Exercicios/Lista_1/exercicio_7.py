'''
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
'''

# entrada de dados
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# saida de dados (IMC do ususario)
imc = peso / (altura * altura)
print(f"Seu IMC é de {imc:.2f}")