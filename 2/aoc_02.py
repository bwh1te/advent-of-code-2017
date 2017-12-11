#!/usr/bin/env python

from itertools import permutations
from types import FunctionType


def calc_checksum(spreadsheet, sum_func=None):
    assert type(sum_func) == FunctionType, "sum_func param gets function or lambda"
    checksum = 0
    for line in spreadsheet.split("\n"):
        numbers = [int(x.strip()) for x in line.split("\t") if x.strip().isdigit()]
        if not numbers:
            continue
        checksum += sum_func(numbers)
    return checksum


def min_max(numbers):
    return max(numbers) - min(numbers)


def evenly_div(numbers):
    for first, second in permutations(numbers, 2):
        if first % second == 0:
            return first // second
    return 0


with open("input.txt") as f:
    task_input = f.read()


test_sheet = "5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8"
assert calc_checksum(test_sheet, sum_func=min_max) == 18

print("Part 1 answer is {}".format(calc_checksum(task_input, sum_func=min_max)))


test_sheet = "5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5"
assert calc_checksum(test_sheet, sum_func=evenly_div) == 9

print("Part 2 answer is {}".format(calc_checksum(task_input, sum_func=evenly_div)))
