import pygame

# Importing classes
from ball import Ball
from paddle import Paddle

# Start
pygame.init()

# GLOBALS
res_x = 800
res_y = 600
ball_radius = 10
paddle_speed = 6

frame_rate = 60

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)

# New window
screen = pygame.display.set_mode((res_x, res_y))
pygame.display.set_caption("Self-Playin\' pong")

# Creating list of all sprites
sprites_list = pygame.sprite.Group()

# Paddles (color, width, height)
paddleA = Paddle(white, 10, 100)
paddleA.rect.x = 20  # X and Y pos
paddleA.rect.y = (res_y // 2 - 50)  # -50 bc of the paddle height

paddleB = Paddle(white, 10, 100)
paddleB.rect.x = (res_x - 30)  # -30 bc of the paddle width
paddleB.rect.y = (res_y // 2 - 50)

sprites_list.add(paddleA, paddleB)

# Ball, just a ball
ball = Ball(white, [res_x // 2, res_y // 2], ball_radius)
sprites_list.add(ball)

# Player scores
scoreA, scoreB = 0, 0

# Continue to play until set to False
isRunning = True

# Controlling frame-rate
clock = pygame.time.Clock()

# --Main loop--
while isRunning:
    for event in pygame.event.get():  # If user did something
        if event.type == pygame.QUIT:  # And something == quitting
            isRunning = False  # Exit the loop and close the game
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    # --SOME GAME LOGIC--
    ball.run()

    # --"CONTROLS"--
    # Left paddle (A)
    if ball.velocity[0] < 0:
        if ball.rect.y + ball_radius < paddleA.rect.y + 50:  # If ball is upper than paddle move it
            if ball.rect.y + ball_radius > paddleA.rect.y + 40:  # Makes it smoother
                paddleA.move_up(paddle_speed // 2)
            else:
                paddleA.move_up(paddle_speed)
        elif ball.rect.y + ball_radius > paddleA.rect.y + 70:  # If ball is lower than paddle
            if ball.rect.y + ball_radius < paddleA.rect.y + 80:
                paddleA.move_down(paddle_speed // 2, res_y)
            else:
                paddleA.move_down(paddle_speed, res_y)
    # Right paddle (B)
    if ball.velocity[0] > 0:
        if ball.rect.y + ball_radius < paddleB.rect.y + 50:
            if ball.rect.y + ball_radius > paddleB.rect.y + 40:
                paddleB.move_up(paddle_speed // 2)
            else:
                paddleB.move_up(paddle_speed)
        elif ball.rect.y + ball_radius > paddleB.rect.y + 70:
            if ball.rect.y + ball_radius < paddleB.rect.y + 80:
                paddleB.move_down(paddle_speed // 2, res_y)
            else:
                paddleB.move_down(paddle_speed, res_y)

    # --BALL HITTING WALLS--
    if ball.rect.x >= res_x - ball_radius:  # Right
        scoreA += 1
        ball.replay([res_x // 2, res_y // 2])
    if ball.rect.x <= 0:  # Left
        scoreB += 1
        ball.replay([res_x // 2, res_y // 2])
    if ball.rect.y <= 0:  # Up
        ball.velocity[1] = abs(ball.velocity[1])
    if ball.rect.y >= res_y - ball_radius:  # Down
        ball.velocity[1] = -abs(ball.velocity[1])

    # --BALL BOUNCING OFF PADDLES--
    if (pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB)) and not ball.isBouncing:
        ball.bounce()
        ball.isBouncing = True
    else:
        ball.isBouncing = False

    # --DRAWINGS--
    # Filling screen black, just in case
    screen.fill(black)
    # Drawing a net
    pygame.draw.line(screen, white, [res_x // 2, 0], [res_x // 2, res_y])
    # Drawing all sprites
    sprites_list.draw(screen)

    # --SCORING SYSTEM--
    font = pygame.font.Font(None, 72)
    text = font.render(str(scoreA), 1, white)
    screen.blit(text, (int(res_x // 2.8), 10))
    text = font.render(str(scoreB), 1, white)
    screen.blit(text, (int(res_x // 1.6), 10))
    # Updating the screen to show everything
    pygame.display.flip()

    # --FRAME LIMIT--
    clock.tick(frame_rate)

# Exit the game if isRunning == False
pygame.quit()
