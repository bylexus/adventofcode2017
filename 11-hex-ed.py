import time
import lib
import math
import re


def read_input():
    input = lib.readfile('inputs/11-input.txt')[0].split(',')
    return input

def calc_dist(coord):
    (col, row) = coord
    col = abs(col)
    row = abs(row)
    if (col > row // 2):
        return row // 2 + (col-row//2)
    else:
        return col + (row - col) // 2



def problem1(input):
    # see:
    # https://www.redblobgames.com/grids/hexagons/#coordinates-doubled
    # I use the doubled coordinate system, easier to calculate
    # (0,0) is (col, row)
    act_coord = (0, 0)

    max_dist = 0
    for dir in input:
        # print(act_coord)
        if dir == 'n':
            act_coord = (act_coord[0], act_coord[1] - 2)
        elif dir == 's':
            act_coord = (act_coord[0], act_coord[1] + 2)
        elif dir == 'nw':
            act_coord = (act_coord[0] - 1, act_coord[1] - 1)
        elif dir == 'ne':
            act_coord = (act_coord[0] + 1, act_coord[1] - 1)
        elif dir == 'sw':
            act_coord = (act_coord[0] - 1, act_coord[1] + 1)
        elif dir == 'se':
            act_coord = (act_coord[0] + 1, act_coord[1] + 1)
        dist = calc_dist(act_coord)
        max_dist = max(max_dist,dist)

    # print(act_coord)

    solution = calc_dist(act_coord)
    print("Solution 1: Solution: {}".format(solution))
    print("Solution 2: Solution: {}".format(max_dist))



def main():

    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    input = read_input()

    t1 = lib.measure(lambda: problem1(input))
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))


if __name__ == "__main__":
    main()
