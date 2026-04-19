import pygame
import random

pygame.init()

W, H = 540, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Love Me Valentine")

font_big = pygame.font.SysFont("arial", 40, bold=True)
font_btn = pygame.font.SysFont("arial", 26, bold=True)

yes_btn = pygame.Rect(150, 520, 100, 50)
no_btn  = pygame.Rect(300, 520, 100, 50)

message = ""
run = True

while run:
    screen.fill((20, 30, 40))

    # title
    title1 = font_big.render("Love Me Valentine", True, (120,255,120))
    screen.blit(title1, (80, 60))

    q = font_big.render("Do you love me?", True, (255,255,255))
    screen.blit(q, (110, 300))

    mx, my = pygame.mouse.get_pos()

    # NO button runs away 😄
    if no_btn.collidepoint(mx, my):
        no_btn.x = random.randint(50, W-150)
        no_btn.y = random.randint(450, 700)

    # draw buttons
    pygame.draw.rect(screen, (255,100,150), yes_btn, border_radius=25)
    pygame.draw.rect(screen, (255,150,180), no_btn, border_radius=25)

    screen.blit(font_btn.render("YES", True, (255,255,255)), (yes_btn.x+25, yes_btn.y+10))
    screen.blit(font_btn.render("NO", True, (255,255,255)), (no_btn.x+30, no_btn.y+10))

    # result message
    if message:
        m = font_big.render(message, True, (255,200,220))
        screen.blit(m, (120, 650))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if yes_btn.collidepoint(e.pos):
                message = "I Love You Too ❤️"

    pygame.display.update()

pygame.se.quit()