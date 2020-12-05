import time
import lib
import math
import re
import itertools
import functools
from operator import xor


def read_input():
    # read all nodes, create each without processing childs:
    # input = "".join(lib.readfile('inputs/09-input-sample4.txt'))
    return lib.readfile('inputs/10-input.txt')[0]
    # return list(map(int, lib.readfile('inputs/10-input-sample.txt', ',')[0]))

def reverse(knot_list, pos, length):
    turn_list = []
    knot_list = list(knot_list)
    for i in range(pos, pos+length):
        turn_list.append(knot_list[i%len(knot_list)])
    turn_list = list(reversed(turn_list))
    for i in range(0, length):
        idx = (pos + i) % len(knot_list)
        knot_list[idx] = turn_list[i]
    return knot_list




def problem1(input):
    lengths = list(map(int, input.split(',')))
    knot_list = range(0, 256)
    skip_size = 0
    pos = 0

    for l in lengths:
        knot_list = reverse(knot_list, pos, l )
        pos = (pos + l + skip_size) % len(knot_list)
        skip_size += 1

    solution = knot_list[0] * knot_list[1]
    print("Solution 1: Solution: {}".format(solution))


def problem2(input):
    # 1: transform input: create an ascii code list of all chars:
    lengths = list(itertools.chain([ord(x) for x in input],[17, 31, 73, 47, 23]))

    # 2: hash rounds: 64
    knot_list = range(0, 256)
    skip_size = 0
    pos = 0

    for i in range(0, 64):
        for l in lengths:
            knot_list = reverse(knot_list, pos, l )
            pos = (pos + l + skip_size) % len(knot_list)
            skip_size += 1

    # 3: chunk it to 16x16 chunks and xor
    chunks = []
    for i in range(0,256,16):
        chunks.append(functools.reduce(xor,knot_list[i:i+16]))

    # form hex hash:
    solution = ''.join('{:02x}'.format(n) for n in chunks)
    
    print("Solution 2: Solution: {}".format(solution))


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
