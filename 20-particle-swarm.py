import time
import lib
from lib import manhattan
import math
import re
import itertools

class Particle(object):
    def __init(self):
        self.index = 0
        self.coords = [0,0,0]
        self.v = [0,0,0]
        self.a = [0,0,0]

    def __str__(self):
        return "p=<{},{},{}>, v=<{},{},{}>, a=<{},{},{}>".format(
            self.coords[0], self.coords[1], self.coords[2],
            self.v[0], self.v[1], self.v[2],
            self.a[0], self.a[1], self.a[2],
        )
    
    def apply_tick(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        self.v[2] += self.a[2]
        self.coords[0] += self.v[0]
        self.coords[1] += self.v[1]
        self.coords[2] += self.v[2]

def read_input():
    # lines = lib.readfile('inputs/20-input-sample.txt')
    # lines = lib.readfile('inputs/20-input-sample2.txt')
    lines = lib.readfile('inputs/20-input.txt')
    particles = []
    m = re.compile(r"p=<([0-9-]+),([0-9-]+),([0-9-]+)>,v=<([0-9-]+),([0-9-]+),([0-9-]+)>,a=<([0-9-]+),([0-9-]+),([0-9-]+)>")
    index = 0
    for line in lines:
        line = line.strip().replace(' ','')
        g = m.match(line)
        if g:
            p = Particle()
            p.index = index
            p.coords = list(map(int, g.group(1,2,3)))
            p.v = list(map(int, g.group(4,5,6)))
            p.a = list(map(int, g.group(7,8,9)))
            particles.append(p)
            index += 1
    return particles

def min_dist_particle(particles):
    dist = 0
    min_index = -1
    for i in range(0, len(particles)):
        m = manhattan(particles[i].coords)
        if dist == 0 or m < dist:
            dist = m
            min_index = i
    return min_index

def find_smallest_a(particles):
    min_a = 0
    for i in range(0, len(particles)):
        p = particles[i]
        m = manhattan(p.a)
        if min_a == 0 or m < min_a:
            min_a = m
    return min_a

def find_smallest_v(particles):
    min_v = 0
    for i in range(0, len(particles)):
        p = particles[i]
        m = manhattan(p.v)
        if min_v == 0 or m < min_v:
            min_v = m
    return min_v

def find_smallest_d(particles):
    min_d = 0
    for i in range(0, len(particles)):
        p = particles[i]
        m = manhattan(p.coords)
        if min_d == 0 or m < min_d:
            min_d = m
    return min_d


def problem1(input):
    # the one that has the smallest accelleration will stay closest.
    # so find those with the (same) smalles acc:
    smallest_a = find_smallest_a(input)
    smallest_a_particles = list(filter(lambda p:manhattan(p.a) == smallest_a, input))

    # now from this set, those with the smallest velocity will be slower in the long run:
    smallest_v = find_smallest_v(smallest_a_particles)
    smallest_v_particles = list(filter(lambda p:manhattan(p.v) == smallest_v, smallest_a_particles))

    # ... and from the slowest, which one is the nearest? that must be the one:
    smallest_d = find_smallest_d(smallest_v_particles)
    smallest_d_particles = list(filter(lambda p:manhattan(p.coords) == smallest_d, smallest_v_particles))

    solution = smallest_d_particles.pop().index
    
    # for i in range(0,10000):
    #     for p in input:
    #         p.apply_tick()
    #     min_p = min_dist_particle(input)
    #     print("Min p: {}".format(min_p))

    print("Solution 1: {}".format(solution))

def find_colliding_p(particles):
    # 1. create a hash of the location of each particle
    # 2. check it against a set. If already in the set, add to collide list
    # 3. if not, add hash to set
    # 4. return collide list
    collide_list = []
    location_hashes = dict()
    for p in particles:
        h = str(p.coords)
        if h in location_hashes.keys():
            collide_list.append(p)
            if location_hashes[h] not in collide_list:
                collide_list.append(location_hashes[h])
        else:
            location_hashes[h] = p
    return collide_list

def find_slower(particles, p):
    slower = []
    v = manhattan(p.v)
    for test_p in particles:
        if manhattan(test_p.v) < v:
            slower.append(test_p)
    return slower

def find_smaller_a(particles, p):
    slower = []
    a = manhattan(p.a)
    for test_p in particles:
        if manhattan(test_p.a) < a:
            slower.append(test_p)
    return slower

def problem2(input):
    run = True
    while run:
        collides = find_colliding_p(input)
        for c in collides:
            input.remove(c)

        # after movement, check for possible future colissions:
        # find the particle(s) nearest to 0 (if some have the same smalles distance, consider all)
        # for each found particle, check:
        #   are there SLOWER ones? if yes, we might have a colission in the future, so proceed
        #   are there ones with smaller accelleration? if yes, we might have a colission in the future, so proceed
        #   --> in any case, repeat
        #  if not, we're done.
        smallest_d = find_smallest_d(input)
        smallest_d_particles = list(filter(lambda p:manhattan(p.coords) == smallest_d, input))
        to_check = set(input) - set(smallest_d_particles)
        possible_coll_nr = 0
        for p in smallest_d_particles:
            slower = find_slower(to_check, p)
            possible_coll_nr += len(slower)

            smaller_a = find_smaller_a(to_check, p)
            possible_coll_nr += len(smaller_a)
        if possible_coll_nr == 0:
            break

        # move forward in time:
        for p in input:
            p.apply_tick()


    solution = len(input)
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
