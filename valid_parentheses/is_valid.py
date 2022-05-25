# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


def is_valid(s):
    pairs = [['(', ')'], ['[', ']'], ['{', '}']]
    stack = []
    for e in s:
        ouvrant, fermant = next(filter(lambda pair: e in pair, pairs))
        if e == ouvrant:
            stack.append(e)
        elif e == fermant:
            if len(stack) == 0:
                return False
            if stack.pop() != ouvrant:
                return False
    return len(stack) == 0


# Trouver la paire
pairs = [['(', ')'], ['[', ']'], ['{', '}']]
s = '()[]{}'
for e in s:
    ouvrant, fermant = next(filter(lambda pair: e in pair, pairs))
    print(ouvrant, fermant)
