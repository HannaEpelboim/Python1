#Jogo NIM

#entrada dos números
# n --> número de peças inicial
# m --> número máximo de peças que podem ser removidas por rodada
def partida():
    n = 0
    m = 0
    y = False
    while n <= 0 or m >= n or m >= n: #n tem que ser maior ou igual a um e m, menor ou igual a n
        n = int(input("Quantas peças?"))
        m = int(input("Limite de peças por jogada?"))

    #precisamos decidir se o computador começa ou o usuario. O usuario começa se n é multiplo de (m + 1), caso contrário o computador começa
    resto = n % (m + 1)

    if resto == 0:#usuario começa
        print ("Você começa!")
        print()
        usuario_escolhe_jogada(n, m)
        if not y: #jogo continua!!!
            while y == False:
                computador_escolhe_jogada(n, m)
                if not y: #jogo continua!!!
                    usuario_escolhe_jogada(n, m)
                
            

    else:
        print("Computador começa!")
        print() #para pular linha
        computador_escolhe_jogada(n, m)
        if not y: #jogo continua!!!
            usuario_escolhe_jogada(n, m)
            if not y: #jogo continua!!!
                computador_escolhe_jogada(n, m)
        
def computador_escolhe_jogada(n, m):
    # o objetivo é deixar um multiplo de (m + 1)
    # formula para isso...
    # x é número de peças removidas...
    resto = n % m

    resto += 1
    n = n - resto

    print("O computador tirou %d peças" %(resto))

    #Se o computador ganhar e se ainda tiver peças
    if n != 0:
        print("Agora restam %d peças" %(n))
        y = False
    else:
        print("Fim de jogo! O computador ganhou!")
        y = True
        ###fazer contagem###

    return (n, m)

def usuario_escolhe_jogada(n, m):
    #sempre perde, mas as escolhas são do usuario!
    remover = 0
    while remover < 1 and m > remover: #caso usuario ponha valores que não permitam o jogo vai pedir de novo as infos.
        # remover diz quantas peças o usuario tirou
        remover = int(input("Quantas peças você vai tirar?"))
        print("Você tirou %d peças" %(remover))
    #Se ainda tiverem peças e se o usuario ganhar
    pecas_restantes = n - remover
    return pecas_restantes
    if pecas_restantes != 0:
        print("Agora restam %d peças no tabuleiro" %(pecas_restantes))
        y = False
    else: #nunca vai acontecer
        y = True
        print("Fim de jogo! Você ganhou")


#MELHOR DE TRES
def campeonato():
    n = 0
    while n < 3:
        partida()
        n = n+1


#chamada do joguinho

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    n = 0
    while n != 1 and n != 2:
        n = int(input())

    if n == 1:
        partida()

    if n == 2:
        campeonato()


if __name__ == '__main__':
    main()




#contador
def contador():
    

        

    


    

