import pygame
from pygame.locals import *

pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Inicialização da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movendo a Imagem")
clock = pygame.time.Clock()

# Carrega a imagem do cubo
cube_img = pygame.image.load("testando.png")  # Substitua "cubo.png" pelo caminho da sua imagem

# Obtém o retângulo que representa a imagem
cube_rect = cube_img.get_rect()

# Dimensões desejadas para a imagem do cubo
cube_width = 100
cube_height = 100

# Redimensiona a imagem do cubo para as dimensões desejadas
cube_img = pygame.transform.scale(cube_img, (cube_width, cube_height))

# Posição inicial da imagem
cube_x = SCREEN_WIDTH // 2
cube_y = SCREEN_HEIGHT // 2

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Captura das teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and cube_x > 0:
        cube_x -= 5
    if keys[K_RIGHT] and cube_x < SCREEN_WIDTH - cube_rect.width:
        cube_x += 5
    if keys[K_UP] and cube_y > 0:
        cube_y -= 5
    if keys[K_DOWN] and cube_y < SCREEN_HEIGHT - cube_rect.height:
        cube_y += 5

    # Limpeza da tela
    screen.fill((255, 255, 255))

    # Desenho da imagem do cubo na posição atual
    screen.blit(cube_img, (cube_x, cube_y))

    # Atualização da tela
    pygame.display.update()

    # Limita a quantidade de quadros por segundo (FPS)
    clock.tick(FPS)

# Finaliza o Pygame
pygame.quit()
