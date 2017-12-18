#!/usr/bin/env python


def count_groups(sequence, state=None):

    if not state:
        state = dict(
            groups_count=0, 
            opened_braces=0, 
            is_garbage=False, 
            ignore_next=False
        )

    head, tail = sequence[0], sequence[1:]

    if not state["ignore_next"]:
        if not state["is_garbage"]:
            if head == "{":
                state["opened_braces"] += 1
            elif head == "}" and state["opened_braces"] > 0:
                state["opened_braces"] -= 1
                state["groups_count"] += 1
            elif head == "<":
                state["is_garbage"] = True            
        else:
            if head == ">":
                state["is_garbage"] = False
            elif head == "!":
                state["ignore_next"] = True
    else:
        state["ignore_next"] = False

    if tail:
        count_groups(tail, state)
    return state["groups_count"]





# Tests
assert count_groups("{}") == 1
assert count_groups("{{{}}}") == 3
assert count_groups("{{},{}}") == 3
assert count_groups("{{{},{},{{}}}}") == 6
assert count_groups("{<{},{},{{}}>}") == 1
assert count_groups("{<a>,<a>,<a>,<a>}") == 1
assert count_groups("{{<a>},{<a>},{<a>},{<a>}}") == 5
assert count_groups("{{<!>},{<!>},{<!>},{<a>}}") == 2





# Solution
with open("input.txt") as f:
    task_input = f.read()

print("Part 1 answer is {}".format(count_groups(task_input)))
