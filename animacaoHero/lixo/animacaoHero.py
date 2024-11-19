#animacaoHeroi
import pygame
width = 800 #Largura Janela
height = 600 #Altura Janela
hero_walk = [] # vetor de imagens
hero_anim_frame = 1
hero_pos_x = 100
hero_pos_y = 225

def load():
    global clock, hero_walk
    clock = pygame.time.Clock() 
    for i in range(1, 5): #carrega as imagens da animação
        hero_walk.append(pygame.image.load("Hero_Walk_0" + str(i) + ".png"))
        
def update(dt):
    global hero_walk, hero_anim_frame, hero_pos_x
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        hero_pos_x = hero_pos_x + (0.1 * dt) # movimenta o personagem
        hero_anim_frame = hero_anim_frame + 1 # incrementa a animação
        if hero_anim_frame > 3: # loop da animação
            hero_anim_frame = 0
            
def draw_screen(screen): #desenha o personagem usando o indice da animação
    screen.fill((255,255,255))
    screen.blit(hero_walk[hero_anim_frame], (hero_pos_x, hero_pos_y))

def main_loop(screen): 
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break
        clock.tick(60)
        dt = clock.get_time() 
        draw_screen(screen) 
        update(dt)
        pygame.display.update()
        
pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()
