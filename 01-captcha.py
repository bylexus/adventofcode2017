import time
import lib
import functools
import math

digits = lib.readfile('inputs/01-input.txt')[0]
count = len(digits)


def problem1():
    sum = 0
    for i in range(0, count):
        if digits[(i+1) % count] == digits[i]:
            sum += int(digits[i])

    print("Solution 1: The sum is {}".format(sum))


def problem2():
    sum = 0
    for i in range(0, count):
        if digits[(i+(count//2)) % count] == digits[i]:
            sum += int(digits[i])

    print("Solution 2: The sum is {}".format(sum))


def main():
    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    t1 = lib.measure(problem1)
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2 = lib.measure(problem2)
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
