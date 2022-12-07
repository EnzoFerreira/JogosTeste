import Forca
import Adivinhacao


def escolhe_jogo():
    print("|----------------------------",end="| \n")
    print("|Bem vindo, escolha seu jogo:",end="| \n")
    print("|----------------------------",end="| \n")

    print("(1)Jogo da Forca  |  (2)Jogo de adivinhação\n")
    jogo=int(input("Qual sua escolha?\n"))

    if jogo ==1:
        print("jogo da Forca\n")
        Forca.jogar()
    elif jogo ==2:
        print("Jogo de adivinhação\n")
        Adivinhacao.jogar()
    

if __name__ == "__main__":
    escolhe_jogo()