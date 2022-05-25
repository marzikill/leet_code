class Reader:
    def __init__(self, s):
        self.chaine = s
        self.pos = 0
        self.fin = len(s)

    def get_pos(self):
        return self.pos

    def set_pos(self, p):
        self.pos = p

    def is_exhausted(self):
        return self.pos >= self.fin

    def is_star(self):
        try:
            return self.chaine[self.pos + 1] == "*"
        except IndexError:
            return False

    def is_any(self):
        if not self.is_exhausted():
            return self.chaine[self.pos] == "."
        return False

    def read(self):
        if self.is_exhausted():
            return ""
        return self.chaine[self.pos]

    def next(self):
        c = self.read()
        if self.is_star():
            self.pos += 2
        else:
            self.pos += 1
        return c

class Validator:
    def __init__(self, s, p):
        self.chaine = Reader(s)
        self.re = Reader(p)

    def check(self):
        m = self.re.read()
        c = self.chaine.read()
        return  (m == c) if not self.re.is_any() else c != ''
        return b

    def match(self,):
        if self.chaine.is_exhausted() and self.re.is_exhausted():
            return True
        elif self.re.is_exhausted():
            return False
        else:
            if not self.re.is_star():
                if self.check():
                    self.chaine.next()
                    self.re.next()
                    return self.match()
                else:
                    return False
            else:
                # Méthode 2 : on peut chercher à sauter le plus possible
                pos_c = self.chaine.get_pos()
                pos_r = self.re.get_pos()
                self.re.next()
                if self.match():
                    return True
                self.chaine.set_pos(pos_c)
                self.re.set_pos(pos_r)
                if self.check():
                    self.chaine.next()
                    return self.match()
                else:
                    return False
                # Méthode 1 : on peut essayer de valider le plus possible
                # pos_c = self.chaine.get_pos()
                # pos_r = self.re.get_pos()
                # if self.check():
                #     self.chaine.next()
                #     b = self.match()
                #     if b:
                #         return b
                # self.chaine.set_pos(pos_c)
                # self.re.set_pos(pos_r)
                # self.re.next()
                # return self.match()

# s = "aaaaabaabaaaaa"
# s = "aaaaabaabaacaaa"
# p = "a*ba*ba*ca*"
# s = "a"
# p = "a*ca*"
# s = ""
# p = "a*ca*"
s = "ab"
s = "ba"
p = ".*"
s = "bacaaabccbbccba"
p = ".*..*c*a*.*b.b*c"
s = "bacaaabccbbcc"
p = ".*..*c*a*.*b.b*c"
S = Reader(s)
P = Reader(p)
V = Validator(s, p)
print(V.match())
# print(re_match(s, p, 2, 4))
            
            
        

    
