import pygame
import random

pygame.init()

dis_width = 600
dis_height = 400
snake_block = 10
snake_speed = 15

dis = pygame.display.set_mode((dis_width, dis_height))  # screen size
pygame.display.set_caption("Snake Game")
pygame.display.update()

color_mid_grey = (182, 187, 205)  # score
color_light_grey = (243, 243, 243)  # for restart screen
color_earth = (248, 223, 212)  # for backgorund
color_teal = (99, 126, 118)  # menu font
color_brown = (198, 151, 116)  # food
color_blue = (7, 103, 173)  # head of the snake
color_geal = (41, 173, 178)  # body of snake

dis.fill(color_earth)  # display color
game_over = False

# positions for the snake head
x = 300
y = 200
x_change = 0
y_change = 0
clock = pygame.time.Clock()
game_close = False
font_style = pygame.font.SysFont("freesans", 25)
score_font = pygame.font.SysFont("freesans", 30)

def our_snake(snake_block, snake_list):
    pygame.draw.rect(dis, color_geal, [int(
        snake_list[-1][0]), int(snake_list[-1][1]), snake_block, snake_block])
    pygame.draw.rect(dis, color_blue, [int(
        snake_list[-1][0]), int(snake_list[-1][1]), snake_block-2, snake_block-2])
    for x in snake_list[0:-1]:
        pygame.draw.rect(
            dis, color_geal, [int(x[0]), int(x[1]), snake_block, snake_block])
        pygame.draw.rect(dis, color_geal, [int(x[0]), int(
            x[1]), snake_block-2, snake_block-2])


def the_score(score):  # function to display score
    # create surface with text
    value = score_font.render(
        "Your Score: " + str(score), True, color_mid_grey)
    dis.blit(value, [0, 0])  # draw surface onto display


def message(msg, score, color):
    mesg = font_style.render(msg, True, color)
    scr = font_style.render(score, True, color)
    dis.blit(mesg, [int(dis_width / 6), int(dis_height / 3)])
    dis.blit(scr, [0, 0])

def game_loop():
    game_over = False
    game_close = False
    x = int(dis_width / 2)
    y = int(dis_height / 2)
    x_change = 0
    y_change = 0
    
    # snake list (tail)
    snake_list = []
    len_of_snake = 1
    
    # food places to display
    # screen size = 600 * 400 so x is (600 - 10) / 10
    # and for y (400 - 10) / 10
    food_x = snake_block * \
        random.randint(0, ((dis_width - snake_block) / snake_block))
    food_y = snake_block * \
        random.randint(0, ((dis_height - snake_block) / snake_block))

    while (game_over == False):  # to keep the game screen
        # game loop
        while (game_close == True):
            dis.fill(color_light_grey)
            
            # lost_img = font_style.render(
            #     "You Loser! Q for Quit, P for Play again",  True, color_teal)
            message("You Loser! 'Q' for Quit, 'P' for Play again",
                    ("Your score was: " + str((len_of_snake - 1))), color_teal)
            # dis.blit(lost_img, [100, 100])

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # to check if the close button is clicked
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # if q clicked
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:  # if q clicked
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # to check if the close button is clicked
                game_over = True
            # check the pressed buttons
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0

        # check if the head is out of the display
        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            game_close = True

        # update the position
        x = x + x_change
        y = y + y_change

        dis.fill(color_earth)  # display color

        # draw the food
        pygame.draw.rect(dis, color_brown,
                         (food_x, food_y, snake_block, snake_block))

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > len_of_snake:
            del snake_list[0]

        # check if snake bites its own tail
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        # snake function
        our_snake(snake_block, snake_list)  # size of rectangle, list

        if x == food_x and y == food_y:
            len_of_snake += 1
            food_x = snake_block * random.randint(0, (dis_width / snake_block - 1))
            food_y = snake_block * \
                random.randint(0, (dis_height / snake_block - 1))

        the_score(len_of_snake - 1)
        pygame.display.update()
        clock.tick(snake_speed)  # frame rate

    pygame.quit()


game_loop()
