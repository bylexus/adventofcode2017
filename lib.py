import time
import functools
import itertools
from operator import xor

def measure(fn):
    start = time.time()
    fn()
    return time.time() - start

def readfile(file, separator = None):
    lines = []
    with open(file) as fp:
        for line in fp.readlines():
            line = line.strip()
            if separator:
                line = line.split(separator)
            lines.append(line)
    return lines

def remove_empty(lst):
    return list(filter(None, lst))


def reverse_part(lst, pos, length):
    """
    reverse a part of a given list, wrapping around at the end if 
    pos + length is > len(lst).
    e.g.:
    reverse([1,2,3,4,5,6], 0, 3) ==> [3,2,1,4,5,6]
    reverse([1,2,3,4,5,6], 3, 3) ==> [1,2,3,6,5,4]
    reverse([1,2,3,4,5,6], 4, 3) ==> [5,2,3,4,1,6]
    reverse([1,2,3,4,5,6], 5, 3) ==> [1,6,3,4,5,2]
    """
    turn_list = []
    lst = list(lst)
    for i in range(pos, pos+length):
        turn_list.append(lst[i%len(lst)])
    turn_list = list(reversed(turn_list))
    for i in range(0, length):
        idx = (pos + i) % len(lst)
        lst[idx] = turn_list[i]
    return lst


def knot_hash(input):
    """
        generates a "knot hash" (see day 10) of the given
        string / list.
        returns a hex string of 32 hex chars / 16 bytes
    """
    input_list = list(itertools.chain([ord(x) for x in list(input)],[17, 31, 73, 47, 23]))
    knot_list = range(0, 256)
    skip_size = 0
    pos = 0

    # hash rounds: 64
    for i in range(0, 64):
        for l in input_list:
            knot_list = reverse_part(knot_list, pos, l )
            pos = (pos + l + skip_size) % len(knot_list)
            skip_size += 1

    # chunk it to 16x16 chunks and xor
    chunks = []
    for i in range(0,256,16):
        chunks.append(functools.reduce(xor,knot_list[i:i+16]))

    # form hex hash:
    return ''.join('{:02x}'.format(n) for n in chunks)
