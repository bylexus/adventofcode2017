#####
# This one needed a bit of thinking. The "brute force" method 
# (really simulate the scanner's moves step-by-step) does not work, at least
# not for problem 2 (just too many loops).
#
# So I figured out that the actual "hit" interval for each scanner
# can be calculated: It's a regular interval the scanner hits the top
# row, and the rougue package moves also regularly: so it can
# be calculated WHEN a scanner hits the top, and WHERE the
# package is then (for each scanner).
#
# this works well for problem 1.
#
# Problem 2 now needs the same algorigthm, but retries a full run with an
# incrementing packet delay in each round, until a full run is calculated
# where the packet is not hit anymore.
#
# This works very well, there is no need to actually simulate the
# scanners, and it finishes in about 1.8 seconds.

import time
import lib
import math
import re


def read_input():
    global prgs

    # input = lib.readfile('inputs/13-input-sample.txt')
    input = lib.readfile('inputs/13-input.txt')
    m = re.compile(r"^(\d+):\s+(\d+)")
    lines = []

    for line in input:
        g = m.match(line)
        if g:
            # tuples of: ( depth, range )
            lines.append((int(g.group(1)), int(g.group(2))))

    return lines


def problem1(inputs):
    # Solution 1 can be calculated without really move all the items:
    # The packet is hit when depth % ((range-1)*2) == 0.
    severity = 0
    for (depth, range) in inputs:
        print("{}: {}".format(depth, range))
        severity += (depth * range) if (depth % ((range-1)*2) == 0) else 0

    solution = severity
    print("Solution 1: {}".format(solution))


def problem2(inputs):
    # the 2nd problem just need to run the loop from problem 1... a lot of times :-)
    # for each new run, we add a delay to the packet, and calculate it again,
    # but with the delay added: 
    delay = 0
    while True:
        hit = False
        for (depth, range) in inputs:
            if (depth+delay) % ((range-1)*2) == 0:
                hit = True
                break
        if not hit:
            # yeah, found it!
            break
        delay += 1
        
    solution = abs(delay)
    print("Solution 2: {}".format(solution))


def main():

    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    input = read_input()

    t1 = lib.measure(lambda: problem1(input))
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2 = lib.measure(lambda: problem2(input))
    print("Problem 2 took {:.3f}s to solve.\n\n".format(t2))


if __name__ == "__main__":
    main()
