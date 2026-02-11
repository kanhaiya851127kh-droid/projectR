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

            text = font.render("love you", True, PINK)
            screen.blit(text, (px, py))

        t += 1

    pygame.display.update()
    clock.tick(30)

pygame.quit()

'''

import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLACK = (0,0,0)
PINK = (234,128,176)
RED = (200,30,30)
GOLD = (255,215,0)
WHITE = (255,255,255)

center_x, center_y = WIDTH//2, HEIGHT//2

# -------- Load Photo --------
photo = pygame.image.load("photo.png").convert_alpha()
photo = pygame.transform.scale(photo, (200,200))

# make circle mask
mask = pygame.Surface((200,200), pygame.SRCALPHA)
pygame.draw.circle(mask, (255,255,255), (100,100), 100)
photo.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

# -------- Gift --------
box = pygame.Rect(250, 300, 300, 200)
lid_offset = 0
opened = False
show_heart = False

font = pygame.font.SysFont("arial", 22, bold=True)

t = 0
running = True

while running:
    screen.fill(BLACK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if box.collidepoint(e.pos):
                opened = True

    # 🎁 gift draw
    if not show_heart:
        pygame.draw.rect(screen, RED, box)
        pygame.draw.rect(screen, GOLD, (box.x, box.y, box.width, 25))
        pygame.draw.rect(screen, GOLD, (box.centerx-10, box.y, 20, box.height))
        pygame.draw.rect(screen, GOLD, (box.x, box.centery-10, box.width, 20))
        txt = font.render("Click Gift 🎁", True, WHITE)
        screen.blit(txt, (box.x+80, box.y+80))

    if opened and lid_offset < 180:
        lid_offset += 5
    if lid_offset >= 180:
        show_heart = True

    if not show_heart:
        pygame.draw.rect(screen, GOLD,
                         (box.x, box.y-lid_offset, box.width, 25))

    # ❤️ heart + photo
    if show_heart:

        # photo center
        rect = photo.get_rect(center=(center_x, center_y))
        screen.blit(photo, rect)

        # heart text curve
        for i in range(0,360,6):
            ang = math.radians(i+t)
            x = 16*math.sin(ang)**3
            y = 13*math.cos(ang)-5*math.cos(2*ang)-2*math.cos(3*ang)-math.cos(4*ang)

            px = center_x + x*15
            py = center_y - y*15

            text = font.render("LOVE YOU", True, PINK)
            screen.blit(text, (px,py))

        t += 1

    pygame.display.update()
    clock.tick(30)

pygame.quit()
'''

