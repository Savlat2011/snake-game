
import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

score = 0

def game_over():
    font = pygame.font.Font(None, 70)
    text = font.render("Game Over", True, pygame.Color('red'))
    text_rect = text.get_rect(center=(RES // 2, RES // 2))
    sc.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

def display_score():
    font = pygame.font.Font(None, 30)
    text = font.render("Score: " + str(score), True, pygame.Color('black'))
    sc.blit(text, (10, 10))

while True:
    sc.fill(pygame.Color('orange'))

    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2 ))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 1
        score += 1

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)) or snake[-1] in snake[:-1]:
        game_over()
        break

    display_score()
    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
    if key[pygame.K_s]:
        dx, dy = 0, 1
    if key[pygame.K_a]:
        dx, dy = -1, 0
    if key[pygame.K_d]:
        dx, dy = 1, 0