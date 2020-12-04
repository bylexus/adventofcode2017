import time
import lib
import functools
import math
import re
import operator

registers = dict()
instructions = []
globals = {
    'max_value': 0
}


class Instruction:
    ops_map = {
        '<': operator.lt,
        '>': operator.gt,
        '<=': operator.le,
        '>=': operator.ge,
        '==': operator.eq,
        '!=': operator.ne,
        'inc': operator.add,
        'dec': operator.sub
    }

    def __init__(self):
        self.reg = None
        self.op = None
        self.val = None
        self.cond_reg = None
        self.cond_op = None
        self.cond_val = None

    def mod_reg(self, registers):
        reg_val = registers.get(self.reg, 0)
        reg_cond_val = registers.get(self.cond_reg, 0)

        if (self.ops_map[self.cond_op])(reg_cond_val, self.cond_val):
            registers[self.reg] = self.ops_map[self.op](reg_val, self.val)
            # for 2nd part of the puzzle: keep the max value ever used:
            globals['max_value'] = max(
                registers[self.reg], globals['max_value'])


def read_input():
    m = re.compile(
        r"(\w+)\s+(\w+)\s+([0-9-]+)\s+if\s+(\w+)\s+(<|>|<=|>=|==|!=)\s+([0-9-]+)")
    # read all nodes, create each without processing childs:
    for line in lib.readfile('inputs/08-input.txt'):
        g = m.match(line)
        if g:
            (reg, op, val, cond_reg, cond_op, cond_val) = g.group(1, 2, 3, 4, 5, 6)
            instr = Instruction()
            instr.reg = reg
            instr.op = op
            instr.val = int(val)
            instr.cond_reg = cond_reg
            instr.cond_op = cond_op
            instr.cond_val = int(cond_val)
            instructions.append(instr)


def problem1():
    for instr in instructions:
        instr.mod_reg(registers)
    solution = max(registers.values())

    print("Solution 1: Solution: {}".format(solution))


def problem2():
    solution = globals['max_value']
    print("Solution 2: Solution: {}".format(solution))


def main():
    title = "Advent of Code 2017!"
    print("{title}\n{line}\n\n".format(title=title, line="="*len(title)))

    read_input()

    t1 = lib.measure(problem1)
    print("Problem 1 took {:.3f}s to solve.\n\n".format(t1))

    t2 = lib.measure(problem2)
    print("Problem 2 took {:.3f}s to solve.".format(t2))


if __name__ == "__main__":
    main()
