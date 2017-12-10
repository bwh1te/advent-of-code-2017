#!/usr/bin/env python

from types import FunctionType


def calc_captcha(input_str, next_func):
    assert type(next_func) == FunctionType, "next_func param gets function or lambda"
    acc = 0
    for i, char in enumerate(input_str):
        next_char = input_str[next_func(i, input_str)]
        if char == next_char:
            acc += int(char)
    return acc

def get_next_index_1(current_index, sequence):
    if current_index + 1 < len(sequence):
        return current_index + 1
    else:
        return 0

def get_next_index_2(current_index, sequence):    
    steps_to_add = int(len(sequence) / 2)
    positions_to_end = (len(sequence) - 1) - current_index
    if steps_to_add <= positions_to_end:
        return current_index + steps_to_add
    else:
        return (steps_to_add - positions_to_end) - 1



with open("input.txt") as f:
    task_input = f.read()


assert calc_captcha("1122", get_next_index_1) == 3
assert calc_captcha("1111", get_next_index_1) == 4
assert calc_captcha("1234", get_next_index_1) == 0
assert calc_captcha("91212129", get_next_index_1) == 9

print("Part 1 answer is {}".format(calc_captcha(task_input, get_next_index_1)))


assert calc_captcha("1212", get_next_index_2) == 6
assert calc_captcha("1221", get_next_index_2) == 0
assert calc_captcha("123425", get_next_index_2) == 4
assert calc_captcha("123123", get_next_index_2) == 12
assert calc_captcha("12131415", get_next_index_2) == 4

print("Part 2 answer is {}".format(calc_captcha(task_input, get_next_index_2)))
