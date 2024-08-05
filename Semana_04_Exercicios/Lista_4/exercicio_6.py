#6. Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, um para cada letra
#da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presentena palavra secreta, ela será revelada nas posições correspondentes. Se
#a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.


import random

def escolher_palavra():
    """Escolhe uma palavra aleatória de uma lista de palavras."""
    palavras = ["python", "desenvolvedor", "programacao", "jogo", "computador"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    """Retorna a palavra com as letras corretas reveladas e os espaços em branco para letras não adivinhadas."""
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

def jogar():
    palavra_secreta = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra.")
    
    while tentativas_restantes > 0:
        print("\nPalavra: ", exibir_palavra(palavra_secreta, letras_corretas))
        print("Letras erradas: ", ' '.join(letras_erradas))
        print(f"Tentativas restantes: {tentativas_restantes}")

        palpite = input("Digite uma letra: ").lower()
        
        if palpite in letras_corretas or palpite in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if palpite in palavra_secreta:
            letras_corretas.add(palpite)
            if set(palavra_secreta) == letras_corretas:
                print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
                break
        else:
            letras_erradas.add(palpite)
            tentativas_restantes -= 1
            if tentativas_restantes == 0:
                print(f"Você perdeu! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogar()
