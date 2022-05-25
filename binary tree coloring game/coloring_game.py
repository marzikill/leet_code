# Two players play a turn based game on a binary tree. We are given the
# root of this binary tree, and the number of nodes n in the tree. n is o
# dd, and each node has a distinct value from 1 to n.

# Initially, the first player names a value x with 1 <= x <= n, and the
# second player names a value y with 1 <= y <= n and y != x. The first pl
# ayer colors the node with value x red, and the second player colors the
# node with value y blue.

# Then, the players take turns starting with the first player. In each
# turn, that player chooses a node of their color (red if player 1, blue
# if player 2) and colors an uncolored neighbor of the chosen node (either
# the left child, right child, or parent of the chosen node.)

# If (and only if) a player cannot choose such a node in this way, they
# must pass their turn. If both players pass their turn, the game ends,
# and the winner is the player that colored more nodes.

# You are the second player. If it is possible to choose such a y to
# ensure you win the game, return true. Otherwise, return false.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tab2bintree(tab):
    """tab est un tableau.
    Renvoie l'arbre binaire correspondant, rempli en largeur d'abord"""
    if not tab:
        return None
    root = TreeNode(val=tab.pop(0))
    liste = [root]
    while not tab == []:
        noeud = liste.pop(0)
        noeud.left = TreeNode(val=tab.pop(0))
        liste.append(noeud.left)
        if not tab == []:
            noeud.right = TreeNode(val=tab.pop(0))
            liste.append(noeud.right)
    return root


tab = [1, 2, 3, 4]
r = tab2bintree(tab)
print(r)


def print_tree(r):
    if r is None:
        print("", end="")
    else:
        print_tree(r.left)
        print(r.val, end="")
        print_tree(r.right)


def find(tree_root, elt):
    if tree_root is None:
        return False
    else:
        if tree_root.val == elt:
            return True
        else:
            return find(tree_root.left, elt) or find(tree_root.right, elt)


def select(tree_root, elt):
    if tree_root is None:
        return None
    else:
        if tree_root.val == elt:
            return tree_root
        else:
            is_left = select(tree_root.left, elt)
            return is_left if is_left else select(tree_root.right, elt)


def count_elt(tree_root):
    if tree_root is None:
        return 0
    else:
        return 1 + count_elt(tree_root.right) + count_elt(tree_root.left)


def winning_strat(tree_root, n, x):
    noeud = select(tree_root, x)
    noeud_taille_gauche = count_elt(noeud.left)
    noeud_taille_droit = count_elt(noeud.right)
    noeud_taille_above = n - 1 - noeud_taille_droit - noeud_taille_gauche
    points = [noeud_taille_gauche, noeud_taille_droit, noeud_taille_above]

    return (
        noeud_taille_above > 1 + noeud_taille_droit + noeud_taille_gauche
        or noeud_taille_gauche > 1 + noeud_taille_droit + noeud_taille_above
        or noeud_taille_droit > 1 + noeud_taille_gauche + noeud_taille_above
    )
