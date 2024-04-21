import pygame
import sys

# Inicializar o pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configurar a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Animação de um Boneco Dançando")

# Posição inicial do boneco
boneco_x, boneco_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
boneco_width, boneco_height = 50, 100

# Loop principal
clock = pygame.time.Clock()
frame = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a posição do boneco (apenas para fins de demonstração)
    boneco_x += 5
    boneco_y += 2

    # Preencher a tela com a cor de fundo
    screen.fill(WHITE)

    # Exibir o boneco na tela (retângulo vermelho como exemplo)
    pygame.draw.rect(screen, RED, (boneco_x, boneco_y, boneco_width, boneco_height))

    # Atualizar a tela
    pygame.display.flip()

    # Avançar para o próximo frame
    frame += 1

    # Limitar a taxa de quadros
    clock.tick(FPS)

# Encerrar o pygame
pygame.quit()
sys.exit()
