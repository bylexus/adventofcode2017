import time
import lib
import math
import re
import itertools
import functools
from operator import xor
from lib import reverse_part, knot_hash

output1 = None

def read_input():
    # return lib.readfile('inputs/10-input.txt')[0]
    # return list(map(int, lib.readfile('inputs/10-input-sample.txt', ',')[0]))
    # return 'flqrgnkx' # test key
    return 'jzgqcdpd' # puzzle input key


def mark_region(disk_bits, x, y, mark):
    """
    Walk the region from the given start coordinate:
    do a depth-first (recursive) "walk" in all 4 directions of the
    current location. Mark all the fields that belong to this
    region with the given "marker".
    """
    disk_bits[y][x] = mark
    # up:
    if y > 0 and disk_bits[y-1][x] == '1':
        mark_region(disk_bits, x, y-1, mark)
    # left:
    if x > 0 and disk_bits[y][x-1] == '1':
        mark_region(disk_bits, x-1, y, mark)
    # down:
    if y+1 < len(disk_bits) and disk_bits[y+1][x] == '1':
        mark_region(disk_bits, x, y+1, mark)
    # right:
    if x+1 < len(disk_bits[y]) and disk_bits[y][x+1] == '1':
        mark_region(disk_bits, x+1, y, mark)
    return disk_bits


def problem1(input):
    global output1

    lines = []
    sum_bits = 0
    for i in range(0,128):
        key = "{}-{}".format(input, str(i))
        line_hash = knot_hash(key)
        hash_nr = int(line_hash,16)
        bits = list("{:0128b}".format(hash_nr))
        lines.append(bits)
        sum_bits += bits.count('1')

    solution = sum_bits
    output1 = lines
    print("Solution 1: {}".format(solution))


def problem2(disk_bits):
    act_region = 1
    for y in range(0,len(disk_bits)):
        for x in range(0, len(disk_bits[y])):
            if (disk_bits[y][x] == '1'):
                mark_region(disk_bits, x, y, act_region)
                act_region += 1

    solution = act_region - 1
    print("Solution 2: {}".format(solution))

def main():

    title="Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    input = read_input()

    t1=lib.measure(lambda: problem1(input))
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2=lib.measure(lambda: problem2(output1))
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
