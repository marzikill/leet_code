# Parcours simple du tableau.
# Algorithme à trouver : raisonnement avec des dessins :
# comprendre la variable "max_atteignable"
# Programmation dynamique très simple : pas nécessaire

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:
#     1 <= nums.length <= 104
#     0 <= nums[i] <= 105

nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]

# Pas très efficace.
def jumpI(nums):
    T = [False for _ in nums]
    N = len(T)
    T[0] = True
    for i, r in enumerate(nums):
        if T[i]:
            for jump in range(i + 1, min(i + r + 1, N)):
                T[jump] = True
    return T[-1]

def jumpI2(nums):
    """ Détermine si le dernier index du tableau est atteignable """
    position = 0
    i_max = len(nums) - 1
    max_atteignable = min(nums[position], i_max)
    while position < max_atteignable < i_max:
        position += 1
        new_best_potentiel = min(position + nums[position], i_max)
        max_atteignable = max(max_atteignable, new_best_potentiel)
    return max_atteignable == i_max

        
print(jumpI(nums))
