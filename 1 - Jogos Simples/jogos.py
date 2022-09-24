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
    
    elif (jogo==2):
        print("Jogando Adivinhação.")
        adivinhacao.jogar()
        
    else:
        print("Escolha corretamente.")

if (__name__=="__main__"):
    while (True):
        escolheJogo()