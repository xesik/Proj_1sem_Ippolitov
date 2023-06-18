# -*- coding: utf-8 -*-
import pygame
from random import randrange, choice


def helpt(some_text):
    global ball_speed_x, ball_speed_y, player_speed, start_vector, platform_list, platform_colors
    screen.blit(some_text, (WIDTH - 1130, HEIGHT / 2))
    ball_speed_x, ball_speed_y, player_speed = 0, 0, 0
    if pygame.key.get_pressed()[pygame.K_r]:
        platform_list = [pygame.Rect(10 + 119 * i, 70 + 70 * j, 110, 50) for i in range(10) for j in range(3)]
        platform_colors = [(randrange(30, 240), randrange(30, 240), randrange(30, 240)) for i in range(10) for j in
                           range(3)]
        ball.x, ball.y = WIDTH / 2 - 15, HEIGHT - HEIGHT / 4
        player.x, player.y = WIDTH / 2 - 90, HEIGHT - 36
        ball_speed_x, ball_speed_y = 6, 6
        player_speed = 8
        start_vector -= 1
        switch_scene(scene1())


def balls():
    global ball_speed_x, ball_speed_y, player_speed, start_vector

    if start_vector == 0:
        ball_speed_y *= -0.9
        ball_speed_x *= choice(imba_vector)
        start_vector += 1

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    platform_hit_index = ball.collidelist(platform_list)

    if platform_hit_index != -1:
        hit_platform = platform_list.pop(platform_hit_index)
        platform_colors.pop(platform_hit_index)
        collision_thing(ball, hit_platform)
        if len(platform_list) % 2 == 0:
            ball_speed_x += 0.15
            ball_speed_y += 0.15
            player_speed += 0.15
    if ball.colliderect(player):
        collision_thing(ball, player)
    # lose
    if ball.bottom >= player.centery + 9:
        helpt(lose_text)
    # win
    if len(platform_list) == 0:
        helpt(win_text)


def player_movement():
    if pygame.key.get_pressed()[pygame.K_LEFT] and player.left >= 0:
        player.left -= player_speed
    if pygame.key.get_pressed()[pygame.K_RIGHT] and player.right <= WIDTH:
        player.right += player_speed


def collision_thing(ball1, platform):
    global ball_speed_x, ball_speed_y
    if ball_speed_x > 0:
        dx = ball1.right - platform.left
    else:
        dx = platform.right - ball1.left
    if ball_speed_y > 0:
        dy = ball1.bottom - platform.top
    else:
        dy = platform.bottom - ball1.top

    if dx == dy:
        ball_speed_x, ball_speed_y = -ball_speed_x, -ball_speed_y
    elif dx > dy:
        ball_speed_y = -ball_speed_y
    elif dy > dx:
        ball_speed_x = -ball_speed_x


WIDTH, HEIGHT = 1200, 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")
clock = pygame.time.Clock()

ball = pygame.Rect(WIDTH / 2 - 15, HEIGHT - HEIGHT / 4, 24, 24)
player = pygame.Rect(WIDTH / 2 - 90, HEIGHT - 36, 180, 18)
platform_list = [pygame.Rect(10 + 119 * i, 70 + 70 * j, 110, 50) for i in range(10) for j in range(3)]
platform_colors = [(randrange(30, 222), randrange(30, 222), randrange(30, 222)) for i in range(10) for j in range(3)]
ball_speed_x = 6
ball_speed_y = 6
player_speed = 8
start_vector = 0
imba_vector = [-0.6, -0.4, -0.3, 0.3, 0.4, 0.6]
font = pygame.font.SysFont('Arialblack', 38)
text1 = font.render("Нажмите пробел чтобы начать игру", False, "#DEB887")
lose_text = font.render("Вы проиграли. Нажмите R, чтобы начать сначала", False, "#DEB887")
win_text = font.render("Вы победили! Нажмите R, чтобы начать сначала", False, "#DEB887")


def switch_scene(scene):
    scene()


def scene2():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit()
        screen.fill('#FFEFD5')
        pygame.draw.rect(screen, '#808080', player)
        pygame.draw.ellipse(screen, '#696969', ball)
        [pygame.draw.rect(screen, platform_colors[color], platform) for color, platform in enumerate(platform_list)]

        balls()
        player_movement()

        pygame.display.flip()
        clock.tick(60)


def scene1():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif pygame.key.get_pressed()[pygame.K_SPACE]:
                switch_scene(scene2())
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit()
        screen.fill('#FFEFD5')
        screen.blit(text1, (WIDTH / 5, HEIGHT / 2))
        pygame.draw.rect(screen, '#808080', player)
        pygame.draw.ellipse(screen, '#696969', ball)
        [pygame.draw.rect(screen, platform_colors[color], platform) for color, platform in enumerate(platform_list)]
        pygame.display.flip()
        clock.tick(60)


switch_scene(scene1())
