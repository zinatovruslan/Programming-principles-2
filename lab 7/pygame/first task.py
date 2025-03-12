#1
import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mickey Mouse Clock")

clock_img = pygame.image.load(r"C:\Users\Askar\Pictures\images\mickeyclock.jpeg")
clock_img = pygame.transform.scale(clock_img, (500, 500))

minute_hand = pygame.image.load(r"C:\Users\Askar\Pictures\images\right_hand.jpeg").convert_alpha()
second_hand = pygame.image.load(r"C:\Users\Askar\Pictures\images\left_hand.jpeg").convert_alpha()

minute_hand = pygame.transform.scale(minute_hand, (150, 30))
second_hand = pygame.transform.scale(second_hand, (200, 20))

center_x, center_y = 250, 250

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))
    
    now = datetime.datetime.now()
    minute_angle = -6 * now.minute
    second_angle = -6 * now.second
    
    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)
    
    screen.blit(rotated_minute, rotated_minute.get_rect(center=(center_x, center_y)).topleft)
    screen.blit(rotated_second, rotated_second.get_rect(center=(center_x, center_y)).topleft)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.time.delay(1000)
    
pygame.quit()
