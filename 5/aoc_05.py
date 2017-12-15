#!/usr/bin/env python

def tape_runner(initial_state, increase_func=None):
    tape = [int(x) for x in initial_state.strip().split("\n")]
    position = tape[0]
    moves = 0
    while True:
        try:
            jump_to = tape[position]
            tape[position] += increase_func(jump_to)
            position += jump_to
            moves += 1
        except IndexError:
            return moves


def one_anyway(jump_length):
    return 1


def lt_three(jump_length):
    return -1 if jump_length >= 3 else 1


assert tape_runner("0\n3\n0\n1\n-3", increase_func=one_anyway) == 5
assert tape_runner("0\n3\n0\n1\n-3", increase_func=lt_three) == 10


# Solution
with open("input.txt") as f:
    task_input = f.read()

print("Part 1 answer is {}".format(tape_runner(task_input, increase_func=one_anyway)))
print("Part 2 answer is {}".format(tape_runner(task_input, increase_func=lt_three)))
