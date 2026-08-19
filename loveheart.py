import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gift Open Heart")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (220, 20, 60)
PINK = (255, 105, 180)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("arial", 40, bold=True)

name_text = "19on1l"   #  under of heart

# -------- Heart Function --------
def draw_heart(surface, cx, cy, size):
    points = []
    for t in range(0, 360):
        t = math.radians(t)
        x = 16 * math.sin(t)**3
        y = (13 * math.cos(t)
             - 5 * math.cos(2*t)
             - 2 * math.cos(3*t)
             - math.cos(4*t))
        points.append((cx + x * size, cy - y * size))
    pygame.draw.polygon(surface, PINK, points)


# -------- Gift Box --------
box_rect = pygame.Rect(300, 250, 200, 150)
lid_offset = 0
opened = False

running = True
show_heart = False
heart_size = 1

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect.collidepoint(event.pos):
                opened = True

    # Draw box
    pygame.draw.rect(screen, RED, box_rect)
    pygame.draw.rect(screen, GOLD, (box_rect.x, box_rect.y, box_rect.width, 20))

    # Lid animation
    if opened and lid_offset < 120:
        lid_offset += 3
    if lid_offset >= 120:
        show_heart = True

    pygame.draw.rect(screen, GOLD,
                     (box_rect.x, box_rect.y - lid_offset,
                      box_rect.width, 20))

    # Heart grow animation
    if show_heart:
        if heart_size < 12:
            heart_size += 0.2
        draw_heart(screen, WIDTH//2, 230, heart_size)

        text = font.render(name_text, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH//2, 230))
        screen.blit(text, text_rect)

    # Instruction text
    info = pygame.font.SysFont("arial", 22).render(
        "Gift box par click karo 🎁", True, BLACK)
    screen.blit(info, (290, 450))

    pygame.display.update()
    clock.tick(60)

pygame.quit()

