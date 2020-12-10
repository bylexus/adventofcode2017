import time
import lib
import math
import re
import itertools
import functools
from operator import xor
from lib import reverse_part, knot_hash

def read_input():
    ops = lib.readfile('inputs/16-input.txt')[0].split(',')
    return ops

    # return ['s1', 'x3/4', 'pe/b']
    # return [65, 8921] # test start value

def exec_spin(progs, i, act_0):
    act_0 = (act_0 - i) % len(progs)
    return act_0

def exec_exchange(progs, a, b, act_0):
    a = (a + act_0) % len(progs)
    b = (b + act_0) % len(progs)
    tmp = progs[a]
    progs[a] = progs[b]
    progs[b] = tmp

def exec_partner(progs, name_a, name_b):
    i_a = progs.index(name_a.lower())
    i_b = progs.index(name_b.lower())
    tmp = progs[i_a]
    progs[i_a] = progs[i_b]
    progs[i_b] = tmp


def exec_op(progs, op, act_0):
    if op[0] == 's':
        i = int(op[1:])
        return exec_spin(progs, i, act_0)
    if op[0] == 'x':
        [a,b] = op[1:].split('/')
        exec_exchange(progs, int(a), int(b), act_0)
    if op[0] == 'p':
        [a,b] = op[1:].split('/')
        exec_partner(progs, a, b)

    return act_0

def problem1(input):
    nr_p = 16
    act_0 = 0
    p = list(map(chr, range(97, 97 + nr_p)))
    for op in input:
        act_0 = exec_op(p, op, act_0)
    
    rot = p[act_0:] + p[:act_0]
    solution = "".join(rot)

    print("Solution 1: {}".format(solution))


def problem2(input):
    nr_p = 16
    # instead of spinning (exec_spin), we just move
    # the 0-index-pointer (and calculate relative indexes for all operations instead)
    act_0 = 0

    # create a list of chars, a-p:
    p = list(map(chr, range(97, 97 + nr_p)))
    start = list(p)
    loops = 1000000000
    rest = 0

    # Step 1: find after how many loops we have the same pattern than at the start:
    for i in range(0, loops):
        for op in input:
            act_0 = exec_op(p, op, act_0)
        # same result thatn at the beginning? great! we can stop here:
        if p == start:
            loop = i + 1
            # We only need to do as many loops:
            rest = loops % loop
            break

    # now do the few loops:
    p = list(start)
    for i in range(0, rest):
        for op in input:
            act_0 = exec_op(p, op, act_0)
    
    # and finally put the result together in the correct order:
    rot = p[act_0:] + p[:act_0]
    solution = "".join(rot)

    print("Solution 2: {}".format(solution))

def main():

    title="Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    input = read_input()

    t1=lib.measure(lambda: problem1(input))
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2=lib.measure(lambda: problem2(input))
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
