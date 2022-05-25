# A city's skyline is the outer contour of the silhouette formed by
# all the buildings in that city when viewed from a distance. Given
# the locations and heights of all the buildings, return the skyline
# formed by these buildings collectively.

# The geometric information of each building is given in the array
# buildings where buildings[i] = [lefti, righti, heighti]:

#     lefti is the x coordinate of the left edge of the ith building.
#     righti is the x coordinate of the right edge of the ith
#     building.  heighti is the height of the ith building.

# You may assume all buildings are perfect rectangles grounded on an
# absolutely flat surface at height 0.

# The skyline should be represented as a list of "key points" sorted
# by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key
# point is the left endpoint of some horizontal segment in the skyline
# except the last point in the list, which always has a y-coordinate 0
# and is used to mark the skyline's termination where the rightmost
# building ends. Any ground between the leftmost and rightmost
# buildings should be part of the skyline's contour.

# Note: There must be no consecutive horizontal lines of equal height
# in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11
# 5],[12 7],...] is not acceptable; the three lines of height 5 should
# be merged into one in the final output as such: [...,[2 3],[4 5],[12
# 7],...]

# Solution inspirée de :
# https://www.geeksforgeeks.org/the-skyline-problem-using-divide-and-conquer-algorithm/
# Livre de Darwish ?


buildings = [
    [2, 9, 10],
    [3, 7, 15],
    [5, 12, 12],
    [15, 20, 10],
    [19, 24, 8]
]

buildings = [
    [1, 2, 1],
    [1, 2, 2],
    [1, 2, 3]
]

buildings = [
    [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]
]

buildings = [[15, 20, 10], [19, 24, 8]]
buildings = [[1, 3, 3], [2, 4, 2]]

# sky1 = [(1, 11),  (3, 13),  (9, 0),  (12, 7),  (16, 0), (float("inf"), 0)]
# sky2 = [(14, 3),  (19, 18), (22, 3), (23, 13),  (29, 0), (float("inf"), 0)]


def merge_skyline(sky1, sky2):
    print(sky1, sky2)
    # Indice des points dans les skylines 1 et 2
    i1, i2 = 0, 0
    # Hauteur courante de la skyline 1 et 2
    h1, h2 = 0, 0
    # Simplifie la boucle while.
    sky1.append((float("inf"), -float("inf")))
    sky2.append((float("inf"), -float("inf")))
    sky_res = []
    while not (i1 == len(sky1) - 1 and i2 == len(sky2) - 1):
        # On ajoute le point dont la coordonnée x est la plus faible
        # on met à jour la hauteur courante de la skyline correspondante
        # et la hauteur courante est la plus haute des hauteur courantes
        # entre les deux des skylines.
        # On ajoute ce point uniquement si cela change la skyline
        # autrement dit si la nouvelle hauteur est différente de
        # la hauteur du point précédent.
        # Puis on incrémente l'indice de la skyline correspondante.
        # Faire un dessin avec un ou deux bâtiments.
        if sky1[i1][0] < sky2[i2][0]:
            h1 = sky1[i1][1]
            new_height = max(h1, h2)
            if not sky_res or new_height != sky_res[-1][1]:
                sky_res.append((sky1[i1][0], new_height))
            i1 += 1
        elif sky1[i1][0] > sky2[i2][0]:
            h2 = sky2[i2][1]
            new_height = max(h1, h2)
            if not sky_res or new_height != sky_res[-1][1]:
                sky_res.append((sky2[i2][0], new_height))
            i2 += 1
        else:
            # Le cas pénible où les deux skylines sont à la même abscisse
            # Faire un dessin pour comprendre.
            if sky1[i1][1] <= sky2[i2][1]:
                h2 = sky2[i2][1]
                if not sky_res or h2 != sky_res[-1][1]:
                    sky_res.append((sky2[i2][0], h2))
                i2 += 1
            else:
                h1 = sky1[i1][1]
                if not sky_res or h1 != sky_res[-1][1]:
                    sky_res.append((sky1[i1][0], h1))
                i1 += 1
    return sky_res


def find_skyline(buildings):
    """ Étant donné une liste de bâtiments, détermine la skyline
    via une méthode diviser pour régner. """
    # Si la liste est composée d'un unique bâtiment, alors
    # la skyline est constituée de deux points uniquement.
    if len(buildings) == 1:
        x, y, h = buildings[0]
        return [(x, h), (y, 0)]
    # Sinon : - [diviser] on divise la liste des bâtiments en deux,
    # - [résoudre] on trouve récursivement la skyline pour chacunes des listes
    # - [fusion] on fusionne les réponses aux deux sous-problèmes.
    else:
        n = len(buildings)
        buildings1, buildings2 = buildings[:n//2], buildings[n//2:]
        sky1, sky2 = find_skyline(buildings1), find_skyline(buildings2)
        return merge_skyline(sky1, sky2)


print(find_skyline(buildings))
