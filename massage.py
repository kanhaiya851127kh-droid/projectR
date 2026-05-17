import pygame
import sys

# Pygame start
pygame.init()

# Screen size
screen = pygame.display.set_mode((700, 300))
pygame.display.set_caption("Love Message")

# Colors
BLACK = (0, 0, 0)
PINK = (255, 105, 180)

# Font
font = pygame.font.SysFont("Arial", 40)

# Message
text = font.render("Py, tum meri smile ka reason ho ❤️", True, PINK)

# Main loop
while True:
    screen.fill(BLACK)

    # Text position
    screen.blit(text, (40, 120))

    pygame.display.update()

    # Exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()