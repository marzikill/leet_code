# Given the root of a binary tree and an integer targetSum, return the
# number of paths where the sum of the values along the path equals
# targetSum.

# The path does not need to start or end at the root or a leaf, but it
# must go downwards (i.e., traveling only from parent nodes to child
# nodes).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tab2bintree(tab):
    """ tab est un tableau.
    Renvoie l'arbre binaire correspondant, rempli en largeur d'abord  """
    if not tab:
        return None
    root = TreeNode(tab.pop(0))
    liste = [root]
    while not tab == []:
        noeud = liste.pop(0)
        x1 = tab.pop(0)
        if x1 is not None:
            noeud.left = TreeNode(x1)
            liste.append(noeud.left)
        if not tab == []:
            x2 = tab.pop(0)
            if x2 is not None:
                noeud.right = TreeNode(x2)
                liste.append(noeud.right)
    return root


root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
root = tab2bintree(root)
gauche = [5, 3, 2, 3, -2, None, 1]
gauche = tab2bintree(gauche)


def path_sumII(root, target_sum, anchor_root=False):
    """ Détermine le nombre de chemins issus d'un noeud de l'arbre de racine root jusqu'à un 
    de ses noeuds descendant dont la somme des noeuds du chemin vaut target_sum 
    Si anchor_root = True : compte uniquement les chemins issus de la racine. """
    if root is None:
        return 0

    if not anchor_root:
        nb_gauche = path_sumII(root.left, target_sum) + \
            path_sumII(root.left, target_sum - root.val, anchor_root=True)
        nb_droit = path_sumII(root.right, target_sum) + \
            path_sumII(root.right, target_sum - root.val, anchor_root=True)
    else:
        nb_gauche = path_sumII(
            root.left, target_sum - root.val, anchor_root=True)
        nb_droit = path_sumII(
            root.right, target_sum - root.val, anchor_root=True)
    return nb_droit + nb_gauche + int(root.val == target_sum)
    # Complexité : ça a au moins le mérite de fonctionner.....


print(path_sumII(root, 8))
