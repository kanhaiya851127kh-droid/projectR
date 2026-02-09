import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart + Text")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 40, bold=True)

BLACK = (0, 0, 0)
PINK = (255, 80, 140)
WHITE = (255, 255, 255)

center_x, center_y = WIDTH // 2, HEIGHT // 2

text_surface = font.render("lost my love", True, WHITE)
text_rect = text_surface.get_rect(center=(center_x, center_y))

t = 0
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # beating scale
    scale = 15 + 2 * math.sin(math.radians(t * 4))

    points = []
    for i in range(360):
        angle = math.radians(i)

        x = 16 * math.sin(angle) ** 3
        y = (13 * math.cos(angle)
             - 5 * math.cos(2 * angle)
             - 2 * math.cos(3 * angle)
             - math.cos(4 * angle))

        px = int(center_x + x * scale)
        py = int(center_y - y * scale)
        points.append((px, py))

    pygame.draw.polygon(screen, PINK, points)

    # draw text on top
    screen.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(30)
    t += 1

pygame.quit()
