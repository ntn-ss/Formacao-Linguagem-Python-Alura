import random

def jogar():
    global chute

    saudacoes()

    dificuldade()

    escolhePalavra()
    
    letrasAcertadas = ["_" for letra in palavraSecreta]
    
    erros = 0

    ganhou = False
    perdeu = False
    
    print(letrasAcertadas)

    while (not perdeu and not ganhou):
        chute = pedeChute()

        if (chute in palavraSecreta):
            marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta)

        else:
            erros += 1
            print("Você errou {} vezes.".format(erros))

        perdeu = erros == limite
        ganhou = "_" not in letrasAcertadas
        print(letrasAcertadas, "\n", sep="")

    if perdeu:
        print('Você perdeu! A palavra secreta era "{}".'.format(palavraSecreta.lower()))

    else:
        print("Você ganhou! Meus parabéns.")

def saudacoes():
    print("**************************")
    print('Bem-vindo ao jogo "Forca"!')
    print("**************************")

def dificuldade():
    #limite é o número de vezes que o jogo rodará.
    global limite

    nivel = int(input("Escolha o seu nível de dificuldade:\n{1} - Fácil (20 tentativas)\n{2} - Médio (10 tentativas)\n{3} - Difícil (5 tentativas)\n"))
    if(nivel==1):
        limite=20
    elif (nivel==2):
        limite=10
    else:
        limite=6

def escolhePalavra():
    global palavraSecreta

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta

def pedeChute():
    chute = input("Digite uma letra. ")
    chute = chute.strip().upper()
    return chute

def marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta):
    index = 0
    for letra in palavraSecreta:
        if (chute.upper() == letra.upper()):
            letrasAcertadas[index] = chute.lower()
        index += 1

if (__name__ == "__main__"):
    while (True):
        jogar()