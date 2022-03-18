from numpy import append
import pygame
import time
import random


# Create a (300,400) window
pygame.init()

# Snake and Board(Black & White)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0) # Message 
blue = (50, 153, 213) # Food for the snake
yellow = (255, 255, 102)
green = (0, 255, 0)

# H and W of the window
display_h = 600
display_w = 400

display = pygame.display.set_mode((display_h, display_w))
pygame.display.set_caption('Snake by KK')

clock = pygame.time.Clock()

# Snake Stats
snake_speed = 15
snake_block = 10

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_style = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    val = score_style.render(f"Your Score :{score}", True, yellow)
    display.blit(val, [0, 0])


def our_snake(snake_block, snake_list):# draw the snake in the game window
    for x in snake_list:
        pygame.draw.rect(display ,black ,[x[0], x[1], snake_block, snake_block])

def message(msg, color): # Create msg inside the game
    msg = font_style.render(msg, True, color)
    display.blit(msg, [display_w / 6 , display_h / 3])

def gameLoop(): # creating a func for the game loop
    game_over = False
    game_close = False

    # Original (x,y)
    x1 = display_w / 2
    y1 = display_h / 2

    # Updated (x,y)
    x1_up = 0
    y1_up = 0

    # Keep Moves and Len of the snake
    snake_list = []
    len_snake = 1
    
    # Randomize the food for the snake
    foodx = round(random.randrange(0, display_w - snake_block) / 10.0) *10.0
    foody = round(random.randrange(0, display_w - snake_block) / 10.0) *10.0


    # Game General Loop
    while not game_over:

        while game_close == True :
            display.fill(blue)
            message("You Lost ! Press Q - quit or C - Play Again", red)
            your_score(len_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                # Restart or Quit the Game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        # Run the game loop all over again
                        gameLoop()
        
        for event in pygame.event.get():
        # Movement of the Snake
            if event.type == pygame.QUIT:
                    game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                  x1_up = -snake_block
                  y1_up = 0
                elif event.key == pygame.K_RIGHT:
                    x1_up = snake_block
                    y1_up = 0
                elif event.key == pygame.K_DOWN:
                    x1_up = 0
                    y1_up = snake_block
                elif event.key == pygame.K_UP:
                    x1_up = 0
                    y1_up = -snake_block

        # Check if we are out of the Limits
        if x1 >= display_w or x1 < 0 or y1 >= display_h or y1 < 0:
            game_over = True
    

        # Update the (x,y)
        x1 += x1_up
        y1 += y1_up
        display.fill(blue)
        pygame.draw.rect(display , green, [foodx, foody, snake_block, snake_block])

        # Append the movements of the snake into a list
        # Check if the head of the snake is equal to the tail of the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Check if the length of the snake is longer than the length of the snake_list
        if len(snake_list) > len_snake :
            del snake_list[0]
        
        # Checking to see if we made it to the tail of the snake
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        # Display our scnake
        our_snake(snake_block, snake_list)
        your_score(len_snake - 1)

        pygame.display.update()

        # Check if the snake ate food the make him grow by 1
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_w - snake_block) / 10.0) *10.0
            foody = round(random.randrange(0, display_w - snake_block) / 10.0) *10.0
            len_snake += 1
            

        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameLoop()





