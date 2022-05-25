# There is a city composed of n x n blocks, where each block contains a single
# building shaped like a vertical square prism. You are given a 0-indexed n x n
# integer matrix grid where grid[r][c] represents the height of the building
# located in the block at row r and column c.

# A city's skyline is the the outer contour formed by all the building when
# viewing the side of the city from a distance. The skyline from each cardinal
# direction north, east, south, and west may be different.

# We are allowed to increase the height of any number of buildings by any
# amount (the amount can be different per building). The height of a 0-height
# building can also be increased. However, increasing the height of a building
# should not affect the city's skyline from any cardinal direction.

# Return the maximum total sum that the height of the buildings can be
# increased by without changing the city's skyline from any cardinal direction.

# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: The building heights are shown in the center of the above image.
# The skylines when viewed from each cardinal direction are drawn in red.
# The grid after increasing the height of buildings without affecting skylines:

# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]
# vue ouest : [8, 7, 9, 3]
# vue sud : [9, 4, 8, 7])


grid = [
    [3, 0, 8, 4],
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
]


def get_skyline(grid):
    """ Étant donné une grille, renvoie le dictionnaire
    des skylines, sud/ouest """
    ouest = list(map(max, grid))
    south = []
    for j in range(len(grid)):
        maxi = grid[0][j]
        for i in range(len(grid)):
            if grid[i][j] > maxi:
                maxi = grid[i][j]
        south.append(maxi)
    return ouest, south


def make_higher_same_skyline(grid):
    """ Transforme la grille afin que les buildings
    soient le plus haut possible. Ne modifie pas
    la skyline.
    Renvoie la somme totale d'augmentation de hauteur. """
    somme = 0
    ouest, sud = get_skyline(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            max_possible = min(ouest[i], sud[j])
            if grid[i][j] < max_possible:
                somme += max_possible - grid[i][j]
                grid[i][j] = max_possible
    return somme


print("\n".join(map(str, grid)))
print(get_skyline(grid))
print(make_higher_same_skyline(grid))
print("\n".join(map(str, grid)))
