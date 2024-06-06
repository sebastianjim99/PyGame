import pygame
import sys
import random

# Inicializar PyGame
pygame.init()

# Definir los colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Configurar la pantalla
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Culebrita")

# Definir los tamaños y velocidades
snake_size = 20
food_size = 20
clock = pygame.time.Clock()

# Fuentes
font = pygame.font.SysFont(None, 35)

# Función para mostrar texto en pantalla
def draw_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])

# Función para el menú de inicio
def game_menu():
    menu = True
    while menu:
        screen.fill(BLACK)
        draw_text("Juguemos culebrita", WHITE, 250, 200)
        draw_text("1. Novato", WHITE, 320, 250)
        draw_text("2. Intermedio", WHITE, 320, 300)
        draw_text("3. Avanzado", WHITE, 320, 350)
        draw_text("Selecciona el nivel de dificultad", WHITE, 230, 450)
        draw_text("Presionando el numero especifico", WHITE, 225, 470)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop(10, False)
                elif event.key == pygame.K_2:
                    game_loop(15, False)
                elif event.key == pygame.K_3:
                    game_loop(17, True) #Definimos velovidad y Si hay o no obstaculos, solo hay obtaculos en nivel avanzado

# Función para mostrar el menú de fin del juego
def game_over_menu(score):
    game_over = True
    while game_over:
        screen.fill(BLACK)
        draw_text(f"Fin del juego! Puntuación: {score}", RED, 250, 200)
        draw_text("1. Reintentar", WHITE, 320, 300)
        draw_text("2. Volver al menú", WHITE, 320, 350)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop(snake_speed, advanced_flag)
                elif event.key == pygame.K_2:
                    game_menu()

# Función para mostrar el puntaje en pantalla
def show_score(score):
    draw_text(f"Puntuación: {score}", WHITE, 10, 10)

# funciones del juego, enemigos, condiciones
def game_loop(speed, advanced):
    global snake_speed, advanced_flag
    snake_speed = speed
    advanced_flag = advanced
    game_over = False

    x1 = size[0] / 2
    y1 = size[1] / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, size[0] - snake_size) / 20.0) * 20.0
    foody = round(random.randrange(0, size[1] - snake_size) / 20.0) * 20.0

    obstacles = []
    if advanced:
        for _ in range(10):
            obstacle_x = round(random.randrange(0, size[0] - snake_size) / 20.0) * 20.0
            obstacle_y = round(random.randrange(0, size[1] - snake_size) / 20.0) * 20.0
            obstacles.append([obstacle_x, obstacle_y])  # Creación de obstaculos ramdom 

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_size

        if x1 >= size[0] or x1 < 0 or y1 >= size[1] or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [foodx, foody, food_size, food_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, [obstacle[0], obstacle[1], snake_size, snake_size]) #Obstaculos en color rojo
            if x1 == obstacle[0] and y1 == obstacle[1]:
                game_over = True

        draw_snake(snake_size, snake_list)
        show_score(length_of_snake - 1)
 
        # pygame.draw.rect(screen, RED, [0, 0, size[0], size[1]], 10)  # Marco rojo para delimitar 

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, size[0] - snake_size) / 20.0) * 20.0
            foody = round(random.randrange(0, size[1] - snake_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    game_over_menu(length_of_snake - 1)

# Función para dibujar la serpiente
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, WHITE, [x[0], x[1], snake_size, snake_size])

# Iniciar el juego
game_menu()
