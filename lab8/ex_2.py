import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('media/catch.mp3')

# Time variables
time_elapsed = 0
speed_increase_interval = 1000  # Increase speed every 1 seconds (in milliseconds)
speed_increase_amount = 0.2  # Amount by which speed increases
shrink_paddle_interval = 5000  # Shrink paddle every 5 seconds (in milliseconds)
shrink_paddle_amount = 10


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


# block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
                          100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255),
               random.randrange(0, 255), random.randrange(0, 255))
              for i in range(10) for j in range(4)]

# Randomly choose unbreakable blocks
unbreakable_block_list = []
for _ in range(5):  # Number of unbreakable blocks
    random_index = random.randint(0, len(block_list) - 1)
    unbreakable_block_list.append(block_list.pop(random_index))

unbreakable_color_list = [(0, 0, 255) for _ in range(len(unbreakable_block_list))]

bonus_brick_types = {
    "longer_paddle": {"color": (0, 255, 0), "perk": "paddle", "message": "Longer paddle!"},
    "increase_speed": {"color": (255, 165, 0), "perk": "speed", "message": "Speed Up!"},
}

bonus_brick_list = []
for _ in range(5):  # Number of bonus bricks
    random_index = random.randint(0, len(block_list) - 1)
    bonus_brick_type = random.choice(list(bonus_brick_types.keys()))
    bonus_brick_list.append((block_list.pop(random_index), bonus_brick_type))

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Message variables
message_font = pygame.font.SysFont('comicsansms', 40)
last_message = ""  # Stores the last message
last_message_rect = None  # Stores the last message's rect

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)

    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]  # drawing blocks
    [pygame.draw.rect(screen, (0, 0, 255), block) for block in unbreakable_block_list]  # drawing unbreakable blocks
    # Drawing bonus bricks

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()

    # Check collision with unbreakable blocks
    for i, unbreakable_block in enumerate(unbreakable_block_list):
        if ball.colliderect(unbreakable_block):
            dx, dy = detect_collision(dx, dy, ball, unbreakable_block)

    for block, bonus_type in bonus_brick_list:
        pygame.draw.rect(screen, bonus_brick_types[bonus_type]["color"], block)

    # Collision detection for bonus bricks
    for i, (bonus_brick, bonus_type) in enumerate(bonus_brick_list):
        if ball.colliderect(bonus_brick):
            # Apply perk of the bonus brick
            if bonus_brick_types[bonus_type]["perk"] == "life":
                # Implement logic to add extra life
                pass
            elif bonus_brick_types[bonus_type]["perk"] == "speed":
                # Implement logic to increase ball speed
                ballSpeed += 2  # Example increase in speed

            # Update last message
            last_message = bonus_brick_types[bonus_type]["message"]
            last_message_surface = message_font.render(last_message, True, (255, 255, 255))
            last_message_rect = last_message_surface.get_rect(
                topright=(W - 10, -5))  # Adjust position to top-right corner

            # Remove the bonus brick from the list
            del bonus_brick_list[i]
            break

        # Display last message
    if last_message:
        screen.blit(last_message_surface, last_message_rect)

    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Increase ball speed over time
    time_elapsed += clock.get_rawtime()
    if time_elapsed >= speed_increase_interval:
        ballSpeed += speed_increase_amount
        time_elapsed = 0

    # Shrink paddle over time
    if time_elapsed >= shrink_paddle_interval:
        paddleW -= shrink_paddle_amount
        if paddleW < 50:  # Limit the minimum width of the paddle
            paddleW = 50
        paddle.width = paddleW
        time_elapsed = 0

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)
