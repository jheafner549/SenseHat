from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)

matrix = [[WHITE for column in range(8)] for row in range(8)]

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

def gen_pipes(matrix):
    for row in matrix:
        row[-1] = GREEN
    gap = randint(1,6)
    matrix[gap][-1] = WHITE
    matrix[gap - 1][-1] = WHITE
    matrix[gap + 1][-1] = WHITE
    return matrix

def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i + 1]
        row[-1] = WHITE
    return matrix

def draw_astronaut(event):
    global x
    global y
    sense.set(x, y, WHITE)
    if event.action == "pressed":
        if event.direction == "up":
            y -= 1
        elif event.direction == "down":
            y += 1
        elif event.direction == "right":
            x += 1
        elif event.direction == "left":
            x -= 1
    sense.set_pixel(x, y, PURPLE)
                    
sense.stick.direction_any = draw_astronaut

while True:
    matrix = gen_pipes(matrix)
    for i in range(3):
        sense.set_pixels(flatten(matrix))
        matrix = move_pipes(matrix)
        sense.set_pixel(x, y, PURPLE)
        sleep(1)

matrix = gen_pipes(matrix)
matrix = flatten(matrix)
sense.set_pixels(matrix)
