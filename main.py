import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0 , 255, 0)
blue = (0, 0, 255)

yellow = (255, 255, 0)

game_over = False

pygame.init()
dis = pygame.display.set_mode((400,300))
dis.fill(blue)
pygame.draw.rect(dis, yellow, [10, 100, 30, 30])

pygame.display.update()

delay = 10000000
count = 0
while game_over is False:
    count += 1
    if count > delay:
        game_over = True
pygame.quit()
quit()