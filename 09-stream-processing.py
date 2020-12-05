import time
import lib
import math
import re
from functools import reduce

result = None


class Group:
    def __init__(self):
        self.childs = []
        self.parent = None

    def print(self, score=1):
        print("{}Group Score: {}".format(" "*score*4, score))
        for child in self.childs:
            child.print(score + 1)

    def sum(self, score=1):
        return score + reduce(lambda a, b: a + b.sum(score+1),
                              filter(lambda c: isinstance(c, Group), self.childs), 0)

    def count_garbage(self):
        sum = 0
        for child in self.childs:
            if isinstance(child, Garbage):
                sum += len(child.content)
            else:
                sum += child.count_garbage()
        return sum


class Garbage:
    def __init__(self):
        self.content=""
        self.parent=None

    def print(self, score=1):
        print("{}Garbage: {}".format(" "*score*4, self.content))


def tokenize_input(input):
    state=None
    g=None
    garbage=None

    # parse state machine:
    i=0
    while i < len(input):
        c=input[i]
        # skip next if ! occurs:
        if c == '!':
            i += 2
            continue
        # skip commas, not relevant:
        if state == None:
            if c != '{':
                raise Exception(
                    'State None: must begin with {{, got {}'.format(c))
            new_g=Group()
            if g:
                g.childs.append(new_g)
            new_g.parent=g
            g=new_g
            state='in_group'
        elif state == 'in_group':
            if c == '}':  # group end
                if not g:
                    state=None
                elif g.parent == None:
                    # we are at the outermost group, end here:
                    return g
                else:
                    g=g.parent
            elif c == '{':
                new_g=Group()
                new_g.parent=g
                if g:
                    g.childs.append(new_g)
                g=new_g
            elif c == '<':  # garbage start
                garbage=Garbage()
                garbage.parent=g
                g.childs.append(garbage)
                state='in_garbage'
        elif state == 'in_garbage':
            if c != '>':  # garbage end
                garbage.content += c
            else:
                state='in_group'
        i += 1
    return g


def read_input():
    # read all nodes, create each without processing childs:
    # input = "".join(lib.readfile('inputs/09-input-sample4.txt'))
    input="".join(lib.readfile('inputs/09-input.txt'))
    return input


def problem1():
    solution=result.sum()
    print("Solution 1: Solution: {}".format(solution))


def problem2():
    solution=result.count_garbage()
    print("Solution 2: Solution: {}".format(solution))


def main():
    global result

    title="Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    result=tokenize_input(read_input())

    t1=lib.measure(problem1)
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2=lib.measure(problem2)
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
