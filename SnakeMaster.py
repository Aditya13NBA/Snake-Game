import pygame
import random
import os

pygame.mixer.init()

pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("SnakeMaster")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
font2 = pygame.font.SysFont(None, 20)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def text_screen2(text, color, x, y):
    screen_text = font2.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((255,140,0))
        text_screen("Welcome to SnakeMasters", black, 200, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('./res/back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


def gameloop():
    exit_game = False
    game_over = False
    snake_x = random.randint(0, screen_width)
    snake_y = random.randint(0, screen_height)
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    if(not os.path.exists("res\hiscore.txt")):
        with open("res\hiscore.txt", "w") as f:
            f.write("0")

    with open("res\hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    food_size = 20
    score = 0
    init_velocity = 7
    dist = 20
    snake_size = 30
    fps = 30
    while not exit_game:
        if game_over:
            with open("res\hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_f:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_s:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_e:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_d:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

                    if event.key == pygame.K_a:
                        dist +=5

                    if event.key == pygame.K_z:
                        score +=100

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<dist and abs(snake_y - food_y)<dist:
                score +=1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(red)
            text_screen2("Score: " + str(score) + "  Hiscore: "+str(hiscore), black, 5, 5)
            pygame.draw.rect(gameWindow, green, [food_x, food_y, food_size, food_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('res\got.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('res\gameover.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, blue, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
