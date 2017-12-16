#!/usr/bin/env python

import re

from collections import Counter


NODE_REGEXP = re.compile("(?P<name>[a-z]+)\s\((?P<size>\d+)\)")


class Node:

    size = 0

    def __init__(self, name):
        self.name = name
        self.children = []

    def __repr__(self):
        return "{}({}): [{}]".format(
            self.name, 
            self.size,
            ", ".join(repr(x) for x in self.children)
        )

    def add_child(self, obj):
        self.children.append(obj)

    def find(self, name):
        if name == self.name:
            return self
        for child in self.children:
            obj = child.find(name)
            if obj:
                return obj


def parse_tree(raw_str):

    prepared_nodes = dict()

    for line in raw_str.strip().split("\n"):
        node_str, _, children_str = line.strip().partition(" -> ")

        parsed_name = NODE_REGEXP.search(node_str)
        name = parsed_name.group("name")
        size = parsed_name.group("size")

        from_children = False
        if name in prepared_nodes:
            node = prepared_nodes[name]
        else:
            for _, node_obj in prepared_nodes.items():
                search_result = node_obj.find(name)
                if search_result:
                    node = search_result
                    from_children = True
                    break
            else:
                node = Node(name)

        node.size = int(size)

        for child_name in children_str.strip().split(", "):
            if child_name in prepared_nodes:
                child_node = prepared_nodes[child_name]
                del prepared_nodes[child_name]
            elif child_name:
                child_node = Node(child_name)
            else:
                continue
            node.add_child(child_node)

        if not from_children:
            prepared_nodes[name] = node

    assert len(prepared_nodes) == 1, "Can't detect root item"
    _, tree = prepared_nodes.popitem()
    return tree


def draw_tree(node, tabs=0):
    print("{tabs}{name}({size}):".format(
        tabs="\t" * tabs, 
        name=node.name, 
        size=node.size)
    )
    for child in node.children:
        draw_tree(child, tabs + 1)


# Tests
test = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""
test_tree = parse_tree(test)
assert test_tree.name == "tknk"


# Solution
with open("input.txt") as f:
    task_input = f.read()
task_tree = parse_tree(task_input)

print("Part 1 answer is {}".format(task_tree.name))
