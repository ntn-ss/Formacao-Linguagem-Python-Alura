import forca
import adivinhacao

def escolheJogo():
    print("*********************************")
    print('****** Escolha o seu jogo! ******')
    print("*********************************")

    jogo = int(input("{1} - Forca\n{2} - Adivinhação\n"))

    if (jogo==1):
        print("Jogando Forca.")
        forca.jogar()
    if (jogo==2):
        print("Jogando Adivinhação.")
        adivinhacao.jogar()

if (__name__=="__main__"):
    while (True):
        escolheJogo()