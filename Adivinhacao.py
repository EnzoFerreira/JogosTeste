import random

                    #versao com while loop 
#print("|-------------------",end="| \n")
#print("|Jogo da advinhação!",end="| \n")
#print("|-------------------",end="| \n")

#numero_secreto=43
#totalTentativas = 3
#rodada = 1

#while rodada <= totalTentativas:
#    print(f'Rodada: {rodada} de {totalTentativas}')
#    chute = int(input("Digite sua previsão: \n"))
#    print(f'Seu numero é {chute}?\n')
#    chuteN = int(chute)

#    acertou = chuteN == numero_secreto
#    maior = chuteN > numero_secreto
#    menor = chuteN < numero_secreto

#    if acertou:
#        print("Você acertou!\n")
#    else:   
#            if maior:
#               print("Você errou, chute muito alto!\n")
#           elif menor: 
#               print("Você errou, chute muito baixo!\n")

#   rodada = rodada +1
#else:
#    print("--Fim do jogo--")

#versao com for in
def jogar():

    print("|-------------------",end="| \n")
    print("|Jogo da advinhação!",end="| \n")
    print("|-------------------",end="| \n")

    numero_secreto = random.randrange(1,101)
    pontos=1000

    print("Qual o nível de dificuldade?\n")
    print("(1)Fácil  |  (2)Médio  |  (3)Difícil")
    nivel = int(input(f'Defina a dificuldade:\n '))

    if nivel == 1:
        totalTentativas=20
    elif nivel == 2:
        totalTentativas=10
    else:
        totalTentativas=5
    for rodada in range(1,totalTentativas+1):
        print(f'Rodada: {rodada} de {totalTentativas}')
        chute_str = int(input("Digite sua previsão: \n"))
        print(f'Seu numero é {chute_str}?\n')
        chute = int(chute_str)

        if chute <1 or chute >100:
            print("Você digitou um número invalido! tente novamente")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Você acertou e fez {pontos}\n')
            break
        else:   
            if maior:
                print("Você errou, chute muito alto!\n")
            elif menor: 
                print("Você errou, chute muito baixo!\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            
            


    else:
        print("--Fim do jogo--\n")
        print(f'O número secreto era {numero_secreto}!')
        print(f'Você fez {pontos} pontos!')

if __name__ == "__main__":
    jogar()
