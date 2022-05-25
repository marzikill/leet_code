class NFA:
    def __init__(self, initial: int, adj: dict, finals: set[int]):
        self.initial = initial
        self.currents = {initial}
        self.adj = adj
        self.adj[-1] = {'.': {-1}}
        self.finals = finals
        self.unite_eps()

    def get_dest(self, state, c):
        """ Renvoie la liste des destinations atteignables
        à partir de l'état state en suivant la transition c. """
        if not self.adj[state].get(c):
            return {}
        if self.adj[state].get('any'):
            return self.adj[state]['any'].copy()
        return self.adj[state][c].copy()

    def eps_closure(self, state):
        """ Renvoie la liste des états atteignables à partir 
        de state en ne suivant que des epsilons transitions """
        closure = {state}
        to_visit = self.get_dest(state, '.')
        while to_visit:
            s = to_visit.pop()
            closure.add(s)
            for sp in self.get_dest(s, '.'):
                if sp not in closure:
                    to_visit.add(sp)
        return closure

    def unite_eps(self):
        """ Ajoute aux états courants tous les états atteignables
        via des epsilons transitions """
        new = set()
        for state in self.currents:
            new = new.union(self.eps_closure(state))
        self.currents = new

    def feed(self, c):
        """ Met à jour les états possibles de l'automate, lors de
        la lecture du caractère c"""
        print(self.currents)
        new = set()
        for possible_state in self.currents:
            if possible_state == -1 or not self.get_dest(possible_state, c):
                new.add(-1)
                continue
            new = new.union(self.get_dest(possible_state, c))
        self.unite_eps()
        self.currents = new

    def is_final(self):
        """ Détermine si l'automate est dans un état final """
        return any(state in self.finals for state in self.currents)

    def validate(self, chaine):
        """ Détermine si l'automate accepte la chaine. """
        for c in chaine:
            self.feed(c)
        return self.is_final()


A = NFA(1,
        {1: {'b': {1}, 'a': {2}, '.': {}},
            2: {'a': {2}, 'b': {3}, '.': {}},
            3: {'a': {2}, 'b': {4}, '.': {}},
            4: {'a': {4}, 'b': {4}, '.': {}}},
        {4})
chaine = 'aaabbbaabbaabba'

B = NFA(1,
        {1: {'0': {1}, '1': {1, 2}, '.': {}},
            2: {}, '.': {}},
        {2})
chaine = '00000011'

C = NFA(1,
        {1: {'.': {5, 2}},
            2: {'a': {3}, },
            3: {'c': {4}},
            4: {},
            5: {'.': {6, 7}},
            6: {'a': {8}, '.': {5}},
            7: {'b': {8}},
            8: {'.': {1}}
         },
        {4})

D = NFA(1,
        {1: {'a': {2}},
         2: {'.': {2}, 'z': {3}},
         3: {}},
        {3})
