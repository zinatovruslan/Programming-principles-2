#3
import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Ball")

ball_x, ball_y = 250, 250
radius = 25
speed = 20

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), radius)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - radius - speed >= 0:
                ball_y -= speed
            elif event.key == pygame.K_DOWN and ball_y + radius + speed <= 500:
                ball_y += speed
            elif event.key == pygame.K_LEFT and ball_x - radius - speed >= 0:
                ball_x -= speed
            elif event.key == pygame.K_RIGHT and ball_x + radius + speed <= 500:
                ball_x += speed

pygame.quit()
