import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart Animation")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
PINK = (255, 80, 120)

def heart_points(scale=10):
    points = []
    for t in range(0, 360):
        t = math.radians(t)
        x = 16 * math.sin(t) ** 3
        y = (13 * math.cos(t)
             - 5 * math.cos(2*t)
             - 2 * math.cos(3*t)
             - math.cos(4*t))
        points.append((x * scale, -y * scale))
    return points

points = heart_points(12)

running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    rotated = []
    for x, y in points:
        xr = x * math.cos(angle) - y * math.sin(angle)
        yr = x * math.sin(angle) + y * math.cos(angle)
        rotated.append((xr + WIDTH//2, yr + HEIGHT//2))

    pygame.draw.polygon(screen, PINK, rotated)

    angle += 0.02
    pygame.display.flip()
    clock.tick(60)

pygame.quit()