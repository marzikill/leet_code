def find_next_jump(t, i):
    """ Étant donné un tableau de sauts t et un index i
    détermine le prochain index d'où sauter """
    j = i + t[i]
    beg = j 
    if j <= 0:
        return 0
    while j < i and t[j] == t[j + 1]:
        j += 1
    return j if t[j] < t[beg] else beg
    
def count_jumps(t):
    """ Étant donné un tableau t de sauts construit
    détermine si l'index 0 est accessible """
    i = len(t) - 1
    count = 0
    while i > 0:
        j = find_next_jump(t, i)
        if i == j:
            return 0
        i = j
        count += 1
    return count

def jumpI2(nums):
    """ Détermine le nombre minimum de sauts pour atteindre la dernière case """
    N = len(nums)
    t = [0 for _ in range(N)]
    for i, jump in enumerate(nums):
        if t[min(i + jump, N - 1)] == 0:
            t[min(i + jump, N - 1)] = -jump + max(0, i + jump - (N - 1))
    print(t)
    c = count_jumps(t)
    return c

nums = [2, 3, 0, 1, 4]
nums = [2, 1, 3, 2, 3, 1, 0, 3]
nums = [1, 2, 3]
nums = [4,1,1,3,1,1,1]
nums = [1, 2, 3, 4, 5]
print(jumpI2(nums))
            
