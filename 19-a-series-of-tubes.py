import time
import lib
import math
import re
import itertools


def read_input():
    # return list(map(list, lib.readfile('inputs/19-input-sample.txt', strip=False)))
    return list(map(list, lib.readfile('inputs/19-input.txt', strip=False)))


def check_path(pipes, pos, direction):
    next_pos = [pos[0] + direction[0], pos[1] + direction[1]]
    if next_pos[0] < 0 or next_pos[0] >= len(pipes):
        return False
    if next_pos[1] < 0 or next_pos[1] >= len(pipes[next_pos[0]]):
        return False
    next_char = pipes[next_pos[0]][next_pos[1]]
    return re.match(r'[a-zA-Z\-\|\+]',next_char)


def walk(pipes, direction, key_queue, pos):
    # collect char, if any:
    act_char = pipes[pos[0]][pos[1]]
    if re.match(r'[a-zA-Z]', act_char):
        key_queue.append(act_char)

    # find next dir to go, start with the current dir, then rotate:
    check_dirs = [
        direction, # current dir
        [-direction[1], direction[0]], # rotate left
        [direction[1], -direction[0]], # rotate right
    ]
    for d in check_dirs:
        if (check_path(pipes, pos, d)):
            pos[0] += d[0]
            pos[1] += d[1]
            return d
    # cannot go anywhere, I must be at the end
    return False


def print_map(pipes):
    print("".join(map(lambda s:"".join(s), pipes)))

def problem1(input):
    # print_map(input)
    key_queue = []
    pos = [0, input[0].index('|')] # Start pos, (y, x)
    direction = [1,0] # direction vector

    steps = 0
    while direction:
        direction = walk(input, direction, key_queue, pos)
        steps += 1

    solution = "".join(key_queue)
    print("Solution 1: {}".format(solution))
    print("Solution 2: {}".format(steps))


def problem2(input):

    solution = 0
    print("Solution 2: {}".format(solution))

def main():

    title="Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    input = read_input()

    t1=lib.measure(lambda: problem1(input))
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    # t2=lib.measure(lambda: problem2(input))
    # print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
