import time
import lib
import math
import re
import itertools
import functools
from operator import xor
from lib import reverse_part, knot_hash

def read_input():
    lines = lib.readfile('inputs/15-input.txt')
    return [int(re.sub(r'[^0-9]','',lines[0])), int(re.sub(r'[^0-9]','',lines[1]))]
    # return [65, 8921] # test start value


def next_val(act_val, factor):
    # 2^31 - 1 = 2147483647 --> I guess the modulo can be implemented in a much more performant way...
    # 2147483647 is a mersenne prime - 2^31 -1
    # there is a fast way to do modulus with mersenne primes:
    # int i = k % p ==> 
    # int i = (k & p) + (k >> s); return (i >= p) ? i - p : i;
    # where s is the power, in this case, 31.

    return (act_val * factor) % 2147483647

    # mult = act_val * factor
    # i = (mult & 2147483647) + (mult >> 31)
    # return i



def problem1(input):
    counter = 0
    mask = 65535
    rounds = 40000000
    act_a = input[0]
    act_b = input[1]
    matches = 0

    for i in range(0,rounds):
        counter += 1
        if counter % 1000000 == 0:
            print("Round: {}".format(counter))
        act_a = next_val(act_a, 16807)
        act_b = next_val(act_b, 48271)
        # print("{} {}".format(act_a, act_b))
        if (act_a & mask == act_b &mask):
            matches += 1
            # print("MATCH: {}".format(counter))
        

    solution = matches
    print("Solution 1: {}".format(solution))


def problem2(input):
    counter = 0
    mask = 65535
    # rounds = 1056
    rounds = 5000000
    act_a = input[0]
    act_b = input[1]
    results_a = []
    results_b = []

    while min(len(results_a), len(results_b)) < rounds:
        counter += 1
        if counter % 1000000 == 0:
            print("Round: {}".format(counter))
        act_a = next_val(act_a, 16807)
        act_b = next_val(act_b, 48271)
        if act_a % 4 == 0:
            results_a.append(act_a)
        if act_b % 8 == 0:
            results_b.append(act_b)
        
        # print("{} {}".format(act_a, act_b))
        # if (act_a & mask == act_b &mask):
        #     matches += 1
            # print("MATCH: {}".format(counter))

    matches = 0
    for i in range(0, min(len(results_a), len(results_b))):
        if ((results_a[i] & mask) == (results_b[i] & mask)):
            matches += 1

        
    # print(results_a[-3:])
    # print(results_b[-3:])

    solution = matches
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
