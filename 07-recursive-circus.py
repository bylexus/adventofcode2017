import time
import lib
import functools
import math
import re

nodes = dict()


class Node:
    weight = 0
    name = None
    childs = []
    parent = None

    def child_weights(self):
        s = 0
        for child in self.childs:
            child_node = nodes[child]
            s = s + child_node.full_weight()
        return s

    def full_weight(self):
        return self.weight + self.child_weights()

    def check_balance(self):
        weights = [nodes[c].full_weight() for c in self.childs]
        unique = len(set(weights))
        if unique > 1:
            return False
        else:
            return True

    def print(self, indent=0):
        print("{}{} ({}):".format(" "*indent, self.name, self.weight))
        for child in self.childs:
            child_node = nodes[child]
            child_node.print(indent + 4)


def link_childs_to_parent(node):
    if len(node.childs) > 0:
        for child in node.childs:
            child_node = nodes[child]
            child_node.parent = node
            link_childs_to_parent(child_node)


def read_input():
    m = re.compile("(\w+)\s+\((\d+)\)(\s*->\s*(.*))?")
    # read all nodes, create each without processing childs:
    # for line in lib.readfile('inputs/07-input-sample.txt'):
    for line in lib.readfile('inputs/07-input.txt'):
        g = m.match(line)
        if g:
            node = Node()
            node.weight = int(g.group(2))
            node.name = g.group(1)
            if g.group(4):
                node.childs = [s.strip() for s in g.group(4).split(',')]
            nodes[node.name] = node

    # now link all childs of the nodes recursively back to
    # their parent node:
    for node in nodes.values():
        if node.parent is None:
            link_childs_to_parent(node)


def problem1():
    # find (sole) node without parent:
    start_node = list(
        filter(lambda node: node.parent is None, nodes.values()))[0]
    # start_node.print(0)

    solution = start_node.name
    print("Solution 1: Solution: {}".format(solution))


def problem2():
    solution = 0
    # find node with unbalanced child weights
    # nodes['yruivis'].weight = 2751
    unbalanced = []
    for node in nodes.values():
        if not node.check_balance():
            unbalanced.append(node)
            # print("Unbalanced node: {}, weight: {} ({})".format(node.name, node.weight, len(node.childs)))

    # now of those unbalanced nodes, search the one which childs are all balanced - that must be the one, then:
    wrong_node = None
    for node in unbalanced:
        balanced = True
        for child in node.childs:
            child_node = nodes[child]
            if not child_node.check_balance():
                balanced = False
        if balanced:
            wrong_node = child_node
            break

    print("Wrong node: {}".format(wrong_node.name))

    # find another sibling, which has the correct weight:
    correct_node = None
    for child in wrong_node.parent.childs:
        if child != wrong_node.name:
            correct_node = nodes[child]
            break
    
    # OK, so now calculate the correct weight for the wrong node:
    solution = correct_node.full_weight() - wrong_node.child_weights()

    print("Solution 2: Correct weight for wrong node: {}".format(solution))


def main():
    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    read_input()

    t1 = lib.measure(problem1)
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2 = lib.measure(problem2)
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
