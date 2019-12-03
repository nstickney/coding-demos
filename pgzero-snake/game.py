from random import randrange

# FOR PYGAME
WIDTH = 500
HEIGHT = 500

# THE SNAKE
positions = [(WIDTH / 2, HEIGHT / 2)]
snakes = [Actor('snake-segment', positions[-1])]

# SOME FOOD
food = [(randrange(0, WIDTH/10) * 10,
         randrange(0, HEIGHT/10) * 10) for _ in range(50)]

# MOVE THE SNAKE
MOVE_DIST = 10
move_time = 0.75
direction = 'N'

# GAME STATE
dead = False
won = False

def move_snake():

    global dead, won
    if dead or won:
        return

    global direction, positions
    if direction == 'N':
        positions.append((positions[-1][0], positions[-1][1] - MOVE_DIST))
    elif direction == 'E':
        positions.append((positions[-1][0] + MOVE_DIST, positions[-1][1]))
    elif direction == 'S':
        positions.append((positions[-1][0], positions[-1][1] + MOVE_DIST))
    else:
        positions.append((positions[-1][0] - MOVE_DIST, positions[-1][1]))

    global snakes
    for i, snake in enumerate(snakes):
        snake.pos = positions[-1-i]

    # Only save necessary position information
    positions = positions[-1-len(snakes):]

    # Did the snake eat?
    global food, move_time
    for bite in food[:]:
        if (abs(bite[0] - positions[-1][0]) < 10 and
                abs(bite[1] - positions[-1][1]) < 10):
            food.remove(bite)
            snakes.append(Actor('snake-segment', positions[0]))
            move_time *= 0.95

    # Are we dead? Did we win?
    if (positions[-1][0] <= 0 or positions[-1][0] >= WIDTH or
            positions[-1][1] <= 0 or positions[-1][1] >= HEIGHT or
            positions[-1] in positions[1:-1]):
        dead = True
    elif len(food) < 1:
        won = True

    # Move again!
    clock.schedule(move_snake, move_time)


# Make the first move
clock.schedule(move_snake, move_time)


# STEER THE SNAKE
def on_key_up(key):
    global direction
    if key == keys.LEFT or key == keys.S:
        direction = 'W'
    elif key == keys.RIGHT or key == keys.F:
        direction = 'E'
    elif key == keys.UP or key == keys.E:
        direction = 'N'
    elif key == keys.DOWN or key == keys.D:
        direction = 'S'


def draw():
    if dead:
        screen.fill((128, 0, 0))
    elif won:
        screen.fill((0, 0, 128))
    else:
        screen.fill((0, 128, 0))
        for bite in food:
            screen.draw.filled_rect(Rect((bite[0] - 4, bite[1] - 4),
                                         (8, 8)), (50, 40, 40))

        global snakes
        for snake in snakes:
            snake.draw()
