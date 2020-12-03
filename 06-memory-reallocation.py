import time
import lib
import functools
import math

globals = {
    'loop_bank': None
}

def read_input():
    # return [int(i) for i in (lib.readfile('inputs/06-input-sample.txt', "\t")[0])]
    return [int(i) for i in (lib.readfile('inputs/06-input.txt', "\t")[0])]

def reallocate(banks):
    max_value = max(banks)
    max_i = banks.index(max_value)
    banks[max_i] = 0
    for i in range(0,max_value):
        max_i = (max_i + 1) % len(banks)
        banks[max_i] = banks[max_i] + 1
    return banks


def calc_reallocations(banks):
    steps = 0
    seen_configs = set()
    while str(banks) not in seen_configs:
        seen_configs.add(str(banks))
        banks = reallocate(banks)
        steps = steps + 1
    return (steps, banks)


def problem1():
    banks = read_input()
    (steps, banks) = calc_reallocations(banks)
    # Store loop bank for 2nd part:
    globals['loop_bank'] = banks

    print("Solution 1: Reallocations: {}".format(steps))
    print("Solution 1: This bank marks the loop: {}".format(str(banks)))

def problem2():
    banks = globals['loop_bank']
    (steps, banks) = calc_reallocations(banks)

    print("Solution 2: Reallocations: {}".format(steps))
    return banks


def main():
    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    t1 = lib.measure(problem1)
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2 = lib.measure(problem2)
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
