import random


def jogar():

    imprime_mensagem()
    palavra_secreta = gerar_palavras()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    #enquanto não enforcou e não acertou.
    while(not enforcou and not acertou):
        chute = pede_chute()
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        mensagem_final_vencedor()
    else:
        mensagem_final_perdedor()



def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def mensagem_final_vencedor():
    print("Você ganhou.")

def mensagem_final_perdedor():
    print("Lixo")

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def imprime_mensagem():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")

def gerar_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if(__name__ == "__main__"):
    jogar()