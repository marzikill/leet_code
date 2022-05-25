# Given a binary tree, find the lowest common ancestor (LCA) of two given
# nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common
# ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a
# descendant of itself).”

# Constraints:
# - The number of nodes in the tree is in the range [2, 105].
# - -109 <= Node.val <= 109
# - All Node.val are unique.
# - p != q
# - p and q will exist in the tree.


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

tab = [3,5,1,6,2,0,8,None,None,7,4]
r = tab2bintree(tab)

def path_to(root, elt):
    if root is None: return []
    if root.val == elt:
        return [0]
    else:
        p1 = path_to(root.left, elt)
        p2 = path_to(root.right, elt)
        if p1 != []:
            p1.append(-1)
            return p1
        elif p2 != []:
            p2.append(1)
            return p2
        else:
            return []
        
def ancestor(r, e1, e2):
    p1 = path_to(r, e1)
    p2 = path_to(r, e2)
    p1.reverse() # 
    p2.reverse() # facultatif... (mais pour le dessin)
    noeud = r
    i = 0
    while p1[i] == p2[i]:
        if p1[i] == -1:
            noeud = noeud.left
        elif p1[i] == 1:
            noeud = noeud.right
        else:
            return noeud.val
        i += 1
    return noeud.val

assert ancestor(r, 5, 1) == 3
assert ancestor(r, 5, 4) == 5
assert ancestor(r, 6, 8) == 3
assert ancestor(r, 0, 1) == 1
assert ancestor(r, 7, 4) == 2
