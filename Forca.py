import random

def vencedor():
    print("\nParabens, você venceu!")

def perdedor(word):
    print("Poxa, não foi dessa vez")

def marcarChute(chute,letras_acertadas, word):
    i = 0
    for letra in word:
        if chute == letra:
            letras_acertadas[i] = letra
        i +=1    

def pedirChute():
    chute = str(input("\nDigite uma letra: \n"))
    chute = chute.strip().upper()
    return chute

def introducao():
    print("|--------------------",end="| \n")
    print("|---Jogo da Forca!---",end="| \n")
    print("|--------------------",end="| \n")

def caixaPalavra(word):
    return ["_"for letra in word]

def carregar_palavra_secreta():
    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()    
   
    numero = random.randrange(0,len(palavras))
    word = palavras[numero].upper()
    return word


def jogar():
    introducao()
    word = carregar_palavra_secreta()
    letras_acertadas = caixaPalavra(word)
    print("\n")
    print(letras_acertadas)

    perdeu = False
    venceu = False
    erros = 0
    
    while (not perdeu and not venceu):
        chute = pedirChute()

        if chute in word:
            marcarChute(chute,letras_acertadas,word)
        else:
            erros += 1

        perdeu = erros == 4
        venceu = "_" not in letras_acertadas
        print(letras_acertadas)
        
    if venceu:
        vencedor()
    else:
        perdedor()



if __name__ == "__main__":
    jogar()
