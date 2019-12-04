#!/usr/bin/env python

import pytest
from aoc.day4 import check_rules

test_inputs1 = [
    "111111",
    "223450",
    "123789",
]
test_inputs2 = [
    "112233",
    "123444",
    "111122",
]

expected_part1 = [True, False, False]
expected_part2 = [True, False, True]

@pytest.mark.parametrize("input,expected", list(zip(test_inputs1, expected_part1)))
def test_rules_part1(input, expected):
    validity = check_rules(input)
    assert validity == expected

@pytest.mark.parametrize("input,expected", list(zip(test_inputs2, expected_part2)))
def test_rules_part2(input, expected):
    validity = check_rules(input, version="v2")
    assert validity == expected
