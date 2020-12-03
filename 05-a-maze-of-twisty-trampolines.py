import time
import lib
import functools
import math

def read_input():
    # return [int(n) for n in lib.readfile('inputs/05-input-sample.txt')]
    return [int(n) for n in lib.readfile('inputs/05-input.txt')]


def calc_mod1(memval):
    return memval + 1

def calc_mod2(memval):
    if memval >= 3:
        return memval - 1
    else:
        return memval + 1

def runProgram(memory, ip = 0, calc_fn = calc_mod1):
    """
    Runs the program until ip points to outside the memory
    Running means:
    - jump relative: the nr at the actual memory position is a relative offset
    - increase actual (before jump) value with 1

    returns the number of steps needed until it reaches outside memory
    """
    steps = 0
    while ip >= 0 and ip < len(memory):
        jmp = memory[ip]
        memory[ip] = calc_fn(memory[ip])
        ip = ip + jmp
        steps = steps + 1
    return steps




def problem1():
    lines = read_input()
    steps = runProgram(lines, 0)
    print("Solution 1: Took {} steps to end the program".format(steps))


def problem2():
    lines = read_input()
    steps = runProgram(lines, ip = 0, calc_fn = calc_mod2)
    print("Solution 2: Took {} steps to end the program".format(steps))


def main():
    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    t1 = lib.measure(problem1)
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2 = lib.measure(problem2)
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
