# Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

# For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

# B B W
# W W W
# W W W
# B B B
# Becomes

# B B G
# G G G
# G G G
# B B B
import random

def create_matrix(size):
    colors = {
        1: "R",
        2: "G",
        3: "B",
        4: "W",
        5: "O",
        6: "Y",
        7: "P",
        8: "K"
    }
    matrix = []
    for w in range(0, size[0]):
        for h in range (0, size[1]):
            c = colors[random.randint(1,8)]
            matrix[w].append(c)
    print(matrix)

create_matrix((3,3))