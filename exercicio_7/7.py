'''
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