##
# A nice graph spanning / traversing problem, with 
# multiple, detached graphs.
#
# the algorithms below:
# - defines the graph by nodes that know their directly connected nodes
# - keeps all nodes in a key (node ident) / value (node itself)
# - marks all traversed nodes as visited to detect loops
# - can detect all single graphs and counts them

import time
import lib
import math
import re

class Prg:
    name: None
    conn_list: []

prgs = dict()


def read_input():
    global prgs

    # input = lib.readfile('inputs/12-input-sample.txt')
    input = lib.readfile('inputs/12-input.txt')
    m = re.compile(r"^(\d+)\s+<->\s+(.*)")

    for line in input:
        g = m.match(line)
        if g:
            (prg, conn_list) = g.group(1, 2)
            conn_list = [s.strip() for s in conn_list.split(',')]
            prg_obj = Prg()
            prg_obj.name = prg
            prg_obj.conn_list = conn_list
            prgs[prg] = prg_obj

    return prgs


def visit(prg, visited, found_0, group):
    global prgs

    if prg.name in visited:
        return prg.name in found_0

    visited.add(prg.name)

    if prg.name == group:
        found_0.add(prg.name)

    for child in prg.conn_list:
        child = prgs[child]
        if prg.name in found_0:
            found_0.add(child.name)
        if visit(child, visited, found_0, group):
            found_0.add(child.name)
            found_0.add(prg.name)

    return prg.name in found_0


def problem1(prgs):
    found_0 = set()
    visited = set()

    visit(prgs['0'], visited, found_0, '0')

    solution = len(found_0)

    print("Solution 1: Solution: {}".format(solution))


def problem2(prgs):
    visited = set()

    groups = 0
    for prg in prgs.values():
        if prg.name not in visited:
            found_0 = set()
            visit(prg, visited, found_0, prg.name)
            groups += 1

    solution = groups
    print("Solution 2: Solution: {}".format(solution))


def main():

    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    prgs = read_input()

    t1 = lib.measure(lambda: problem1(prgs))
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2 = lib.measure(lambda: problem2(prgs))
    print("Problem 2 took {:.3f}s to solve.\n\n".format(t2))


if __name__ == "__main__":
    main()
