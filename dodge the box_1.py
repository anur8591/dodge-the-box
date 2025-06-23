import pygame
import random 
import sys

pygame.init()

Width = 800      # Width of the game window in pixels
Height = 600     # Height of the game window in pixels
win = pygame.display.set_mode((Width, Height))  # Create game window
pygame.display.set_caption("Dodge the Box")     # Set the window title

clock = pygame.time.Clock()  # Controls how fast the game runs


blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

high_score = 0 

font = pygame.font.SysFont("Arial", 30)          # For score display
game_over_font = pygame.font.SysFont("Arial", 60)  # For game over message

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = Width // 2 - self.width // 2  # Start horizontally centered
        self.y = Height - self.height - 10     # Start near the bottom
        self.speed = 7                         # Speed of movement

    def draw(self, win):
        # Draw the player as a blue square
        pygame.draw.rect(win, blue, (self.x, self.y, self.width, self.height))

    def moves(self, keys):
        # Handle left/right movement using arrow keys or A/D
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed

        # Keep the player inside the screen
        self.x = max(0, min(self.x, Width - self.width))

class Enemy:
    def __init__(self, speed):
        self.width = 40
        self.height = 40
        self.x = random.randint(0, Width - self.width)  # Random X position
        self.y = -self.height  # Start just above the screen
        self.speed = speed     # How fast the enemy falls

    def fall(self):
        self.y += self.speed  # Move the enemy downwards

    def draw(self, win):
        # Draw the enemy as a red square
        pygame.draw.rect(win, red, (self.x, self.y, self.width, self.height))

    def off_screen(self):
        # Return True if enemy moves below the bottom of the screen
        return self.y > Height

def is_collision(player, enemy):
    # AABB (Axis-Aligned Bounding Box) collision logic
    return (
        player.x < enemy.x + enemy.width and
        player.x + player.width > enemy.x and
        player.y < enemy.y + enemy.height and
        player.y + player.height > enemy.y
    )

def game_over_screen(score, high_score):
    win.fill(black)  # Clear the screen with black

    # Render all the messages
    title = game_over_font.render("Game Over!", True, red)
    score_text = font.render(f"Score: {score}", True, white)
    high_score_text = font.render(f"High Score: {high_score}", True, white)
    restart_text = font.render("Click to Restart or Press Enter", True, gray)

    # Show the text at the center
    win.blit(title, (Width // 2 - title.get_width() // 2, Height // 3))
    win.blit(score_text, (Width // 2 - score_text.get_width() // 2, Height // 2))
    win.blit(high_score_text, (Width // 2 - high_score_text.get_width() // 2, Height // 2 + 40))
    win.blit(restart_text, (Width // 2 - restart_text.get_width() // 2, Height // 2 + 100))

    pygame.display.update()  # Update screen with new drawings

    # Wait for player to click or press Enter to restart
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                waiting = False  # Exit loop and restart game

def main():
    global high_score  # Access the global high_score variable

    # Create player and enemy list
    player = Player()
    enemies = []
    enemy_speed = 5
    score = 0

    # Game loop starts here
    running = True
    while running:
        clock.tick(60)
        win.fill(black)  # Clear the screen with black

        keys = pygame.key.get_pressed()  # Get currently held-down keys

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.moves(keys)
        player.draw(win)

        # Randomly create a new enemy
        if random.randint(1, 25) == 5:
            enemies.append(Enemy(enemy_speed))

        # Update each enemy
        for enemy in enemies[:]:
            enemy.fall()
            enemy.draw(win)

            if is_collision(player, enemy):
                running = False  # Game over if hit

            if enemy.off_screen():
                enemies.remove(enemy)
                score += 1

                # Increase speed every 15 points
                if score % 15 == 0:
                    enemy_speed += 1

        # Show score during the game
        score_text = font.render(f"Score: {score}", True, white)
        win.blit(score_text, (10, 10))

        pygame.display.update()  # Refresh the screen

    if score > high_score:
        high_score = score

    game_over_screen(score, high_score)

    # Restart game by calling main() again
    main()
main()
