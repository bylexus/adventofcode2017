import time
import lib
import functools
import math

number = 325489
# number = 25
array_length = math.ceil(math.sqrt(number))
if array_length % 2 == 0:
    array_length = array_length + 1


def manhattan_dist(p1, p2):
    """
    Calcs the manhattan distance of point 1 (tupel(x,y)) and point 2
    """
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def print_mem(memory):
    for line in memory:
        for col in line:
            print("{:5d}".format(col), end='')
        print('')


def problem1():
    memory = [[-1 for i in range(0, array_length)]
              for j in range(0, array_length)]
    x = array_length // 2
    y = x
    start_x = x
    start_y = y
    act = 1
    dir = 'r'
    memory[y][x] = act

    if number < 1000:
        print_mem(memory)

    while act < number:
        memory[y][x] = act

        # move one further:
        if dir == 'r':
            x = x + 1
        elif dir == 'l':
            x = x - 1
        elif dir == 'u':
            y = y - 1
        elif dir == 'd':
            y = y + 1

        # calc new dir:
        if dir == 'r' and memory[y-1][x] == -1:
            dir = 'u'
        elif dir == 'u' and memory[y][x-1] == -1:
            dir = 'l'
        elif dir == 'l' and memory[y+1][x] == -1:
            dir = 'd'
        elif dir == 'd' and memory[y][x+1] == -1:
            dir = 'r'

        act = act + 1

        if number < 1000:
            print_mem(memory)
            print()
    print("End x: {}, y: {}, Manhattan Dist: {}".format(
        x, y, manhattan_dist((x, y), (start_x, start_y))))

    # print("Start x:{}|y:{}",x,y)
    # print("Solution 1: The value is {}".format(0))


def problem2():
    memory2 = [[-1 for i in range(0, array_length)]
               for j in range(0, array_length)]
    x = array_length // 2
    y = x
    start_x = x
    start_y = y
    act = 1
    dir = 'r'
    memory2[y][x] = act

    if number < 1000:
        print_mem(memory2)

    while act < number:
        # calc memory 2, which is the sum of all surrounding entries:
        sum = 0
        # up:
        if y > 0 and memory2[y-1][x] >= 0:
            sum = sum + memory2[y-1][x]
        # right:
        if x < array_length-1 and memory2[y][x+1] >= 0:
            sum = sum + memory2[y][x+1]
        # down:
        if y < array_length-1 and memory2[y+1][x] >= 0:
            sum = sum + memory2[y+1][x]
        # left:
        if x > 0 and memory2[y][x-1] >= 0:
            sum = sum + memory2[y][x-1]
        # up-left:
        if y > 0 and x > 0 and memory2[y-1][x-1] >= 0:
            sum = sum + memory2[y-1][x-1]
        # up-right:
        if y > 0 and x < array_length - 1 and memory2[y-1][x+1] >= 0:
            sum = sum + memory2[y-1][x+1]
        # down-left:
        if y < array_length-1 and x > 0 and memory2[y+1][x-1] >= 0:
            sum = sum + memory2[y+1][x-1]
        # down-right:
        if y < array_length-1 and x < array_length - 1 and memory2[y+1][x+1] >= 0:
            sum = sum + memory2[y+1][x+1]
        memory2[y][x] = sum if sum > 0 else 1
        if sum > number:
            print("Solution 2: End x: {}, y: {}, Manhattan Dist: {}, value: {}".format(
                x, y, manhattan_dist((x, y), (start_x, start_y)), sum))
            return

        # move one further:
        if dir == 'r':
            x = x + 1
        elif dir == 'l':
            x = x - 1
        elif dir == 'u':
            y = y - 1
        elif dir == 'd':
            y = y + 1

        # calc new dir:
        if dir == 'r' and memory2[y-1][x] == -1:
            dir = 'u'
        elif dir == 'u' and memory2[y][x-1] == -1:
            dir = 'l'
        elif dir == 'l' and memory2[y+1][x] == -1:
            dir = 'd'
        elif dir == 'd' and memory2[y][x+1] == -1:
            dir = 'r'

        act = act + 1

        if number < 1000:
            print_mem(memory2)
            print()
    print("End x: {}, y: {}, Manhattan Dist: {}".format(
        x, y, manhattan_dist((x, y), (start_x, start_y))))


def main():
    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    t1 = lib.measure(problem1)
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2 = lib.measure(problem2)
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
