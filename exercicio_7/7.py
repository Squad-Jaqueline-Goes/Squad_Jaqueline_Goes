'''
<<<<<<< HEAD
Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
'''

idade = int(input('Digite a sua idade: '))

if idade < 0:
    print('\nVocê ainda está a caminho!')
elif idade > 120:
    print('\nPara esta idade, você deve ser um dinossauro')
elif idade <= 12:
    print('\nOlá Criança, não esqueça de brincar hoje!')
elif idade > 12 and idade <= 18:
    print('\nOlá Adolescente, não esqueça de estudar')	
elif idade > 18 and idade <= 60:
    print('\nOlá Adulto, não esqueça de pagar os boletos')
else:
    print('\nIdoso, não esqueça de tomar os remédios')
=======
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
'''

peso = float(input('Qual o Seu peso em Kg? : '))
altura = float(input('Qual a sua Altura em Metros? : '))
IMC = peso / (altura * altura)
print(f'O seu Indice De Massa Corporal é: {IMC}')
>>>>>>> a4500e2f5ad032ad0cdfbc63c5f5c5ec1388d01a
