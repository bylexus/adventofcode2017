import time
import lib
import math
import re
import itertools
from collections import deque

class CPU:
    def __init__(self, prg_mem):
        self.prg_mem = list(prg_mem)
        self.reset()

    def reset(self):
        self.registers = dict()
        self.iptr = 0
        self.running = True
        self.last_freq = 0
        self.rec_freq = 0

    def get_reg_val(self, reg):
        return self.registers.get(reg, 0)

    def set_reg_val(self, reg, val):
        self.registers[reg] = val

    def exec_next(self, stop_at_rcv = False):
        if self.iptr < 0 or self.iptr >= len(self.prg_mem):
            self.running = False
            return False
        instr = self.prg_mem[self.iptr]
        op = instr[0]
        val_1 = instr[1]
        val_2 = instr[2] if len(instr) > 2 else None
        real_val_1 = val_1 if isinstance(val_1, int) else self.get_reg_val(val_1)
        real_val_2 = val_2 if isinstance(val_2, int) else (self.get_reg_val(val_2) if val_2 else None)
        inc_ptr = 1
        if op == 'snd':
            # print("Sound: {}".format(real_val_1))
            self.last_freq = real_val_1
        elif op == 'set':
            self.set_reg_val(val_1, real_val_2)
        elif op == 'add':
            self.set_reg_val(val_1, self.get_reg_val(val_1) + real_val_2)
        elif op == 'mul':
            self.set_reg_val(val_1, self.get_reg_val(val_1) * real_val_2)
        elif op == 'mod':
            self.set_reg_val(val_1, self.get_reg_val(val_1) % real_val_2)
        elif op == 'rcv':
            if real_val_1 != 0:
                self.rec_freq = self.last_freq
                if stop_at_rcv:
                    self.running = False
                    return True
        elif op == 'jgz':
            if real_val_1 > 0:
                inc_ptr = real_val_2

        self.iptr += inc_ptr
        return  True

class CPU2:
    def __init__(self, prg_mem, nr):
        self.prg_mem = list(prg_mem)
        self.receiver_cpu = None
        self.nr = nr
        self.reset()

    def reset(self):
        self.dataq = deque()
        self.registers = dict()
        self.registers['p'] = self.nr
        self.iptr = 0
        self.running = True
        self.send_counter = 0

    def get_reg_val(self, reg):
        return self.registers.get(reg, 0)

    def set_reg_val(self, reg, val):
        self.registers[reg] = val

    def exec_next(self):
        self.running = True
        if self.iptr < 0 or self.iptr >= len(self.prg_mem):
            self.running = False
            return False
        instr = self.prg_mem[self.iptr]
        op = instr[0]
        val_1 = instr[1]
        val_2 = instr[2] if len(instr) > 2 else None
        real_val_1 = val_1 if isinstance(val_1, int) else self.get_reg_val(val_1)
        real_val_2 = val_2 if isinstance(val_2, int) else (self.get_reg_val(val_2) if val_2 else None)
        inc_ptr = 1
        if op == 'snd':
            self.receiver_cpu.dataq.append(real_val_1)
            self.send_counter += 1
        elif op == 'set':
            self.set_reg_val(val_1, real_val_2)
        elif op == 'add':
            self.set_reg_val(val_1, self.get_reg_val(val_1) + real_val_2)
        elif op == 'mul':
            self.set_reg_val(val_1, self.get_reg_val(val_1) * real_val_2)
        elif op == 'mod':
            self.set_reg_val(val_1, self.get_reg_val(val_1) % real_val_2)
        elif op == 'rcv':
            if len(self.dataq):
                data = self.dataq.popleft()
                self.set_reg_val(val_1, data)
            else:
                inc_ptr = 0
                self.running = False
        elif op == 'jgz':
            if real_val_1 > 0:
                inc_ptr = real_val_2

        self.iptr += inc_ptr
        return  True


def read_input():
    # ops = list(map(lambda line:line.split(' '), lib.remove_empty(lib.readfile('inputs/18-input-sample.txt'))))
    # ops = list(map(lambda line:line.split(' '), lib.remove_empty(lib.readfile('inputs/18-input-sample2.txt'))))
    ops = list(map(lambda line:line.split(' '), lib.remove_empty(lib.readfile('inputs/18-input.txt'))))
    for i in range(0, len(ops)):
        try:
            nr = int(ops[i][1])
            ops[i][1] = nr
        except Exception:
            pass
        try:
            nr = int(ops[i][2])
            ops[i][2] = nr
        except Exception:
            pass
    return ops



def problem1(input):
    cpu = CPU(input)
    solution = 0
    while cpu.running:
        ret = cpu.exec_next(stop_at_rcv=True)
        if ret and cpu.running == False:
            solution = cpu.rec_freq
            break
    print("Solution 1: {}".format(solution))


def problem2(input):
    cpu0 = CPU2(input, 0)
    cpu1 = CPU2(input, 1)
    cpu0.receiver_cpu = cpu1
    cpu1.receiver_cpu = cpu0

    solution = 0
    while cpu0.running or cpu1.running:
        cpu0.exec_next()
        cpu1.exec_next()
    solution = cpu1.send_counter
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
