#!/usr/bin/env python

import pytest
from aoc.day1 import part1, part2

def test_part1():
    input = """12
               14
               1969
               100756"""
    solution = part1(input)
    assert solution == 34241

def test_part2():
    input = """14
               1969
               100756"""
    solution = part2(input)
    assert solution == 51314
