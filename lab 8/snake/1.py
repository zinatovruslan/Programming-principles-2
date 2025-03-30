import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
INITIAL_SPEED = 10
FOOD_PER_LEVEL = 3

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game with Apples')

        try:
            self.apple_image = pygame.image.load(r'C:\Users\Askar\OneDrive - АО Казахстанско-Британский Технический Университет\Рисунки\images\apple.png')
            self.apple_image = pygame.transform.scale(self.apple_image, (BLOCK_SIZE, BLOCK_SIZE))
        except:
            self.apple_image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA)
            pygame.draw.circle(self.apple_image, (255, 50, 50), (BLOCK_SIZE//2, BLOCK_SIZE//2), BLOCK_SIZE//2)
            pygame.draw.rect(self.apple_image, (0, 150, 0), (BLOCK_SIZE//2-2, 2, 4, 6))

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 25)

        self.reset_game()
    
    def reset_game(self):
        self.snake = [[SCREEN_WIDTH//2, SCREEN_HEIGHT//2]]
        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'
        self.score = 0
        self.level = 1
        self.food_eaten = 0
        self.game_over = False
        self.current_speed = INITIAL_SPEED
        self.generate_food()
    
    def generate_food(self):
        while True:
            food_pos = [
                random.randrange(BLOCK_SIZE, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE),
                random.randrange(BLOCK_SIZE, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            ]
            
            if food_pos not in self.snake:
                self.food_pos = food_pos
                return
    
    def check_collision(self, position=None):
        if position is None:
            position = self.snake[0]

        if (position[0] >= SCREEN_WIDTH or position[0] < 0 or 
            position[1] >= SCREEN_HEIGHT or position[1] < 0):
            return True
        
        for segment in self.snake[1:]:
            if position == segment:
                return True
        
        return False
    
    def check_level_up(self):
        if self.food_eaten >= FOOD_PER_LEVEL:
            self.food_eaten = 0
            self.level += 1
            self.current_speed = INITIAL_SPEED + (self.level * 2)
            return True
        return False
    
    def update_snake(self):
        head = self.snake[0].copy()
        
        self.direction = self.next_direction
        
        if self.direction == 'UP':
            head[1] -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            head[1] += BLOCK_SIZE
        elif self.direction == 'LEFT':
            head[0] -= BLOCK_SIZE
        elif self.direction == 'RIGHT':
            head[0] += BLOCK_SIZE
        
        if self.check_collision(head):
            self.game_over = True
            return
        
        self.snake.insert(0, head)
        
        if head == self.food_pos:
            self.score += 10
            self.food_eaten += 1
            if self.check_level_up():
                self.screen.fill(WHITE)
                pygame.display.flip()
                time.sleep(0.2)
            self.generate_food()
        else:
            self.snake.pop()
    
    def draw_objects(self):
        self.screen.fill(BLACK)
        
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])
        
        self.screen.blit(self.apple_image, (self.food_pos[0], self.food_pos[1]))
        
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(score_text, [10, 10])
        self.screen.blit(level_text, [10, 40])
        
        if self.game_over:
            game_over_text = self.font.render("GAME OVER! Press R to restart", True, WHITE)
            self.screen.blit(game_over_text, [SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2])
        
        pygame.display.update()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.reset_game()
                else:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.next_direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.next_direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.next_direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.next_direction = 'RIGHT'
        
        return True
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            
            if not self.game_over:
                self.update_snake()
            
            self.draw_objects()
            self.clock.tick(self.current_speed)
        
        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
