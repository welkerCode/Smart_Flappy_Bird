import pygame

game_width = 200
game_height = 300
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0 , 255, 0)
blue = (0, 0, 255)

yellow = (255, 255, 0)

game_over = False
flappy_bird_im = pygame.image.load(r'C:\Users\taylo\source\repos\Smart_Flappy_Bird\images\flappy_bird.png')
pipe_downward_im = pygame.image.load(r'C:\Users\taylo\source\repos\Smart_Flappy_Bird\images\pipe_downward.png')
pygame.init()
dis = pygame.display.set_mode((game_width, game_height))
dis.fill(blue)
dis.blit(flappy_bird_im, (0, 0))
dis.blit(pipe_downward_im, (50, -200))

pygame.display.update()

delay = 10000000
count = 0
while game_over is False:
    count += 1
    if count > delay:
        game_over = True
pygame.quit()
quit()