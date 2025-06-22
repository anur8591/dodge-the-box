import pygame
import random
import sys
pygame.init()

Width, Height = 500, 600
win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Dodge the box")

clock = pygame.time.clock()

blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

class Player:
    def __init__(self):
        self.width = 50
        self.hight = 50
        self.a = Width // 2 - self.width // 2
        self.b = Height - self.hight - 10
        self.speed = 7

    def draw(self, win):
        pygame.draw.rect(win, blue,(self.a, self.b, self.hight, self.width))

    def moves(self, keys):
        if keys[pygame.k_left] or keys[pygame.k_a] or keys[pygame.k_A]:
            self.a -= self.speed
        if keys[pygame.k_left] or keys[pygame.k_d] or keys[pygame.k_D]:
            self.a += self.speed

        self.a = max(0, min(self.a, Width - self.width))


class Enemy:
    def __init__(self, speed):
        self.width = 40
        self.height = 40
        self.x = random.randint(0,Width - self.width)
        self.y = -self.height
        self.speed = speed

    def fall(self):
        self.y += self.speed

    def draw(self, win):
        pygame.draw.rect(win, red,(self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.y > Height
    
def is_colllision(player, enemy):
    return(
        player.a < enemy.a + enemy.width and
        player.x + player.width > enemy.x and
        player.b < enemy.b + enemy.height and
        player.y + player.height > enemy.y
    )

def main():
    player = Player()
    enemies = []
    enemy_speed = 5
    score = 0
    font = pygame.font.SysFont("Arial", 300)

    running = True
    while running:
        clock.tick(60) 
        win.fill(black)

        keys = pygame.key.get_pressed()
        for enent in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.move(keys)
        player.draw(win)

        if random.randint(1, 20) == 1:
            enemies.append(Enemy(enemy_speed))
        
        for enemy in enemies[:]:
            enemy.fall()
            enemy.draw(win)

            if is_collision(player, enemy):
                running = False

            if enemy.off_screen():
                enemies.remove(enemy)
                score += 1
                

            