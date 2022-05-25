from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def est_feuille(self):
        return self.left is None and self.right is None

    def __str__(self):
        return f"({self.left}) - {self.val} - ({self.right})"

def tab_2_tree(tab):
    root = Node(tab[0], None, None)
    queue_node = deque([root])
    for i in range(1, len(tab) - 1, 2):
        current_node = queue_node.popleft()
        current_node.left = Node(tab[i], None, None)
        current_node.right = Node(tab[i + 1], None, None)
        queue_node.append(current_node.left)
        queue_node.append(current_node.right)
    return root
        
    
def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    queue = deque([root, None])
    while queue:
        sommet = queue.popleft()
        if sommet == None:
            pass
        elif queue[0] is None:
            sommet.next = None
            queue.append(sommet.left)
            queue.append(sommet.right)
            queue.append(None)
        else:
            sommet.next = queue[0]
            queue.append(sommet.left)
            queue.append(sommet.right)

tab = list(range(1, 8))
root = tab_2_tree(tab)
connect(root)
print(root)

