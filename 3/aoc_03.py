#!/usr/bin/env python

import math
from functools import partial
from types import FunctionType


def spiral_coords_gen():
    x = y = 0
    turn = 1
    step = 1
    yield 0, 0
    while True:
        for n in range(0, turn):
            x, y = x + step, y
            yield x, y
        for n in range(0, turn):
            x, y = x, y + step
            yield x, y
        turn += 1
        step *= -1


class SequenceGenerator(object):

    def __init__(self):
        self._cache = {
            (0, 0): 1,
        }
        self._prev_x = 0
        self._prev_y = 0
        self._coords_gen = spiral_coords_gen()
        self._stop = False

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self._stop:
            raise StopIteration()
        x, y = next(self._coords_gen)
        self._cache[(x, y)] = self._calc_value(x, y)
        self._prev_x, self._prev_y = x, y
        return (x, y), self._cache[(x, y)]

    def _calc_value(self, x, y):
        raise NotImplemented()


class IncreasingGenerator(SequenceGenerator):

    def _calc_value(self, x, y):
        if x or y:
            self._cache[(x, y)] = self._cache[(self._prev_x, self._prev_y)] + 1
        return self._cache[(x, y)]


class AdjacentSumGenerator(SequenceGenerator):

    def _calc_value(self, x, y):
        if x or y:
            current_value = sum(
                self._cache.get((x + dx, y + dy), 0) 
                for dx in (-1, 0, 1) 
                for dy in (-1, 0, 1)
            )
            self._cache[(x, y)] = current_value
        return self._cache[(x, y)]


def get_coords_and_value(point_value, generator_cls=None):
    gen = generator_cls()
    current_value = 0
    x = y = 0
    while current_value < point_value:
        (x, y), current_value = next(gen)
    return (x, y), current_value


def get_distance(coords_value_a, coords_value_b):
    (x1, y1), _ = coords_value_a
    (x2, y2), _ = coords_value_b
    return abs(x1 - x2) + abs(y1 - y2)


get_distance_from_zero = partial(get_distance, coords_value_b=((0, 0), 0))



test_input = 368078

assert get_distance_from_zero(get_coords_and_value(1, IncreasingGenerator)) == 0
assert get_distance_from_zero(get_coords_and_value(12, IncreasingGenerator)) == 3
assert get_distance_from_zero(get_coords_and_value(23, IncreasingGenerator)) == 2
assert get_distance_from_zero(get_coords_and_value(1024, IncreasingGenerator)) == 31

print("Part 1 answer for input={} is {}".format(test_input, get_distance_from_zero(get_coords_and_value(368078, IncreasingGenerator))))


assert get_distance_from_zero(get_coords_and_value(1, AdjacentSumGenerator)) == 0
assert get_distance_from_zero(get_coords_and_value(11, AdjacentSumGenerator)) == 2
assert get_distance_from_zero(get_coords_and_value(59, AdjacentSumGenerator)) == 4
assert get_distance_from_zero(get_coords_and_value(806, AdjacentSumGenerator)) == 2

(_, _), value = get_coords_and_value(test_input, AdjacentSumGenerator)
print("Part 2 answer for input={} is {}".format(test_input, value))
