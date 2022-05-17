import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = (1024, 720)
FPS = 30
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()

def render_multi_line(text, x, y, fsize):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            font = pygame.font.SysFont('Arial', fsize)
            screen.blit(font.render(l, 0, 0), (x, y + fsize*i))
            
text = "Eres Santiago Nasar, te acabas de levantar\ny te estas preparando para la llegada del obispo."

while True:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill(pygame.Color('white'))
    render_multi_line(text, 10, 10, 15)
    pygame.display.update()