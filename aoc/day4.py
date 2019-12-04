#!/usr/bin/env python

import re

def check_rules(password, version="v1"):
    if version == "v1":
        if not rule1(password) or not rule2(password) or not rule3(password):
            return False
    elif version == "v2":
        if not rule1(password) or not rule2_v2(password) or not rule3(password):
            return False
    return True

def rule1(password):
    if not password.isdigit() or not len(password) == 6:
        return false
    return True

def rule2(password):
    match = re.search(r"(.)\1", password)
    if match:
        return True
    return False

def rule2_v2(password):
    for match in re.findall(r"((.)\2{2,})", password):
        password = password.replace(match[0], '')
    return rule2(password)

def rule3(password):
    for index in range(len(password) - 1):
        if password[index] > password[index+1]:
            return False
    return True

def part1(puzzle_input):
    rangemin, rangemax = [int(x) for x in puzzle_input.split('-')]
    passwords = []
    for password in [str(x) for x in range(rangemin, rangemax+1)]:
        if check_rules(password):
            passwords.append(password)
    return len(passwords)


def part2(puzzle_input, intcode_output=19690720):
    rangemin, rangemax = [int(x) for x in puzzle_input.split('-')]
    passwords = []
    for password in [str(x) for x in range(rangemin, rangemax+1)]:
        if check_rules(password, version="v2"):
            passwords.append(password)
    return len(passwords)
