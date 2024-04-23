import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
       _ = system('clear')

def game():
    limpa_tela()
    print("Bem vindo ao jogo da forca!")
    print("Advinhe a palavra abaixo: \n")

palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
palavra_secreta = random.choice(palavras)

letras_descobertas = ['_' for letra in palavra_secreta]
chances =  6
letras_erradas = []

# loop
while chances > 0:
    print(" ".join(letras_descobertas))
    print("\nChances restantes: ", chances)
    print("Letras erradas: ", " ".join(letras_erradas))

    tentativa = input("\nDigite uma letra: ").lower()

    if tentativa in palavra_secreta:
        index = 0
        for letra in palavra_secreta:
            if tentativa == letra:
                letras_descobertas[index] = letra
            index += 1
    else:
        chances -= 1
        letras_erradas.append(tentativa)

    if "_" not in letras_descobertas:
        print("\nVocê venceu, a palavra era: ", palavra_secreta)
        break
