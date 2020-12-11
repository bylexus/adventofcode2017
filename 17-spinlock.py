import time
import lib
import math
import re
import itertools
from lib import reverse_part, knot_hash
from collections import deque

def read_input():
    # return 3 # test input
    return 370 # puzzle input


def problem1(input):
    steps = input
    buffer = deque([0])
    rounds = 2017

    for i in range(1, rounds+1):
        buffer.rotate(-steps)
        buffer.append(i)

    solution = buffer[(buffer.index(2017)+1)%len(buffer)]
    print("Solution 1: {}".format(solution))


def problem2(input):
    steps = input
    buffer = deque([0])
    rounds = 50000000

    for i in range(1, rounds+1):
        buffer.rotate(-steps)
        buffer.append(i)

    solution = buffer[(buffer.index(0)+1) % len(buffer)]
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
