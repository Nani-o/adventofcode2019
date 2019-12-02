#!/usr/bin/env python

import math

def part1(puzzle_input):
    modules_mass = list(map(int, puzzle_input.split()))
    total_fuel_required = 0
    for module_mass in modules_mass:
        total_fuel_required += fuel_for_mass(module_mass)
    return total_fuel_required

def part2(puzzle_input):
    modules_mass = list(map(int, puzzle_input.split()))
    total_fuel_required = 0
    for module_mass in modules_mass:
        total_fuel_required += fuel_for_mass_and_extra_fuel(module_mass)
    return total_fuel_required

def fuel_for_mass(mass):
    fuel = math.floor(mass / 3) - 2
    return fuel

def fuel_for_mass_and_extra_fuel(mass):
    total_fuel = 0
    fuel = fuel_for_mass(mass)
    if fuel > 0:
        total_fuel += fuel
        total_fuel += fuel_for_mass_and_extra_fuel(fuel)
    return total_fuel
