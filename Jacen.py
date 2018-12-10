from sense_hat import SenseHat
sense = SenseHat()
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

matrix = [[WHITE for column in range(8)] for row in range(8)]

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

def gen_pipes(matrix):
    from random import randint
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
        row[-1] = BLUE
    return matrix

while True:
    matrix = gen_pipes(matrix)
    for i in range(9):
        matrix = move_pipes(matrix)
        sense.set_pixels(flatten(matrix))
        sleep(1)

matrix = gen_pipes(matrix)
matrix = flatten(matrix)
sense.set_pixels(matrix)
