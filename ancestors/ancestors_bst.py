# Given a binary search tree (BST), find the lowest common ancestor (LCA)
# of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common
# ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a
# descendant of itself).”

# Constraints:
# - The number of nodes in the tree is in the range [2, 105].
# - -109 <= Node.val <= 109
# - All Node.val are unique.
# - p != q
# - p and q will exist in the BST.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tab2bintree(tab):
    """ tab est un tableau. 
    Renvoie l'arbre binaire correspondant, rempli en largeur d'abord  """
    if not tab: return None
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

tab = [6,2,8,0,4,7,9,None,None,3,5]
r = tab2bintree(tab)

def order(e1, e2):
    return (e1, e2) if e1 < e2 else (e2, e1)

def ancestor(r_bst, e1, e2):
    e1, e2 = order(e1, e2)
    if r_bst.val == e1 or r_bst.val == e2:
        return r_bst.val
    else:
        if e1 < r_bst.val < e2:
            return r_bst.val
        elif e1 <= e2 < r_bst.val:
            return ancestor(r_bst.left, e1, e2)
        else:
            return ancestor(r_bst.right, e1, e2)

def ancestor_test():
    assert ancestor(r, 2, 8) == 6
    assert ancestor(r, 2, 6) == 6
    assert ancestor(r, 0, 5) == 2
    assert ancestor(r, 2, 7) == 6
    assert not ancestor(r, 2, 7) == 8
