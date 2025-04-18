import pygame
import random
import time
import psycopg2

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "12345678",  # Замените на ваш пароль
    "port": "5432"
}

# Connect to the database
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS user_scores (
    score_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    score INT DEFAULT 0,
    level INT DEFAULT 1,
    saved_state TEXT,
    last_played TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()

# Function to get or create a user
def get_or_create_user(username):
    cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        return user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

# Function to load user data
def load_user_data(user_id):
    cur.execute("SELECT score, level, saved_state FROM user_scores WHERE user_id = %s ORDER BY last_played DESC LIMIT 1", (user_id,))
    data = cur.fetchone()
    if data:
        return data[0], data[1], data[2]
    return 0, 1, None

# Function to save user data
def save_user_data(user_id, score, level, saved_state):
    cur.execute("""
    INSERT INTO user_scores (user_id, score, level, saved_state)
    VALUES (%s, %s, %s, %s)
    """, (user_id, score, level, saved_state))
    conn.commit()

# Initialize the game
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
INITIAL_SPEED = 10
FOOD_PER_LEVEL = 3

# Levels configuration
LEVELS = {
    1: {"speed": 10, "walls": []},
    2: {"speed": 12, "walls": [[200, 200, 200, 400], [400, 200, 400, 400]]},
    3: {"speed": 15, "walls": [[100, 100, 500, 100], [100, 500, 500, 500], [100, 100, 100, 500], [500, 100, 500, 500]]},
}

class SnakeGame:
    def __init__(self, username):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game with Apples')
        self.user_id = get_or_create_user(username)
        self.score, self.level, self.saved_state = load_user_data(self.user_id)

        print(f"Welcome back, {username}! Your current level is {self.level}.")

        try:
            self.apple_images = {
                1: pygame.image.load(r'C:\path\to\apple.png'),
                2: pygame.image.load(r'C:\path\to\golden_apple.png'),
                3: pygame.image.load(r'C:\path\to\diamond_apple.png')
            }
            for key in self.apple_images:
                self.apple_images[key] = pygame.transform.scale(self.apple_images[key], (BLOCK_SIZE, BLOCK_SIZE))
        except:
            self.apple_images = {weight: pygame.Surface((BLOCK_SIZE, BLOCK_SIZE), pygame.SRCALPHA) for weight in [1, 2, 3]}
            pygame.draw.circle(self.apple_images[1], (255, 50, 50), (BLOCK_SIZE//2, BLOCK_SIZE//2), BLOCK_SIZE//2)
            pygame.draw.circle(self.apple_images[2], (255, 215, 0), (BLOCK_SIZE//2, BLOCK_SIZE//2), BLOCK_SIZE//2)
            pygame.draw.circle(self.apple_images[3], (173, 216, 230), (BLOCK_SIZE//2, BLOCK_SIZE//2), BLOCK_SIZE//2)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 25)
        self.reset_game()

    def reset_game(self):
        self.snake = [[SCREEN_WIDTH//2, SCREEN_HEIGHT//2]]
        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'
        self.food_eaten = 0
        self.game_over = False
        self.current_speed = LEVELS[self.level]["speed"]
        self.walls = LEVELS[self.level]["walls"]
        self.food_timer = 0
        self.generate_food()

    def generate_food(self):
        while True:
            food_pos = [
                random.randrange(BLOCK_SIZE, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE),
                random.randrange(BLOCK_SIZE, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            ]
            if food_pos not in self.snake and not any(self.check_wall_collision(food_pos)):
                self.food_pos = food_pos
                self.food_weight = random.choice([1, 2, 3])
                self.food_timer = time.time() + random.randint(5, 10)
                return

    def check_collision(self, position=None):
        if position is None:
            position = self.snake[0]
        if position[0] >= SCREEN_WIDTH or position[0] < 0 or position[1] >= SCREEN_HEIGHT or position[1] < 0:
            return True
        for segment in self.snake[1:]:
            if position == segment:
                return True
        return False

    def check_wall_collision(self, position):
        collisions = []
        for wall in self.walls:
            x1, y1, x2, y2 = wall
            if x1 <= position[0] <= x2 and y1 <= position[1] <= y2:
                collisions.append(True)
            else:
                collisions.append(False)
        return collisions

    def check_level_up(self):
        if self.food_eaten >= FOOD_PER_LEVEL:
            self.food_eaten = 0
            self.level += 1
            if self.level > max(LEVELS.keys()):
                self.level = 1
            self.current_speed = LEVELS[self.level]["speed"]
            self.walls = LEVELS[self.level]["walls"]
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

        if self.check_collision(head) or any(self.check_wall_collision(head)):
            self.game_over = True
            return

        self.snake.insert(0, head)
        if head == self.food_pos:
            self.score += self.food_weight * 10
            self.food_eaten += 1
            if self.check_level_up():
                self.screen.fill(WHITE)
                pygame.display.flip()
                time.sleep(0.2)
            self.generate_food()
        else:
            self.snake.pop()

        if time.time() > self.food_timer:
            self.generate_food()

    def draw_objects(self):
        self.screen.fill(BLACK)
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        # Draw walls
        for wall in self.walls:
            x1, y1, x2, y2 = wall
            pygame.draw.line(self.screen, RED, (x1, y1), (x2, y2), 5)

        self.screen.blit(self.apple_images[self.food_weight], (self.food_pos[0], self.food_pos[1]))
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
                    elif event.key == pygame.K_p:
                        self.save_game_state()
        return True

    def save_game_state(self):
        saved_state = {
            "snake": self.snake,
            "direction": self.direction,
            "next_direction": self.next_direction,
            "score": self.score,
            "level": self.level,
            "food_pos": self.food_pos,
            "food_weight": self.food_weight,
            "food_timer": self.food_timer
        }
        save_user_data(self.user_id, self.score, self.level, str(saved_state))
        print("Game state saved!")

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
    username = input("Enter your username: ")
    game = SnakeGame(username)
    game.run()
