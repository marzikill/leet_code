# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ajoute_noeud(valeur, chemins):
    for i, c in enumerate(chemins):
        chemins[i] = f"{valeur}->" + c


def chemins(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [f"{root.val}"]

    chemins_gauche = chemins(root.left)     # c_{h - 1}
    chemins_droit = chemins(root.right)     # c_{h - 1}
    ajoute_noeud(root.val, chemins_gauche)  # O(nombre de chemins_{h-1})
    ajoute_noeud(root.val, chemins_droit)   # O(nombre de chemins_{h-1})
    return chemins_gauche + chemins_droit   # O(nombre_de_chemins_{h-1})

# Très moche comme algorithme à optimiser. Par exemple :
# https://leetcode.com/problems/binary-tree-paths/discuss/68272/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively).
