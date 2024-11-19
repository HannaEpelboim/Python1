# Jogo NIM

#o jogo em si: n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
#Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

def partida():
    #primeira parte: perguntar o número inicial de peças e máximo e garantir que ambos sejam jogáveis
    pecas = 0
    limite = 1
    while pecas<1 or limite>pecas: #o número inicial de peças deve ser maior ou igual a 1 e o limite deve ser menor que o número de peças.
        pecas = int(input("Quantas peças?"))
        limite = int(input("Limite de peças por jogada?"))
    
    #vamos decidir quem começa!
    definidor = pecas % (limite + 1) 
   
    #se pecas for múltiplo de (limite+1), ou seja, definidor == 0, o usuário começa
    if definidor == 0:
        print("")
        print("Você começa!")
        print('')
        
    #caso contrário, computador começa
    else: 
        print('')
        print("Computador começa!")
        print('')
        computador_escolhe_jogada(pecas, limite)
        print("Validação da retiração", retiradas)
        #o que resta?
        multiplicador = pecas//(limite+1)
        retiradas = pecas - ((limite+1)*multiplicador)
        pecas = pecas - retiradas
        if pecas == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam %d peças no tabuleiro." %(pecas))
        
        while pecas != 0:
            usuario_escolhe_jogada(pecas,limite)
            ###falta botar o que sobrou!!!!
            retiradas = pecas - ((limite+1)*multiplicador)
            pecas = pecas - retiradas
   
            if pecas != 0:
                computador_escolhe_jogada(pecas, limite)
                multiplicador = pecas//(limite+1)
                if pecas == 0:
                    print("Fim de jogo! O omputador ganhou!")
            else:
                print("Você fez o impossível e ganhou!")
        
        
    
        

def computador_escolhe_jogada(pecas, limite):
    # pecas - retiradas = (limite + 1) * multiplicador
    #  retiradas = -[(limite + 1)*multiplicador] + pecas
    multiplicador = pecas//(limite + 1)
    retiradas = pecas - ((limite + 1)*multiplicador)
    
    if retiradas == 1:
        print("O computador tirou 1 peça.")
    else:
        print("O computador tirou %d peças." %(retiradas))
    print('')
    
        
def usuario_escolhe_jogada(pecas, limite):
    retiradas = 0
    while retiradas < 1 or retiradas > limite:
        retiradas = int(input('Quantas peças?'))
        if retiradas < 1 or retiradas > limite:
            print("Oops! Jogada inválida! Tente de novo.")
        
    if retiradas == 1:
        print("Você tirou uma peça.")
        
    else:
        print("Você tirou %d peças." %(retiradas))
    print('')
    



def main():
    partida()
            
if __name__ == '__main__':
    main()
    



