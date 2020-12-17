import time
import lib
from lib import manhattan
import math
import re
import itertools


def read_input():
    # input = list(map(list,lib.remove_empty(lib.readfile('inputs/22-input-sample.txt'))))
    input = list(map(list,lib.remove_empty(lib.readfile('inputs/22-input.txt'))))
    return input

def prt(the_map, carrier_pos):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for x,y in the_map.keys():
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    for y in range(min_y, max_y + 1):
        line = []
        for x in range(min_x, max_x + 1):
            line.append('#' if the_map.get((x,y),'.') == '#' else '.')
        print("".join(line))
    print()

def burst(the_map, carrier_pos, carrier_dir):
    infection_count = 0

    # Step 1: turn:
    if the_map.get(carrier_pos, '.') == '#':
        # turn right:
        carrier_dir = (-1*carrier_dir[1], carrier_dir[0])
    else:
        # turn left:
        carrier_dir = (carrier_dir[1], -1*carrier_dir[0])
    
    # Step 2: change infection:
    the_map[carrier_pos] = '.' if the_map.get(carrier_pos,'.') == '#' else '#'
    if the_map[carrier_pos] == '#':
        infection_count += 1
    # Step 3: move forward
    carrier_pos = (carrier_pos[0] + carrier_dir[0], carrier_pos[1] + carrier_dir[1])

    return the_map, carrier_pos, carrier_dir, infection_count

def burst2(the_map, carrier_pos, carrier_dir):
    infection_count = 0

    state = the_map.get(carrier_pos, '.')
    if state == '#':
        # turn right:
        carrier_dir = (-1*carrier_dir[1], carrier_dir[0])
        state = 'f'
    elif state == '.':
        # turn left:
        carrier_dir = (carrier_dir[1], -1*carrier_dir[0])
        state = 'w'
    elif state == 'f':
        # reverse:
        carrier_dir = (-1*carrier_dir[0], -1*carrier_dir[1])
        state = '.'
    elif state == 'w':
        state = '#'
        infection_count += 1
    the_map[carrier_pos] = state
    
    # move forward
    carrier_pos = (carrier_pos[0] + carrier_dir[0], carrier_pos[1] + carrier_dir[1])

    return the_map, carrier_pos, carrier_dir, infection_count


def problem1(input):
    the_map = dict()
    for y, line in enumerate(input):
        for x, val in enumerate(line):
            if val == '#':
                the_map[(x, y)] = '#'
    carrier_pos = (len(input[0]) // 2, len(input) // 2)
    carrier_dir = (0, -1)
    prt(the_map, carrier_pos)

    infection_count = 0
    for i in range(0,10000):
        the_map, carrier_pos, carrier_dir, icount = burst(the_map, carrier_pos, carrier_dir)
        infection_count += icount
        # prt(the_map, carrier_pos)


    solution = infection_count
    print("Solution 1: {}".format(solution))

def problem2(input):
    the_map = dict()
    for y, line in enumerate(input):
        for x, val in enumerate(line):
            if val == '#':
                the_map[(x, y)] = '#'
    carrier_pos = (len(input[0]) // 2, len(input) // 2)
    carrier_dir = (0, -1)
    prt(the_map, carrier_pos)

    infection_count = 0
    for i in range(0,10000000):
        the_map, carrier_pos, carrier_dir, icount = burst2(the_map, carrier_pos, carrier_dir)
        infection_count += icount
        # prt(the_map, carrier_pos)

    solution = infection_count
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
