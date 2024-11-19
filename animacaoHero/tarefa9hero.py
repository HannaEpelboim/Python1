#animacaoHeroComTempo
import pygame
width = 800 
height = 600 
hero_walk = [] 
hero_anim_frame = 1
hero_pos_x = 100
hero_pos_y = 225
hero_anim_time = 0 # variavel para controle do tempo da animação

def load():
    global clock, hero_walk
    clock = pygame.time.Clock() 
    for i in range(1, 17):
        hero_walk.append(pygame.image.load("Hero_Walk_" + str('%02d'%(i)) + ".png"))
        
def update(dt):
    global hero_walk, hero_anim_frame, hero_pos_x, hero_anim_time,hero_pos_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        hero_pos_x = hero_pos_x + (0.1 * dt) 
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_anim_frame = hero_anim_frame + 1 # avança para proximo frame
            if hero_anim_frame > 3: # loop da animação
                hero_anim_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo
    if keys[pygame.K_LEFT]:
        if hero_anim_frame > 7 or hero_anim_frame < 4:
            hero_anim_frame = 4
        hero_pos_x = hero_pos_x - (0.1 * dt) 
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_anim_frame = hero_anim_frame + 1 # avança para proximo frame
            if hero_anim_frame > 7: # loop da animação
                hero_anim_frame = 4
            hero_anim_time = 0 #reinicializa a contagem do tempo
    if keys[pygame.K_UP]:
        if hero_anim_frame > 11 or hero_anim_frame < 8:
            hero_anim_frame = 8
        hero_pos_y = hero_pos_y - (0.1 * dt) 
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_anim_frame = hero_anim_frame + 1 # avança para proximo frame
            if hero_anim_frame > 11: # loop da animação
                hero_anim_frame = 8
            hero_anim_time = 0 #reinicializa a contagem do tempo
    if keys[pygame.K_DOWN]:
        if hero_anim_frame > 15 or hero_anim_frame < 12:
            hero_anim_frame = 12
        hero_pos_y = hero_pos_y + (0.1 * dt) 
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_anim_frame = hero_anim_frame + 1 # avança para proximo frame
            if hero_anim_frame > 15: # loop da animação
                hero_anim_frame = 12
            hero_anim_time = 0 #reinicializa a contagem do tempo                
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

