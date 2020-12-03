import time
import lib
import functools
import math

numbers = lib.readfile('inputs/02-input.txt', "\t")


def problem1():
    sum = 0
    for line in numbers:
        line = [int(nr) for nr in line]
        sum += (max(line) - min(line))

    print("Solution 1: The sum is {}".format(sum))


def problem2():
    sum = 0
    for line in numbers:
        line = [int(nr) for nr in line]
        stop = False
        for first in range(0,len(line)-1):
            for second in range(first+1,len(line)):
                small = min(line[first], line[second])
                large = max(line[first], line[second])
                if small == 0 or large == 0:
                    break
                if  large % small == 0:
                    sum +=  large // small 
                    stop = True
                    break
            if stop == True:
                break

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
