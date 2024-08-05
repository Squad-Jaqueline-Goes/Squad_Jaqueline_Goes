'''
Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.

Extra: Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão
correta.

'''

def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("Escolha a conversão desejada:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    escolha = input("Digite o número da sua escolha (1 ou 2): ")

    if escolha == '1':
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit}°F")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius}°C")
    else:
        print("Escolha inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
