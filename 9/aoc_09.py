#!/usr/bin/env python

def parse_groups(sequence, state=None):

    state = dict(
        groups_count=0,
        groups_score=0,
        opened_braces=0,
        is_garbage=False,
        ignore_next=False,
        garbage_size=0
    )

    for char in sequence:
        if not state["ignore_next"]:
            if not state["is_garbage"]:
                if char == "{":
                    state["opened_braces"] += 1
                elif char == "}" and state["opened_braces"] > 0:
                    state["groups_score"] += state["opened_braces"]
                    state["opened_braces"] -= 1
                    state["groups_count"] += 1
                elif char == "<":
                    state["is_garbage"] = True            
            else:
                if char == ">":
                    state["is_garbage"] = False
                elif char == "!":
                    state["ignore_next"] = True
                else:
                    state["garbage_size"] += 1
        else:
            state["ignore_next"] = False

    return state["groups_count"], state["groups_score"], state["garbage_size"]


count_groups = lambda x: parse_groups(x)[0]
score_groups = lambda x: parse_groups(x)[1]
garbage_size = lambda x: parse_groups(x)[2]


# Tests
assert count_groups("{}") == 1
assert count_groups("{{{}}}") == 3
assert count_groups("{{},{}}") == 3
assert count_groups("{{{},{},{{}}}}") == 6
assert count_groups("{<{},{},{{}}>}") == 1
assert count_groups("{<a>,<a>,<a>,<a>}") == 1
assert count_groups("{{<a>},{<a>},{<a>},{<a>}}") == 5
assert count_groups("{{<!>},{<!>},{<!>},{<a>}}") == 2

assert score_groups("{}") == 1
assert score_groups("{{{}}}") == 6
assert score_groups("{{},{}}") == 5
assert score_groups("{{{},{},{{}}}}") == 16
assert score_groups("{<a>,<a>,<a>,<a>}") == 1
assert score_groups("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
assert score_groups("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
assert score_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

assert garbage_size("<>") == 0
assert garbage_size("<random characters>") == 17
assert garbage_size("<<<<>") == 3
assert garbage_size("<{!>}>") == 2
assert garbage_size("<!!>") == 0
assert garbage_size("<!!!>>") == 0
assert garbage_size('<{o"i!a,<{i<a>') == 10


# Solution
with open("input.txt") as f:
    task_input = f.read().strip()

print("Part 1 answer is {}".format(score_groups(task_input)))
print("Part 2 answer is {}".format(garbage_size(task_input)))
