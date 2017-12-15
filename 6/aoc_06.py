#!/usr/bin/env python

from itertools import cycle


def parse_input(raw_str):
    return [int(item) for item in raw_str.strip().split("\t")]


def reallocate(banks):
    """
    :param banks: list of numbers of blocks in each bank
    :return: tuple (number of cycles before configuration repeats, 
        number of cycles between configuration appearences)
    """

    def get_next(i):
        return i + 1 if i < len(banks) - 1 else 0

    seen = []
    while True:
        blocks_num, position = max(banks), banks.index(max(banks))
        banks[position] = 0
        while blocks_num > 0:
            position = get_next(position)
            banks[position] += 1
            blocks_num -= 1
        state = " ".join(str(x) for x in banks)
        # print(seen)
        if state in seen:
            return len(seen) + 1, len(seen) - seen.index(state)
        else:
            seen.append(state)


# Tests
assert reallocate(parse_input("0\t2\t7\t0")) == (5, 4)


# Solution
with open("input.txt") as f:
    task_input = parse_input(f.read())


cycles, distance = reallocate(task_input)
print("Part 1 answer is {}".format(cycles))
print("Part 2 answer is {}".format(distance))
