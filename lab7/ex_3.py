import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

ball_radius = 25
ball_color = (255, 0, 0)
ball_position = [screen_width // 2, screen_height // 2]

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and ball_position[1] - 20 > 0:
        ball_position[1] -= 20
    if keys[pygame.K_DOWN] and ball_position[1] + 20 < screen_height:
        ball_position[1] += 20
    if keys[pygame.K_LEFT] and ball_position[0] - 20 > 0:
        ball_position[0] -= 20
    if keys[pygame.K_RIGHT] and ball_position[0] + 20 < screen_width:
        ball_position[0] += 20

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, ball_color, (ball_position[0], ball_position[1]), ball_radius)

    pygame.display.flip()
    clock.tick(60)
