#Início
import random

def jogar():

    #numeroSecreto é um número aleatório sorteado entre 0 e 100. Maior e menos são o início e o fim do intervalo.
    numeroSecreto = random.randrange(1,101)

    pontos = 1000

    numMin = 0
    numMax = 100

    print("********************************")
    print('Bem-vindo ao jogo "Adivinhação"!')
    print("********************************")

    nivel = int(input("Escolha seu nível de dificuldade:\n{1} - Fácil (20 tentativas)\n{2} - Médio (10 tentativas)\n{3} - Difícil (5 tentativas)\n"))

    #tentativas é o número de vezes que o jogo rodará.
    if(nivel==1):
        tentativas=20

    elif (nivel==2):
        tentativas=10
    
    else:
        tentativas=5



    #O último item do range é apagado, por isso o +1.

    for rodada in range(1, tentativas+1):

        #Interpolação de string.
        print("Tentativa {} de {}.".format(rodada, tentativas))
        print("Digite algo entre {} e {}.".format(numMin, numMax))

        #O comando input retorna uma string por padrão, e nosso cálculo precisa de um número inteiro.
        chuteStr = input("Digite o seu palpite: ")
        chute = int(chuteStr)

        #Retorno ao usuário e verificações internas.
        print("Você digitou {}.".format(chute))

        if (chute<numMin or chute>numMax):
            print("Digite algo entre {} e {}.".format(numMin, numMax))
            continue

        acertou = chute == numeroSecreto
        errMaior = chute > numeroSecreto
        errMenor = chute < numeroSecreto

        if (acertou):
            if (pontos==1):
                print("Você acertou e fez {} ponto!".format(pontos))
                break
            else:
                print("Você acertou e fez {} pontos!".format(pontos))
                break

        else:
            pontosPerdidos=abs(numeroSecreto-chute)
            pontos -= pontosPerdidos

            if (errMaior):
                print("Você errou! Seu chute foi maior que o número secreto.\n")
                numMax=chute

            elif (errMenor):
                print("Você errou! Seu chute foi menor que o número secreto.\n")
                numMin=chute

        if rodada < tentativas:
            rodada += 1

    if (acertou==False):
        print("Você perdeu, o número secreto era {}.".format(numeroSecreto))
        print("Fim de jogo!")

    else:
        print("Fim de jogo!")


if(__name__=="__main__"):
    while(True):
        jogar()