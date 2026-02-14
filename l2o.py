import pygame
import random

# init
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Particle Animation")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 40, bold=True)

# ---------------- PARTICLE CLASS ----------------
class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = HEIGHT + 20
        self.speed = random.uniform(1, 3)
        self.size = random.randint(2, 6)
        self.color = (255, random.randint(80,160), random.randint(120,200))

    def move(self):
        self.y -= self.speed

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            self.color,
            (int(self.x), int(self.y)),
            self.size
        )

# ---------------- MAIN LOOP ----------------
particles = []
running = True

while running:
    screen.fill((0, 0, 0))

    # limit particle count
    if len(particles) < 300:
        for _ in range(6):
            particles.append(Particle())

    # update & draw
    for p in particles[:]:
        p.move()
        p.draw(screen)
        if p.y < -10:
            particles.remove(p)

    # blinking text
    if (pygame.time.get_ticks() // 500) % 2 == 0:
        text = font.render("love you 19on1l", True, (255, 255, 255))
        rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, rect)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()