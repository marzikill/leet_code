# Given the root of a binary tree and an integer targetSum, return all
# root-to-leaf paths where the sum of the node values in the path
# equals targetSum. Each path should be returned as a list of the node
# values, not node references.

# A root-to-leaf path is a path starting from the root and ending at
# any leaf node. A leaf is a node with no children.


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


root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
root = tab2bintree(root)


def ajoute_debut(listlist, e):
    return [[e] + c for c in listlist if len(listlist[0]) > 0]


def path_sum(root, target_sum):
    if root is None:
        return [[]]
    elif root.left is None and root.right is None:
        return [[root.val]] if root.val == target_sum else []
    else:
        chemins_à_gauche = path_sum(root.left, target_sum - root.val)
        chemins_à_droite = path_sum(root.right, target_sum - root.val)
        return ajoute_debut(chemins_à_gauche, root.val) + ajoute_debut(chemins_à_droite, root.val)


print(path_sum(root, 22))
