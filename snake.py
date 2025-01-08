import  pygame
import  time
import  random

pygame.init()

# Set the window size
window_x = 720
window_y = 480

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
# Create the game window
dis = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')

# Create a clock object to control the frame rate
clock = pygame.time.Clock()
# Set the initial snake speed and block size
snake_block = 10
snake_speed = 15

# Define the initial snake position and length
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
length_of_snake = 3
# Generate a random food position
food_position = [round(random.randrange(0, window_x - snake_block) / 10.0) * 10.0,
                 round(random.randrange(0, window_y - snake_block) / 10.0) * 10.0]
                 
def move_snake(direction):
    if direction == 'UP':
        snake_position[1] -= snake_block
    if direction == 'DOWN':
        snake_position[1] += snake_block
    if direction == 'LEFT':
        snake_position[0] -= snake_block
    if direction == 'RIGHT':
        snake_position[0] += snake_block

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def draw_food(food_position):
    pygame.draw.rect(dis, red, [food_position[0], food_position[1], snake_block, snake_block])
def game_loop():
    game_over = False
    game_close = False
    direction = 'RIGHT'

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                elif event.key == pygame.K_c:
                    game_loop()

        # Move the snake
        move_snake(direction)

        # Check for collision with food
        if snake_position == food_position:
            food_position = [round(random.randrange(0, window_x - snake_block) / 10.0) * 10.0,
                             round(random.randrange(0, window_y - snake_block) / 10.0) * 10.0]
            length_of_snake += 1
            snake_body.append(list(snake_position))

        # Update the snake body
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Check for collision with itself or the wall
        for x in snake_body[1:]:
            if x == snake_position:
                game_close = True
        if snake_position[0] < 0 or snake_position[0] > window_x - snake_block:
            game_close = True
        if snake_position[1] < 0 or snake_position[1] > window_y - snake_block:
            game_close = True

        # Draw the game elements
        dis.fill(black)
        draw_food(food_position)
        draw_snake(snake_block, snake_body)
        pygame.display.update()

        # Control the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()