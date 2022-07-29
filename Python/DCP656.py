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

# Helper function to create a 2d array of given size
def create_matrix(size):
    colors = {
        1: 'R',
        2: 'G',
        3: 'B',
        4: 'W',
        5: 'O',
        6: 'Y',
        7: 'P',
        8: 'K'
    }
    matrix = []
    for w in range(0, size[0]):
        print()
        matrix.append([])
        for h in range (0, size[1]):
            c = colors[random.randint(1,3)]
            print(c, end=' ')
            matrix[w].append(c)
    print('\n')
    return matrix

def replace_pixel(matrix, location, C, original_C = ""):
    try:
        if matrix[location[0]][location[1]] == C:
            return matrix
    except IndexError:
        print(f'Location not in matrix, ending.')
        return matrix

    if original_C == "":
        original_C = matrix[location[0]][location[1]]
    
    if matrix[location[0]][location[1]] != original_C:
        return matrix

    print(f'height = {len(matrix)-1}  width = {len(matrix[0])-1}  location = {location}')
    print(f'original_C = {original_C} current color = {matrix[location[0]][location[1]]}')

    matrix[location[0]][location[1]] = C

    if location[0] >= len(matrix)-1:        
        return matrix
    elif matrix[location[0]+1][location[1]] == original_C:
        matrix = replace_pixel(matrix, (location[0]+1,location[1]), C, original_C)
    if location[1] >= len(matrix[0])-1:        
        return matrix
    elif matrix[location[0]][location[1]+1] == original_C:
        matrix = replace_pixel(matrix, (location[0],location[1]+1), C, original_C)
    if location[0] <= 0:        
        return matrix
    elif matrix[location[0]-1][location[1]] == original_C: 
        matrix = replace_pixel(matrix, (location[0]-1,location[1]), C, original_C)
    if location[1] <= 0:        
        return matrix
    elif matrix[location[0]][location[1]-1] == original_C:
        matrix = replace_pixel(matrix, (location[0],location[1]-1), C, original_C)
    return matrix

def replace_pixel_corners(matrix, location, C, original_C = ""):
    try:
        if matrix[location[0]][location[1]] == C:
            return matrix
    except IndexError:
        print(f'Location not in matrix, ending.')
        return matrix

    if original_C == "":
        original_C = matrix[location[0]][location[1]]
    
    if matrix[location[0]][location[1]] != original_C:
        return matrix

    print(f'height = {len(matrix)-1}  width = {len(matrix[0])-1}  location = {location}')
    print(f'original_C = {original_C} current color = {matrix[location[0]][location[1]]}')

    matrix[location[0]][location[1]] = C

    if location[0] >= len(matrix)-1:        
        return matrix
    elif matrix[location[0]+1][location[1]] == original_C:
        matrix = replace_pixel(matrix, (location[0]+1,location[1]), C, original_C)
    if location[1] >= len(matrix[0])-1:        
        return matrix
    else:  
        if matrix[location[0]][location[1]+1] == original_C:
            matrix = replace_pixel(matrix, (location[0],location[1]+1), C, original_C)
        if matrix[location[0]+1][location[1]+1] == original_C:
            matrix = replace_pixel(matrix, (location[0]+1,location[1]+1), C, original_C)
    if location[0] <= 0:        
        return matrix
    else:
        if matrix[location[0]-1][location[1]] == original_C: 
            matrix = replace_pixel(matrix, (location[0]-1,location[1]), C, original_C)
        if matrix[location[0]-1][location[1]+1] == original_C: 
            matrix = replace_pixel(matrix, (location[0]-1,location[1]+1), C, original_C)
    if location[1] <= 0:        
        return matrix
    else:
        if matrix[location[0]][location[1]-1] == original_C:
            matrix = replace_pixel(matrix, (location[0],location[1]-1), C, original_C)
        if matrix[location[0]-1][location[1]-1] == original_C:
            matrix = replace_pixel(matrix, (location[0]-1,location[1]-1), C, original_C)
        if matrix[location[0]+1][location[1]-1] == original_C:
            matrix = replace_pixel(matrix, (location[0],location[1]-1), C, original_C)
    return matrix

original_matrix = create_matrix((10,10))

replace_matrix = replace_pixel(original_matrix, (5,5), "R")
try:
    for i in replace_matrix:
        for j in i:
            print(j, end=' ')
        print()
    print()
except IndexError:
    print(f'Location not in matrix, ending.')

replace_matrix_corners = replace_pixel_corners(original_matrix, (5,5), "R")
try:
    for i in replace_matrix_corners:
        for j in i:
            print(j, end=' ')
        print()
    print()
except IndexError:
    print(f'Location not in matrix, ending.')

'''Answer: I decided on using recursion here, and created two solutions. One only works in straight lines (up, left, right, down)
 to change the pixel, the other counts "corners" (diagonally) as being adjacent as well. In an actual interview or during a task,
 I would ask for further clarification first.'''
