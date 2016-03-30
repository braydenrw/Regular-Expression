from Stack import *
from Node import *
__author__ = 'braydenrw'


class Regex:
    def __init__(self):
        self.stack = Stack()
        self.nfa_final = Node()
        self.q_node = 0
        self.array = []

    def regex(self, string):  # converts a regular expression to an nfa
        for char in string:  # traverses each character in the reg exp
            if char == '&':  # if the concatenate operation is used
                assert self.stack.__len__() >= 2
                nfa2 = self.stack.pop()
                nfa1 = self.stack.pop()
                self.stack.push(self.concatenate(nfa1, nfa2))
            elif char == '+':  # if the union operation is used
                assert self.stack.__len__() >= 2
                nfa1 = self.stack.pop()
                nfa2 = self.stack.pop()
                self.stack.push(self.union(nfa1, nfa2))
            elif char == '*':  # if kleene star is used
                assert self.stack.__len__() >= 1
                nfa = self.stack.pop()
                self.stack.push(self.star(nfa))
            else:  # there is no operation, so push the newest character as an nfa
                final = Node()
                temp = Node()
                temp.q = self.q_node
                self.q_node += 1
                final.q = self.q_node
                self.q_node += 1
                temp.create(final, char)
                self.stack.push(temp)

        self.nfa_final = self.stack.pop()

    def concatenate(self, nfa1, nfa2):  # concatenate function epsilon jumps from nfa1 to nfa2
        temp1 = self.traverse_final(nfa1)  # temp1 is the old final state of nfa1
        temp1.final = False
        nfa2.start = False
        temp1.E2 = nfa2

        return nfa1

    def union(self, nfa1, nfa2):  # union function
        start_node = Node()  # new start state
        start_node.q = self.q_node
        self.q_node += 1
        start_node.start = True
        final_node = Node()  # new final state
        final_node.q = self.q_node
        self.q_node += 1
        final_node.final = True

        temp1 = self.traverse_final(nfa1)  # old final state of nfa1
        temp2 = self.traverse_final(nfa2)  # old final state of nfa2

        temp1.final = False
        temp1.E2 = final_node
        temp2.final = False
        temp2.E2 = final_node

        start_node.E = nfa1
        start_node.E2 = nfa2
        nfa1.start = False
        nfa2.start = False

        return start_node

    def star(self, nfa):  # kleene star function
        start_node = Node()  # new start state
        start_node.q = self.q_node
        self.q_node += 1
        start_node.start = True

        final_node = Node()  # new final state
        final_node.q = self.q_node
        self.q_node += 1
        final_node.final = True

        temp = self.traverse_final(nfa)  # old final state of nfa

        temp.final = False
        temp.E_star = nfa  # loop back to old start state
        temp.E2 = final_node

        start_node.E = nfa
        start_node.E2 = final_node
        nfa.start = False

        return start_node

    @staticmethod
    def traverse_final(nfa):  # traverses through an nfa to the final state
        temp = nfa
        while not temp.is_final():  # while nfa is not at the final state
            if temp.a is not None:
                temp = temp.a
            elif temp.b is not None:
                temp = temp.b
            elif temp.c is not None:
                temp = temp.c
            elif temp.d is not None:
                temp = temp.d
            elif temp.e is not None:
                temp = temp.e
            elif temp.E2 is not None:  # doesn't check for temp.E because that loops sometimes
                temp = temp.E2
        return temp

    def find_q(self, nfa, q):  # looks for a specific node and returns it
        temp = nfa
        if nfa.q == q:  # if we're at the right q return
            return nfa
        if temp.E is not None and temp.E2 is not None:  # append the subtrees so we don't miss a node
            self.array.append(temp.E)
            self.array.append(temp.E2)
        elif temp.a is not None:  # next node at a
            self.array.append(temp.a)
        elif temp.b is not None:  # next node at b
            self.array.append(temp.b)
        elif temp.c is not None:  # next node at c
            self.array.append(temp.c)
        elif temp.d is not None:  # next node at d
            self.array.append(temp.d)
        elif temp.e is not None:  # next node at e
            self.array.append(temp.e)
        elif temp.E2 is not None:  # next node after single epsilon
            self.array.append(temp.E2)
        assert not self.array.__len__() == 0
        entry = self.array.pop()
        return self.find_q(entry, q)

    def print_table(self):  # prints out the table
        q = 0
        print 'q__|____a|____b|____c|____d|____e|______E|'
        while True:  # loop here
            nfa = self.find_q(self.nfa_final, q)  # find the q state
            if nfa.start:  # label start state
                start = 'S'
            else:
                start = ' '
            if nfa.a is not None:  # if a progresses
                print nfa.q, start+'|  ', nfa.a.q, '|     |     |     |     |       |'
            elif nfa.b is not None:  # if b progresses
                print nfa.q, start+'|     |  ', nfa.b.q, '|     |     |     |       |'
            elif nfa.c is not None:  # if c progresses
                print nfa.q, start+'|     |     |  ', nfa.c.q, '|     |     |       |'
            elif nfa.d is not None:  # if d progresses
                print nfa.q, start+'|     |     |     |  ', nfa.d.q, '|     |       |'
            elif nfa.e is not None:  # if e progresses
                print nfa.q, start+'|     |     |     |     |  ', nfa.e.q, '|       |'
            if nfa.E is not None and nfa.E2 is not None:
                print nfa.q, start+'|     |     |     |     |     |', nfa.E.q, ',', nfa.E2.q, '|'
            elif nfa.E2 is not None and nfa.E_star is not None:
                print nfa.q, start+'|     |     |     |     |     |', nfa.E_star.q, ',', nfa.E2.q, '|'
            elif nfa.E2 is not None:
                print nfa.q, start+'|     |     |     |     |     |  ', nfa.E2.q, '  |'
            if nfa.is_final():  # print final state
                print nfa.q, 'F|     |     |     |     |     |       |'
                assert nfa.q == self.q_node - 1
                break
            q += 1
            self.array = []

    def null_case(self):
        self.nfa_final = Node()
        self.nfa_final.start = True
        self.nfa_final.q = 0
        print 'q__|____a|____b|____c|____d|____e|______E|'
        print self.nfa_final.q, 'S|     |     |     |     |     |       |'

    def read_in(self):
        filename = raw_input("Enter the filename: ")
        print "We're going to look into %r." % filename
        print "If this is NOT correct, press CTRL-C (^C)."
        raw_input("If this is correct, press RETURN")

        with open(filename) as f:
            expressions = f.readlines()

        expressions = [x.strip('\n') for x in expressions]

        for entry in expressions:
            print '\n'+entry
            if '0' in entry:
                self.null_case()
            else:
                self.regex(entry)
                self.print_table()
            self.__init__()

    def main(self):
        self.read_in()

if __name__ == '__main__':
    Regex().main()
