import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Love You Heart")

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 18, bold=True)
name_font = pygame.font.SysFont("arial", 80, bold=True)  

BLACK = (0, 0, 0)
PINK = (234, 128, 176)
WHITE = (255, 255, 255)

center_x, center_y = WIDTH // 2, HEIGHT // 2

your_name = " s "   

running = True
t = 0

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------- NAME IN BACKGROUND ----------
    name_text = name_font.render(your_name, True, WHITE)
    name_rect = name_text.get_rect(center=(center_x, center_y))
    screen.blit(name_text, name_rect)

    # ---------- HEART TEXT CURVE ----------
    for i in range(0, 360, 6):
        angle = math.radians(i + t)

        x = 16 * math.sin(angle) ** 3
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        )

        px = center_x + x * 15
        py = center_y - y * 15

        text = font.render("love you", True, PINK)
        screen.blit(text, (px, py))

    t += 1
    pygame.display.update()
    clock.tick(20)

pygame.quit()
