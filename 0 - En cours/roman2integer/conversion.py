# 13. Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X,
# L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27
# is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to
# right. However, the numeral for four is not IIII. Instead, the number
# four is written as IV. Because the one is before the five we subtract
# it making four. The same principle applies to the number nine, which
# is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.  X can be
# placed before L (50) and C (100) to make 40 and 90.  C can be
# placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

def roman2integer(chaine: str) -> int:
    """ Converti le nombre en écriture romaine chaine en un entier n """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rules = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    somme = 0
    position = 0
    while position <= len(chaine) - 1:
        if chaine[position:position + 2] in rules:
            somme += rules[chaine[position:position + 2]]
            position += 2
        else:
            somme += values[chaine[position]]
            position += 1
    return somme

# Given an integer, convert it to a roman numeral

def plus_grand_en_dessous(valeurs: dict[int, str], n: int) -> int:
    """ Détermine la plus grande clé de valeurs inférieure ou égale à n """
    maxi = -float("inf")
    for v in valeurs:
        if v > maxi and v <= n:
            maxi = v
    return maxi


def integer2roman(n: int) -> str:
    """ Converti le nombre entier n >= 0 en son écriture romaine """
    values = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
              90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    symboles = []
    while n > 0:
        max_val = plus_grand_en_dessous(values, n)
        symboles.append(values[max_val])
        n -= max_val
    return ''.join(symboles)


def intToRoman1(num: int) -> str:
    """ Converti le nombre entier n >= 0 en son écriture romaine """
    # solution alternative (leetcode)
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC",
                "L", "XL", "X", "IX", "V", "IV", "I"]
    res, i = "", 0
    while num:
        res += (num//values[i]) * numerals[i]
        num %= values[i]
        i += 1
    return res


def intToRoman(self, num: int) -> str:
    """ Converti le nombre entier n >= 0 en son écriture romaine """
    # solution alternative (leetcode)
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
         50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    res = ''
    for k in sorted(d.keys(), reverse=True):
        while num >= k:
            res += d[k]
            num -= k
    return res
