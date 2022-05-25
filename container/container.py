#  You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

height = [1,8,6,2,5,4,8,3,7]
# height = [1, 3, 2, 6, 4, 3, 5, 1, 3, 4, 2, 3]

def volume(h, i, j):
    """ Returns the volume of water between line i-j """
    hauteur = min(h[i], h[j])
    return hauteur*(j - i)

def maximum_volume_with(h, i):
    """ Renvoie le volume maximum dans l'intervalle 
    d'indices 0..i """
    # Méthode naïve : on teste tous les poteaux précédents
    if i == 1:
        return volume(h, 0, 1)
    else:
        plus = maximum_volume_with(h, i - 1)
        for k in range(i):
            volume_k_to_i = volume(h, k, i)
            if volume_k_to_i > plus:
                plus = volume_k_to_i
        return plus
    # complexité quadratique : naze

# Avec une technique de mémoïsation
# J'ai honte de laisser ça.
# C'est complètement con. On transforme un algo
# quadratique en un algo quadratique..........
def maximum_volume_between(h, i, j, cache = {}):
    if cache.get((i, j)):
        return cache.get((i, j))
    if (i, j) == (0, 1):
        cache[(0, 1)] = volume(h, 0, 1)
        return volume(h, 0, 1), (0, 1)
    else:
        plus, bars = maximum_volume_between(h, i, j - 1)
        for k in range(i, j):
            volume_k_to_j = volume(h, k, j)
            if volume_k_to_j > plus:
                plus, bars = volume_k_to_j, (k, j) 
        cache[(i, j)] = plus, bars
        return plus, bars

def front_montant(height):
    """ Renvoie la liste des (i_k, h_{i_k}) de telle sorte que
    - le premier de la liste est (0, height[0])
    - i_k < i_{k + 1} (indices croissants)
    - h_{i_k} < h_{i_{k + 1}} (hauteurs croissantes)
    """
    front = [(-1, -float("inf"))]
    for i, h in enumerate(height):
        if h > front[-1][1]:
            front.append((i, h))
    return front
    # Complexité linéaire

def front_descendant(height):
    """ Renvoie la liste des (i_k, h_{i_k}) de telle sorte que
    - le premier de la liste est (len(height) - 1, height[-1])
    - i_k > i_{k + 1} (indices croissants)
    - h_{i_k} > h_{i_{k + 1}} (hauteurs croissantes)
    """
    front = [(-1, -float("inf"))]
    for i in range(len(height) - 1, -1, -1):
        h = height[i]
        if h > front[-1][1]:
            front.append((i, h))
    return front
    # Complexité linéaire

def max_volume(height):
    """ Renvoie le volume maximal d'un conteneur 
    dont les extrémités sont définies par la liste height """
    fm = front_montant(height)
    fd = front_descendant(height)
    i, j = len(fm) - 1, len(fd) - 1
    i_max, j_max = fm[i][0], fd[j][0]
    v_max = volume(height, fm[i][0], fd[j][0])
    while not ((i == 1) and (j == 1)):
        # On commence à faire la mise à jour des bords
        # du conteneur : de cette manière lorsque i == 1
        # et j == 1, on effectue quand même la
        # comparaison avec le maximum courant.
        
        # Si le descendant précédent est plus grand
        # que le front montant précédent
        # le front descendant devient le suivant
        if fd[j - 1][1] > fm[i - 1][1]:
            j -= 1
        # Si le front montant précédent est plus grand
        # que le front descendant suivant,
        # le front montant devient le suivant
        else:
            i -= 1

        # Mise à jour du maximum courant.
        v = volume(height, fm[i][0], fd[j][0])
        if v > v_max:
            v_max = v
            i_max, j_max = fm[i][0], fd[j][0]
    return v_max
    # Complexité linéaire
    # Faster than 78%
    
print(front_montant(height))
print(front_descendant(height))
print(max_volume([1, 1]))
            
def solution(h):
    return maximum_volume_with(h, len(h) - 1)
        
def solution2(h):
    return maximum_volume_between(h, 0, len(h) - 1)

# print(solution2(height))
