import forca
import main

def escolhe_jogo():
    print("****************")
    print("Qual o seu jogo? ")
    print("****************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogar adivinhação.")
        main.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()