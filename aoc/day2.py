#!/usr/bin/env python

import math

def part1(puzzle_input):
    intcodes = reset_memory(puzzle_input)
    # Exercise say : before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
    # I removed this line and edited the inputs/day2 file directly to not mess with the test
    # intcodes[1], intcodes[2] = 12, 2
    return execute_intcodes(intcodes)

def part2(puzzle_input, intcode_output=19690720):
    intcodes = reset_memory(puzzle_input)
    max_range = len(intcodes) - 1
    for x in range(1,max_range):
        for y in range(1,max_range):
            intcodes[1], intcodes[2] = x, y
            result = execute_intcodes(intcodes)
            if result == intcode_output:
                return 100 * x + y
            else:
                intcodes = reset_memory(puzzle_input)
                continue

def execute_intcodes(intcodes):
    index = 0
    while True:
        new_intcodes = execute_opcode(intcodes, index)
        if new_intcodes:
            index += 4
            intcodes = new_intcodes
        else:
            break
    return intcodes[0]

def execute_opcode(intcodes, index):
    opcode = intcodes[index]
    if opcode == 1:
        print(index)
        intcodes[intcodes[index+3]] = intcodes[intcodes[index+1]] + intcodes[intcodes[index+2]]
    elif opcode == 2:
        intcodes[intcodes[index+3]] = intcodes[intcodes[index+1]] * intcodes[intcodes[index+2]]
    elif opcode == 99:
        intcodes = None
    else:
        pass
    return intcodes

def reset_memory(puzzle_input):
    return list(map(int, puzzle_input.split(',')))
