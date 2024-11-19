import pygame
global width,height
global score
score = ['a','b','c']
width = 432 
height = 1008

##############################################################################
def carrega_ranking():
    WHITE = [252, 157, 251]
    Rank = open("ranking.txt","w")
    i = 0
    while i < len(score) and i < 5:
        print('o')
        Rank.write("%dº -- %s\n" %(i+1,score[i]))
        i+= 1
    Rank.close
def ranking():
    carrega_ranking()
    Rank = open("ranking.txt","r")
    WHITE = [252, 157, 251]
    BLACK = [0,0,0]
    PINK = [250, 22, 54]
    s = "\n"
    i = 0
    while i < 3:
        s += Rank.readline()
        i +=1
    def load():
        global sys_font,Sys_font
        sys_font = pygame.font.Font(pygame.font.get_default_font(), 40)
        Sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)

    def check_click(x1,y1,w1,h1,x2,y2):
         return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1    
    def draw_screen(screen):
        screen.fill(WHITE)
        pygame.draw.rect(screen, (250, 22, 54), (345, 720, 100, 100))
        t = Sys_font.render("VOLTAR", False, WHITE)
        screen.blit(t, (360,740))

        
        t = sys_font.render(s, False, BLACK)
        screen.blit(t, (20,360))
        Rank.close
        
    def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
        global result
        if mouse_buttons[0]:
            if check_click(345, 720, 100, 100, px_mouse, py_mouse):
                main()
                 
    def main_loop(screen):
        running = True
        while running:
            for e in pygame.event.get(): 
                if e.type == pygame.QUIT:
                    running = False
                    break
                elif e.type == pygame.MOUSEBUTTONDOWN: #detecta o inicio do clique do mouse
                        mouse_buttons = pygame.mouse.get_pressed()
                        px_mouse, py_mouse = pygame.mouse.get_pos()
                        mouse_click_down(px_mouse, py_mouse, mouse_buttons)
            # Desenha objetos na tela 
            draw_screen(screen)
            # Pygame atualiza o seu estado
            pygame.display.update() 


    pygame.init()
    screen = pygame.display.set_mode((width, height))
    load()
    main_loop(screen)
    pygame.quit()

##############################################################################



    
##############################################################################
def jogo():
    global hero_walk,hero_anim_frame,hero_pos_x,hero_pos_y,hero_anim_time
    hero_walk = [] 
    hero_anim_frame = 1
    hero_pos_x = 170
    hero_pos_y = 720
    hero_anim_time = 0 # variavel para controle do tempo da animação

    def load():
        global clock, hero_walk
        clock = pygame.time.Clock() 
        for i in range(1, 17):
            hero_walk.append(pygame.image.load("Hero_Walk_" + str('%02d'%(i)) + ".png"))
    def update(dt):
        global hero_walk, hero_anim_frame, hero_pos_x, hero_anim_time,hero_pos_y
        keys = pygame.key.get_pressed()

        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_anim_frame = hero_anim_frame + 1 # avança para proximo frame
            if hero_anim_frame > 3: # loop da animação
                hero_anim_frame = -1
            hero_anim_time = 0 #reinicializa a contagem do tempo



        if keys[pygame.K_RIGHT]:
            hero_pos_x = 324       

        if keys[pygame.K_UP]:
            hero_pos_x = 172

        if keys[pygame.K_LEFT]:
            hero_pos_x = 26      
        
    def draw_screen(screen):
        screen.fill((255,255,255))
        #desenha o personagem usando o indice da animação
        screen.blit(hero_walk[hero_anim_frame], (hero_pos_x, hero_pos_y))


    def main_loop(screen):  
        global clock
        running = True
        while running:
            for e in pygame.event.get(): 
                if e.type == pygame.QUIT:
                    running = False
                    break

            # Define FPS máximo
            clock.tick(60)        
            # Calcula tempo transcorrido desde a última atualização 
            dt = clock.get_time()
            # Desenha objetos na tela 
            draw_screen(screen)
            # Atualiza posição dos objetos da tela
            update(dt)
            # Pygame atualiza o seu estado
            pygame.display.update() 

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Exemplo de Audio")
    load()
    main_loop(screen)
    pygame.quit()
##############################################################################
def regras():
    WHITE = [252, 157, 251]
    BLACK = [0,0,0]
    PINK = [250, 22, 54]
    def load():
        global sys_font
        sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    def check_click(x1,y1,w1,h1,x2,y2):
         return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1    
    def draw_screen(screen):
        screen.fill(WHITE)
        pygame.draw.rect(screen, (250, 22, 54), (345, 720, 100, 100))
        t = sys_font.render("VOLTAR", False, WHITE)
        screen.blit(t, (360,740))
        t = sys_font.render("BLABLABLABLA", False, BLACK)
        screen.blit(t, (150,360))
        
    def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
        global result
        if mouse_buttons[0]:
            if check_click(345, 720, 100, 100, px_mouse, py_mouse):
                main()
                 
    def main_loop(screen):
        running = True
        while running:
            for e in pygame.event.get(): 
                if e.type == pygame.QUIT:
                    running = False
                    break
                elif e.type == pygame.MOUSEBUTTONDOWN: #detecta o inicio do clique do mouse
                        mouse_buttons = pygame.mouse.get_pressed()
                        px_mouse, py_mouse = pygame.mouse.get_pos()
                        mouse_click_down(px_mouse, py_mouse, mouse_buttons)
            # Desenha objetos na tela 
            draw_screen(screen)
            # Pygame atualiza o seu estado
            pygame.display.update() 


    pygame.init()
    screen = pygame.display.set_mode((width, height))
    load()
    main_loop(screen)
    pygame.quit()

##############################################################################

def main():
    WHITE = [252, 157, 251]
    PINK = [250, 22, 54]
    def load():
        global sys_font,Sys_font
        sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
        Sys_font = pygame.font.Font(pygame.font.get_default_font(), 50)

    def check_click(x1,y1,w1,h1,x2,y2):
         return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1
        
    def draw_screen(screen):
        screen.fill(WHITE)

        pygame.draw.rect(screen, (250, 22, 54), (130, 360, 200, 100))
        t = sys_font.render("JOGAR!!!", False, WHITE)
        screen.blit(t, (190,400))
        pygame.draw.rect(screen, (250, 22, 54), (130, 490, 200, 100))
        t = sys_font.render("REGRAS", False, WHITE)
        screen.blit(t, (180,530))
        pygame.draw.rect(screen, (250, 22, 54), (130, 620, 200, 100))
        t = sys_font.render("RANKING", False, WHITE)
        screen.blit(t, (180,660))

        
        t = Sys_font.render("NOME", False, PINK)
        screen.blit(t, (150,200))


    def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
        global result
        if mouse_buttons[0]:
            if check_click(130, 360, 200, 100, px_mouse, py_mouse):
                jogo()
            if check_click(130, 490, 200, 100, px_mouse, py_mouse):
                regras()
            if check_click(130, 620, 200, 100, px_mouse, py_mouse):
                ranking()  
                   
    def main_loop(screen):
        running = True
        while running:
            for e in pygame.event.get(): 
                if e.type == pygame.QUIT:
                    running = False
                    break
                elif e.type == pygame.MOUSEBUTTONDOWN: #detecta o inicio do clique do mouse
                        mouse_buttons = pygame.mouse.get_pressed()
                        px_mouse, py_mouse = pygame.mouse.get_pos()
                        mouse_click_down(px_mouse, py_mouse, mouse_buttons)
                        
            # Desenha objetos na tela 
            draw_screen(screen)
            # Pygame atualiza o seu estado
            pygame.display.update() 


    pygame.init()
    screen = pygame.display.set_mode((width, height))
    load()
    main_loop(screen)
    pygame.quit()
##################################################################################################
main()



