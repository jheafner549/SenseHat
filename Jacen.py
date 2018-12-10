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

matrix = gen_pipes(matrix)
matrix = flatten(matrix)
sense.set_pixels(matrix)
