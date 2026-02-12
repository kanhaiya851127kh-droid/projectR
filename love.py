import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gift → Heart")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 18, bold=True)

BLACK = (0, 0, 0)
PINK = (234, 128, 176)
RED = (200, 30, 30)
GOLD = (255, 215, 0)
WHITE = (255, 255, 255)

center_x, center_y = WIDTH // 2, HEIGHT // 2

# 🎁 Gift box
box = pygame.Rect(250, 300, 300, 200)
lid_offset = 0
opened = False
show_heart = False

t = 0
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if box.collidepoint(event.pos):
                opened = True

    # ---------- Gift Draw ----------
    if not show_heart:
        pygame.draw.rect(screen, RED, box)
        pygame.draw.rect(screen, GOLD, (box.x, box.y, box.width, 25))

        # ribbon cross
        pygame.draw.rect(screen, GOLD, (box.centerx-10, box.y, 20, box.height))
        pygame.draw.rect(screen, GOLD, (box.x, box.centery-10, box.width, 20))

        txt = pygame.font.SysFont("arial", 26).render(
            "Click Gift 🎁", True, WHITE)
        screen.blit(txt, (box.x+80, box.y+80))

    # lid open animation
    if opened and lid_offset < 180:
        lid_offset += 5
    if lid_offset >= 180:
        show_heart = True

    if not show_heart:
        pygame.draw.rect(screen, GOLD,
                         (box.x, box.y - lid_offset, box.width, 25))

    # ---------- Your Heart Animation ----------
    if show_heart:
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

            text = font.render("love", True, PINK)
            screen.blit(text, (px, py))

        t += 1

    pygame.display.update()
    clock.tick(30)

pygame.quit()