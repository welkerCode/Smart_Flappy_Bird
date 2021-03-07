import pygame

game_width = 200
game_height = 300\

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0 , 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
brown = (150, 75, 0)

# Define the boundaries
bird_lowest_pos = 250

game_over = False

# Define the sprites
flappy_bird_im = pygame.image.load(r'images\flappy_bird.png')
pipe_downward_im = pygame.image.load(r'images\pipe_downward.png')
pipe_upward_im = pygame.image.load(r'images\pipe_upward.png')
grass = pygame.Rect(0, 275, 200, 25)
dirt = pygame.Rect(0, 280, 200, 20)

# Define the initial position of the pird and pipes
bird_pos_x = 0
bird_pos_y = 0

# Initialize the game
pygame.init()


# Run the loop
delay = 10000000
count = 0
while game_over is False:
    count += 1
    if count > delay:
        game_over = True
    if count % 100000:
        bird_pos_y = bird_pos_y + 1
        if bird_pos_y > bird_lowest_pos:
            bird_pos_y = 0

    # Define a frame
    dis = pygame.display.set_mode((game_width, game_height))

    # Draw the frame
    dis.fill(blue)                                              # Fill in the background
    dis.blit(flappy_bird_im, (bird_pos_x, bird_pos_y))          # Add the flappy bird
    dis.blit(pipe_downward_im, (50, -200))                      # Add the downward pipe
    dis.blit(pipe_upward_im, (100, 0))                          # Add the upward pipe
    pygame.draw.rect(dis, green, grass)                         # Add the grass
    pygame.draw.rect(dis, brown, dirt)                          # Add the dirt under the grass

    # Update the frame
    pygame.display.update()

pygame.quit()
quit()