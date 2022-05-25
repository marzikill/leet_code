# Given the root of a binary tree, determine if it is a valid binary
# search tree (BST).

# A valid BST is defined as follows:
# - The left subtree of a node contains only nodes with keys less
# than the node's key.
# - The right subtree of a node contains only nodes with keys greater 
# than the node's key.
# - Both the left and right subtrees must also be binary search trees.

# Constraints:
# - The number of nodes in the tree is in the range [1, 104].
# - -231 <= Node.val <= 231 - 1

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

tab = [2, 1, 3]
r = tab2bintree(tab)

def traversal_inorder(r, l):
    if r is None: pass
    else:
        traversal_inorder(r.left, l)
        l.append(r.val)
        traversal_inorder(r.right, l)
        
def est_trie_croissant(tab):
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True

def est_abr(r):
    valeurs = []
    traversal_inorder(r, valeurs)
    return est_trie_croissant(valeurs)

    

