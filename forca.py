import random

def jogar():

    print("**************************")
    print('Bem-vindo ao jogo "Forca"!')
    print("**************************")

    palavraSecreta = "banana".upper()

    #limite é o número de vezes que o jogo rodará.
    nivel = int(input("Escolha o seu nível de dificuldade:\n{1} - Fácil (20 tentativas)\n{2} - Médio (10 tentativas)\n{3} - Difícil (5 tentativas)\n"))
    if(nivel==1):
        limite=20
    elif (nivel==2):
        limite=10
    else:
        limite=6


    letrasAcertadas = []
    erros = 0

    ganhou = False
    perdeu = False

    for letra in palavraSecreta:
        letrasAcertadas.append("_")
    
    print(letrasAcertadas)

    while (not perdeu and not ganhou):
        chute = input("Digite uma letra. ")
        chute = chute.strip().upper()

        if (chute in palavraSecreta):
            index = 0
            for letra in palavraSecreta:
                if (chute.upper() == letra.upper()):
                    letrasAcertadas[index] = chute.lower()
                index += 1

        else:
            erros += 1
            print("Você errou {} vezes.".format(erros))

        perdeu = erros == limite
        ganhou = "_" not in letrasAcertadas
        print(letrasAcertadas, "\n", sep="")

    if perdeu:
        print('Você perdeu! A palavra secreta era "{}".'.format(
            palavraSecreta.lower()))

    else:
        print("Você ganhou! Meus parabéns.")


if (__name__ == "__main__"):
    while (True):
        jogar()