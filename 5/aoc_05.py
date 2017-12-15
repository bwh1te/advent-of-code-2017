#!/usr/bin/env python

def tape_runner(initial_state):
    tape = [int(x) for x in initial_state.strip().split("\n")]
    position = tape[0]
    moves = 0
    while True:
        try:
            jump_to = tape[position]
            tape[position] += 1
            position += jump_to
            moves += 1
        except IndexError:
            return moves


assert tape_runner("0\n3\n0\n1\n-3") == 5


# Solution
with open("input.txt") as f:
    task_input = f.read()

print("Part 1 answer is {}".format(tape_runner(task_input)))
