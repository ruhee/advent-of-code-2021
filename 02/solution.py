#! /usr/local/bin/python3

def split_line(line):
    instruction, quantity = line.split(' ')
    return [instruction, int(quantity)]

filepath = 'input.txt'
file = open(filepath, 'r').read().strip().split('\n')


def part1():
    horizontal_position = 0
    depth = 0

    for line in file:
        instruction, quantity = split_line(line)

        # python match case statement is only available in > 3.10 :(
        if instruction == 'forward':
            horizontal_position += quantity
        elif instruction == 'up':
            depth -= quantity
        elif instruction == 'down':
            depth += quantity

    print(f'Part 1: {horizontal_position * depth}')

def part2():
    horizontal_position = 0
    depth = 0
    aim = 0

    for line in file:
        instruction, quantity = split_line(line)

        if instruction == 'forward':
            horizontal_position += quantity
            depth += aim*quantity
        elif instruction == 'up':
            aim -= quantity
        elif instruction == 'down':
            aim += quantity

    print(f'Part 2: {horizontal_position * depth}')


part1()
part2()