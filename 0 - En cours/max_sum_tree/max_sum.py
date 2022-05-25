class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tab2bintree(tab: list):
    """ Renvoie l'arbre binaire correspondant, rempli en largeur d'abord  """
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


def liste_chemins(root: TreeNode):
    if root is None:
        return [[]]
    elif root.left is None:
        chemins_droite = liste_chemins(root.right)
        for c in chemins_droite:
            c.append(root)
        return chemins_droite
    elif root.right is None:
        chemins_gauche = liste_chemins(root.left)
        for c in chemins_gauche:
            c.append(root)
        return chemins_gauche
    else:
        chemins_gauche = liste_chemins(root.left)
        for c in chemins_gauche:
            c.append(root)
        chemins_droite = liste_chemins(root.right)
        for c in chemins_droite:
            c.append(root)
        return chemins_droite + chemins_gauche


def max_chemin(chemin: [TreeNode]):
    if not chemin:
        return -float("inf")
    acc_val = chemin[-1].val
    maxi = acc_val
    for i in range(len(chemin) - 2, -1, -1):
        n = chemin[i]
        acc_val += n.val
        maxi = max(maxi, acc_val)
    return maxi


def max_through_root(root: [TreeNode]):
    if root.left is None and root.right is None:
        return root.val
    chemins_gauche = liste_chemins(root.left)
    chemins_droite = liste_chemins(root.right)
    root_floor = max(0, root.val)
    max_gauche = max(max_chemin(c) for c in chemins_gauche)
    max_droite = max(max_chemin(c) for c in chemins_droite)
    return max(root.val,
               max_gauche + root_floor,
               max_droite + root_floor,
               max_gauche + max_droite + root.val)


def stupid(root: TreeNode):
    if root is None:
        return -float('inf')
    else:
        max_left = stupid(root.left)
        max_right = stupid(root.right)
        max_root = max_through_root(root)
        return max(max_left, max_right, max_root)
    # Passe les tests mais la complexité est vraiment beaucoup trop stupide


def affiche_liste_chemins(root: TreeNode):
    L = liste_chemins(root)
    # Afficher la liste des chemins de la racine à une feuille
    for c in L:
        print("Maximum", max_chemin(c))
        for n in c:
            print(n.val)
        print()

