#!/usr/bin/env python

from collections import defaultdict


def do_instructions(instructions):
    registers = defaultdict(int)
    max_value = 0
    for line in instructions:
        instr, _, cond = line.partition(" if ")
        check_reg, _, cond = cond.partition(" ")

        if eval("registers[check_reg] " + cond):
            reg_name, action, value_str = instr.split(" ")
            adder = 1 if action == "inc" else -1
            registers[reg_name] += adder * int(value_str)
            
            max_value = max(max_value, registers[reg_name])

    # TODO: More elegant solution
    print("Part 2: Max reg_value={}".format(max_value))
    return registers


def get_max(registers):
    max_reg = max(registers, key=registers.get)
    return max_reg, registers[max_reg]


test_input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".strip().split("\n")
reg, val = get_max(do_instructions(test_input))
assert val == 1

with open("input.txt") as f:
    task_input = f.read().strip().split("\n")

reg, val = get_max(do_instructions(task_input))
print("Part 1 answer is {}".format(val))
