def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    j = 0
    lettres = {}
    current_win = 0
    max_win = current_win
    while j < len(s) - 1:
        j += 1
        print(lettres)
        if not s[j] in lettres:
            lettres[s[j]] = i
            current_win += 1
            max_win = max(max_win, current_win)
        else:
            k = lettres[s[j]]
            lettres = { caractère:indice for caractère, indice in lettres.items() if indice > k }
            i = k + 1
            current_win = j - i
            max_win = max(max_win, current_win)
    return max_win

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
