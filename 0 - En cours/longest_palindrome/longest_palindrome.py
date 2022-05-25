from functools import cache

def fits(k, l, i, j, s):
    return (k == i + 1 and k + l == j - 1 and s[i] == s[j - 1])

@cache
def sol_rec(s, i, j, cache = {}):
    # if cache.get((i, j)):
    #     return cache[(i, j)]
    if i >= j:
        # cache[(i, j)] = i, 0
        return i, 0
    elif i + 1 == j:
        # cache[(i, j)] = i, 1
        return i, 1
    else:
        if s[i] == s[j-1]:
            k, t = sol_rec(s, i + 1, j - 1)
            if k == i + 1 and k + t == j - 1:
                # cache[(i, j)] = i, t + 2
                return i, t + 2
        k1, l1 = sol_rec(s, i + 1, j)
        k2, l2 = sol_rec(s, i , j - 1)
        l = max(l1, l2)
        if fits(k1, l1, i, j, s) or fits(k2, l2, i, j, s):
            # cache[(i, j)] = i, j - i
            return i, j - i 
        else:
            if l1 > l2:
                # cache[(i, j)] = k1, l1
                return k1, l1
            else:
                # cache[(i, j)] = k2, l2
                return k2, l2

def formata(t):
    n = len(t)
    m = len(t[0])
    s_col = 15
    s = ""
    for i in range(n):
        s += "_"*(s_col*m + 1 + m) + "\n"
        for j in range(m):
            s += str(t[i][j]).rjust(15) if t[i][j] else "                "
            s += "|"
        s += "\n"
    s += "_"*(s_col*m + 1 + m) + "\n"
    print(s)
    return t
    
            

def sol_dyna(s):
    n = len(s)
    t = [ [None for i in range(len(s))] for j  in range(len(s))]
    for k in range(n):
        t[k][k] = k, k
    for k in range(0, n - 1):
        if s[k] == s[k + 1]:
            t[k][k + 1] = k, k + 1
        else:
            t[k][k + 1] = k + 1, k + 1
    for j in range(2, n + 1):
        for k in range(n - j):
            u, v = k, j + k 
            a = t[u][v - 1]
            b = t[u + 1][v - 1]
            c = t[u + 1][v]
            # print(u, v)
            # print(a, b, c)
            if s[u] == s[v] and (b[0] == u + 1 and b[1] == v - 1):
                t[u][v] = u, v
            else:
                # if a[2] and s[u] == s[u + 1]:
                #     a = a[0], u, a[2]
                # if c[2] and s[v - 1] == s[v]:
                #     c = v, c[1], c[2]
                # print(u, v, a, c)
                if a[1] - a[0] > c[1] - c[0]:
                    t[u][v] = a
                else:
                    t[u][v] = c
            # formata(t)
    begin, end = t[0][n - 1]
    return s[begin:end + 1]
                
# def longuest_palindrome(s):
#     i, l = sol_dyna(s, 0, len(s))
#     return s[i:i + l]
            
# s = "abccbade"
# s = "bdk"
# s = "bb"
# s = "abba"
# s = "aacabdkacaa"
# s = "abbcccbbbcaaccbababcbcabca"
# s = "lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc"

# print(s, sol_rec(s, 0, len(s)), longuest_palindrome(s))
s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"

# s = "cbbd"
# s = "cbabd"
print(sol_dyna(s) == s)

# Or 
# https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
