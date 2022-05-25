# Chaines de caractères
# Parcours simples
# Cas limites




# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lower-case English letters.



strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
strs = ["flower","flow","flight", ""]

def longest_common_prefix(strs):
    posis = 0
    posis_max = [len(str(s)) - 1 for s in strs]
    if any(t == -1 for t in posis_max):
        return ""
    N = len(strs)
    is_any_finished = False
    same = True
    while not is_any_finished and same:
        car = strs[0][posis]
        check_count = 0
        # parcourir tous les posis caractères de la liste
        # si un n'est pas le même que le premier : on s'arrête
        # On vérifie au passage que l'on peut continuer 
        while check_count < N and strs[check_count][posis] == car:
            if posis == posis_max[check_count]:
                is_any_finished = True
            check_count += 1
        if check_count == N:
            posis += 1
        else:
            same = False
    return strs[0][0:posis]
    
print(longest_common_prefix(strs))


            
