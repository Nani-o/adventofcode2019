#!/usr/bin/env python

import pytest
from aoc.day2 import part1, part2

def test_part1():
    input = "1,9,10,3,2,3,11,0,99,30,40,50"
    solution = part1(input)
    assert solution == 3500

def test_part2():
    input = "1,9,10,3,2,3,11,0,99,30,40,50"
    intcode_output = 5100
    solution = part2(input, intcode_output)
    assert solution == 308
