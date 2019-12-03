#!/usr/bin/env python

def get_wire_positions(wire):
    x, y, steps = 0, 0, 0
    positions = {}

    for move in wire.split(','):
        direction = move[0]
        distance = int(move[1:])
        for i in range(distance):
            if direction == "L":
                x -= 1
            if direction == "R":
                x += 1
            if direction == "U":
                y += 1
            if direction == "D":
                y -= 1

            steps += 1
            if (x,y) not in positions.keys():
                positions[(x,y)] = steps
    return positions

def distance_between(coordinate, coordinate2):
    x, y = coordinate
    j, k = coordinate2
    return abs(x - j) + abs(y - k)

def find_wires_intersections(wire1_positions, wire2_positions):
    return list(set(wire1_positions.keys()) & set(wire2_positions.keys()))

def get_wires(puzzle_input):
    wires = puzzle_input.split('\n')
    return wires[0], wires[1]

def part1(puzzle_input):
    wire, wire2 = get_wires(puzzle_input)
    wire_positions = get_wire_positions(wire)
    wire2_positions = get_wire_positions(wire2)
    intersections = find_wires_intersections(wire_positions, wire2_positions)

    closest_intersection_distance = 0
    for intersection in intersections:
        intersection_distance = distance_between((0,0), intersection)
        if not closest_intersection_distance or closest_intersection_distance > intersection_distance:
            closest_intersection_distance = intersection_distance
            closest_intersection = intersection
    return closest_intersection_distance

def part2(puzzle_input, intcode_output=19690720):
    wire, wire2 = get_wires(puzzle_input)
    wire_positions = get_wire_positions(wire)
    wire2_positions = get_wire_positions(wire2)
    intersections = find_wires_intersections(wire_positions, wire2_positions)

    lowest_steps_intersection = 0
    for intersection in intersections:
        total_steps = wire_positions[intersection] + wire2_positions[intersection]
        if not lowest_steps_intersection or lowest_steps_intersection > total_steps:
            lowest_steps_intersection = total_steps
    return lowest_steps_intersection
