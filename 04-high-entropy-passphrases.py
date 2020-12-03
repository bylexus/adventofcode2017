import time
import lib
import functools
import math

lines = lib.readfile('inputs/04-input.txt')


def check_phrase1(phrase):
    word_hash = {}
    words = phrase.split(' ')
    for word in words:
        count = word_hash.get(word)
        if count:
            return False
        else:
            word_hash[word] = 1
    return True

def check_phrase2(phrase):
    word_hash = {}
    words = phrase.split(' ')
    for word in words:
        word = "".join(sorted(word))
        count = word_hash.get(word)
        if count:
            return False
        else:
            word_hash[word] = 1
    return True



def problem1():
    correct_phrases = 0

    for line in lines:
        if check_phrase1(line):
            correct_phrases = correct_phrases + 1

    print("Solution 1: The nr of correct phrases is {}".format(correct_phrases))


def problem2():
    correct_phrases = 0

    for line in lines:
        if check_phrase2(line):
            correct_phrases = correct_phrases + 1

    print("Solution 2: The nr of correct phrases is {}".format(correct_phrases))


def main():
    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    t1 = lib.measure(problem1)
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2 = lib.measure(problem2)
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
