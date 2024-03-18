import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((830, 830))
clock = pygame.time.Clock()

mickey = pygame.image.load('images/mickey.png')
right_hand = pygame.image.load('images/right.png')
left_hand = pygame.image.load('images/left.png')

mickey_rect = mickey.get_rect(center=(415, 415))
left_hand_rect = left_hand.get_rect(center=mickey_rect.center)
right_hand_rect = right_hand.get_rect(center=mickey_rect.center)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.now().time()

    seconds_angle = current_time.second * 6
    minutes_angle = (current_time.minute * 60 + current_time.second) / 50

    rotated_left_hand = pygame.transform.rotate(left_hand, -seconds_angle)
    rotated_right_hand = pygame.transform.rotate(right_hand, -minutes_angle)

    left_hand_rect = rotated_left_hand.get_rect(center=mickey_rect.center)
    right_hand_rect = rotated_right_hand.get_rect(center=mickey_rect.center)

    screen.blit(mickey, mickey_rect)
    screen.blit(rotated_left_hand, left_hand_rect)
    screen.blit(rotated_right_hand, right_hand_rect)

    pygame.display.flip()

    clock.tick(60)
