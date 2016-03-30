__author__ = 'braydenrw'


class Node:
    def __init__(self):
        self.start = False
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None
        self.E = None
        self.E2 = None
        self.E_star = None
        self.final = False
        self.q = -1

    def create(self, obj, c):
        self.start = True
        if c == 'a':
            self.a = obj
        elif c == 'b':
            self.b = obj
        elif c == 'c':
            self.c = obj
        elif c == 'd':
            self.d = obj
        elif c == 'e':
            self.e = obj
        elif c == 'E':
            self.E2 = obj
        obj.final = True

    def is_final(self):
        return self.final
