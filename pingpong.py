import pygame
import sys
import random

pygame.init()

def game_status():
   global status_game
   if status_game == "STOP":
      for _ in range(0,1):
         clock.tick(2)
      status_game = "PLAY"

WIDTH,HEIDTH = 1000,600

text_color = (255,255,255)
score_player,score_enum = 0,0
main_player,main_enum = pygame.font.Font(None,40),pygame.font.Font(None,40)
txt_enum = main_enum.render(f"Счёт противника: {score_enum}",True,text_color)
txt_player = main_player.render(f"Твой счёт: {score_player}",True,text_color)
win_bg = (61,245,101)
win_bg_player_rect,win_bg_enum_rect = pygame.Rect(0,0,WIDTH/2-25,HEIDTH),pygame.Rect(WIDTH/2-25,0,WIDTH/2+25,HEIDTH)
status_game = "PLAY"

ball_move_y,ball_move_x = -20,-15
ball_color,ball_speed = (255,255,255),1
ball_size = 50
ball_x,ball_y = WIDTH/2 - ball_size,HEIDTH/2 - ball_size

last_move_player = "UP"
player_color,player_speed = (0,0,255),10
player_size_x,player_size_y = 25,HEIDTH/4
player_x,player_y = 5,HEIDTH/3
enum_color,enum_speed,enum_step,enum_move = (255,0,0),10,70,"UP"
enum_size_x,enum_size_y = 25,HEIDTH/4
enum_x,enum_y = WIDTH-enum_size_x-5,ball_y 

display = pygame.display.set_mode((WIDTH,HEIDTH))
pygame.display.set_caption("Пинг-понг")
clock = pygame.time.Clock()
isgame = True

while isgame:
    game_status()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isgame = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player_y -= player_speed
        last_move_player = "UP"
    elif keys[pygame.K_DOWN]:
        player_y += player_speed
        last_move_player = "DOWN"

    if enum_step >= 15:
       enum_step = 0

    if enum_move == "UP":
       enum_y -= enum_speed
    elif enum_move == "DOWN":
       enum_y += enum_speed

    enum_step += 1

    if enum_y < 0:
       enum_y = 0
       enum_move = "DOWN"
       enum_step = 35
    elif enum_y > HEIDTH - enum_size_y:
       enum_y = HEIDTH - enum_size_y
       enum_move = "UP"
       enum_step = 35

    if player_y < 0:
        player_y = 0
    elif player_y > HEIDTH - player_size_y:
        player_y = HEIDTH - player_size_y

    ball_rect = pygame.Rect(ball_x,ball_y,ball_size,ball_size)
    enum_rect = pygame.Rect(enum_x,enum_y,enum_size_x,enum_size_y)
    player_rect = pygame.Rect(player_x,player_y,player_size_x,player_size_y)

    if ball_rect.colliderect(player_rect):
     ball_move_x = abs(ball_move_x)
    elif ball_rect.colliderect(enum_rect):
     ball_move_x = -abs(ball_move_x)
    if ball_y < 0:
     ball_move_y = abs(random.randint(5,20))
    elif ball_y > HEIDTH - ball_size:
     ball_move_y = -abs(random.randint(5,20))

    ball_x += ball_move_x
    ball_y += ball_move_y

    ball_rect = pygame.Rect(ball_x,ball_y,ball_size,ball_size)

    if ball_rect.colliderect(player_rect):
        ball_move_x = abs(ball_move_x)
        if last_move_player == "UP":
           ball_move_y = abs(random.randint(5,20))
        else:
           ball_move_y = -abs(random.randint(5,20))
    elif ball_rect.colliderect(enum_rect):
        ball_move_x = -abs(ball_move_x)
        if enum_move == "UP":
           ball_move_y = abs(random.randint(5,20))
        else:
           ball_move_y = -abs(random.randint(5,20))

    display.fill((0,0,0))
    
    if ball_x < 0 - ball_size:
       score_enum += 1
       txt_enum = main_enum.render(f"Счёт противника: {score_enum}",True,text_color)
       ball_x,ball_y = WIDTH/2 - ball_size,HEIDTH/2 - ball_size
       ball_move_x,ball_move_y = 15,0
       pygame.draw.rect(display,win_bg,win_bg_enum_rect)
       player_x,player_y = 5,HEIDTH/3
       enum_x,enum_y = WIDTH-enum_size_x-5,ball_y 
       status_game = "STOP"
    elif ball_x > WIDTH:
       score_player += 1
       txt_player = main_player.render(f"Твой счёт: {score_player}",True,text_color)
       ball_x,ball_y = WIDTH/2 - ball_size,HEIDTH/2 - ball_size
       ball_move_x,ball_move_y = -15,0
       pygame.draw.rect(display,win_bg,win_bg_player_rect)
       player_x,player_y = 5,HEIDTH/3
       enum_x,enum_y = WIDTH-enum_size_x-5,ball_y 
       status_game = "STOP"

    pygame.draw.line(display,(30,30,30),(WIDTH/2-25,0),(WIDTH/2-25,HEIDTH),10)
    pygame.draw.ellipse(display,ball_color,ball_rect)
    pygame.draw.rect(display,enum_color,enum_rect)
    pygame.draw.rect(display,player_color,player_rect)
    display.blit(txt_player,(25,HEIDTH - 25))
    display.blit(txt_enum,(WIDTH - 300,HEIDTH - 25))
    clock.tick(35)
    pygame.display.update()
pygame.quit()
sys.exit()