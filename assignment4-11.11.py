import pygame

pygame.init()

# Set screen resolution
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Maze Game")

# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (50,50,50)
BLUE = (50,50,50)
GREEN = (50,50,50)


# Set up the player
player_x = 30
player_y = 30

player_x2 = 1860
player_y2 = 960

player_width = 25
player_length = 100

speed = 7
ballspeed = 7

ball_x = 1000
ball_y = 500

# Create the exit
exit_rect = pygame.Rect(0, 0, 1, 30)

# Create the maze walls
walls = [
    pygame.Rect(100, 0, 20, 300),
    pygame.Rect(200, 100, 20, 300),
    pygame.Rect(300, 0, 20, 250),
    pygame.Rect(400, 100, 20, 300),
    pygame.Rect(500, 0, 20, 250)
]

# Set up the game
clock = pygame.time.Clock()
running = True
won = False

# Main game loop
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    if not won:

        # Move up
        if keys[pygame.K_UP]:
            player_y2 -= speed
            player = pygame.Rect(player_x2, player_y2, player_width, player_length)

            for wall in walls:
                if player.colliderect(wall):
                    player_y2 += speed

        # Move down
        if keys[pygame.K_DOWN]:
            player_y2 += speed
            player = pygame.Rect(player_x2, player_y2, player_width, player_length)

            for wall in walls:
                if player.colliderect(wall):
                    player_y2 -= speed

        #player 2 up
        if keys[pygame.K_w]:
            player_y -= speed
            player = pygame.Rect(player_x, player_y, player_width, player_length)
            
            for wall in walls:
                if player.colliderect(wall):
                    player_y -= speed

        #player 2 down
        if keys[pygame.K_s]:
            player_y += speed
            player = pygame.Rect(player_x, player_y, player_width, player_length)
            
            for wall in walls:
                if player.colliderect(wall):
                    player_y += speed

        #ball movement

        ball_x += ballspeed
        

        if ball_x == player_x:
            ball_x -= ballspeed
        elif ball_x == player_x2:
            ball_x == player_x
        ball = pygame.Rect(ball_x, ball_y, 30, 30)
        # Keep the player inside the screen
        if player_x < 0:
            player_x = 0

        if player_x > SCREEN_WIDTH - player_width:
            player_x = SCREEN_WIDTH - player_width

        if player_y < 0:
            player_y = 0

        if player_y > SCREEN_HEIGHT - player_length:
            player_y = SCREEN_HEIGHT - player_length

        #Player 2 inside the screen

        if player_x2 < 0:
            player_x2 = 0

        if player_x2 > SCREEN_WIDTH - player_width:
            player_x2 = SCREEN_WIDTH - player_width

        if player_y2 < 0:
            player_y2 = 0

        if player_y2 > SCREEN_HEIGHT - player_length:
            player_y2 = SCREEN_HEIGHT - player_length

        #ball bouncing (inside the screen)

        if ball_x < 0:
            ball_x = 0

        if ball_x > SCREEN_WIDTH - 15:
            ball_x = SCREEN_WIDTH - ballspeed

        if ball_y < 0:
            ball_y = 0

        if ball_y > SCREEN_HEIGHT - 15:
            ball_y = SCREEN_HEIGHT - ballspeed



        # Update the player rectangle
        player = pygame.Rect(player_x, player_y, player_width, player_length)
        player2 = pygame.Rect(player_x2, player_y2, player_width, player_length)
        #ball = pygame.circle(ball_x, ball_y)
        #ball = pygame.circle(ball_x, ball_y, 15)
        
        ball_hitbox = pygame.Rect(ball_x, ball_y, 30, 30)

        # Check if the player reaches the exit
        if player.colliderect(exit_rect):
            won = True

    # Draw the background
    screen.fill(BLACK)

    # Draw the maze walls


    # Draw the exit
    pygame.draw.rect(screen, GREEN, exit_rect)

    # Draw the player
    player = pygame.Rect(player_x, player_y, player_width, player_length)
    pygame.draw.rect(screen, WHITE, player)

    player2 = pygame.Rect(player_x2, player_y2, player_width, player_length)
    pygame.draw.rect(screen, WHITE, player2)
    
    #draw the ball
    pygame.draw.circle(screen, WHITE, (ball_x,ball_y),15)
    
   
    
    
    # Display the winning message

    if won:
        font = pygame.font.SysFont(None, 48)
        message = font.render("YOU WIN!", True, BLACK)
        screen.blit(message, (220, 180))

    # Update the display
    pygame.display.flip()

    # Limit the game to 60 FPS
    clock.tick(60)

# Close Pygame
pygame.quit()

"""

started coding the ball

"""
