#!/usr/bin/env python

import pytest
from aoc.day3 import part1, part2

test_inputs = [
    "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83",
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
]

expected_part1 = [159, 135]
expected_part2 = [610, 410]

@pytest.mark.parametrize("input,expected", list(zip(test_inputs, expected_part1)))
def test_part1(input, expected):
    solution = part1(input)
    assert solution == expected

@pytest.mark.parametrize("input,expected", list(zip(test_inputs, expected_part2)))
def test_part2(input, expected):
    solution = part2(input)
    assert solution == expected
