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

tab = [1, 2, 3, 4, 5, 6, 7]
tab = [2,1,3,None,4]
r = tab2bintree(tab)

def max_sum(r):
    if r is None: return 0
    return r.val + max(max_sum(r.left), max_sum(r.right))

def a_chemin_somme(r, somme_cible):
    if r is None: return False

    if r.left == None and r.right == None:
        return somme_cible == r.val
    else:
        return a_chemin_somme(r.left, somme_cible - r.val) or a_chemin_somme(r.right, somme_cible - r.val)

def rob(r, will_rob):
    if r is None:
        return 0
    else:
        a, b = rob(r.left, True), rob(r.right, True)
        c, d = rob(r.left, False), rob(r.right, False)
        if will_rob:
            return r.val + a + b
        else:
            return max(a + b, a + d, c + b, c + d)

def max_rob(r):
    return max(rob(r, True), rob(r, False))




    
    


