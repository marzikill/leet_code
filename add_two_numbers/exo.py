 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next is None:
            return f"{self.val} - •"
        else:
            return f"{self.val} - {self.next}"
            

class Solution:
    def recursive_add(self, l1, l2, ret):
        """ ajoute l1 et l2 et la liste (ret) """
        if l1 is None and l2 is None:
            return None
        d, ret = (ret + l1.val + l2.val)%10, (ret + l1.val + l2.val)//10
        # Si une exactement des listes ne contient qu'un seul chiffre
        if (l1.next is None)^(l2.next is None):
            # On propage la retenue sur l'autre liste 
            if l1.next is None:
                return ListNode(d, self.recursive_add(ListNode(0, None), l2.next, ret))
            elif l2.next is None:
                return ListNode(d, self.recursive_add(l1.next, ListNode(0, None), ret))
        # si exactement deux des listes ne contiennent qu'un seul chiffre : on renvoit la liste "{d} - {ret} - •"
        elif (l1.next is None) and (l2.next is None):
            if ret == 1:
                return ListNode(d, ListNode(1, None))
            else:
                return ListNode(d, None)
        # Sinon on ajoute récursivement les deux listes
        else:
            return ListNode(d, self.recursive_add(l1.next, l2.next, ret))
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.recursive_add(l1, l2, 0)

def tab_2_list(t):
    """ Prend un tableau et le converti en liste chaînée """
    if len(t) == 0:
        return None
    else:
        return ListNode(t[0], tab_2_list(t[1:]))

tests = [
    [[0, 1], [0, 2, 0, 3]],
    [[2, 4, 3], [5, 6, 4]],
    [[9,9,9,9,9,9,9], [9,9,9,9]]
] 

for t in tests:
    print(Solution().addTwoNumbers(tab_2_list(t[0]), tab_2_list(t[1])))

