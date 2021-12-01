#! /usr/bin/python

filepath = 'input.txt'
input = open(filepath, 'r').read().strip().split('\n')

# part 1
greater_than = 0

for idx, val in enumerate(input):
    if idx > 0:
        if int(val) > int(input[idx - 1]):
            greater_than += 1

print(greater_than)

# part 2
second_greater_than = 0

for idx, val in enumerate(input):
    if idx <= len(input) - 4:
        first = int(val) + int(input[idx+1]) + int(input[idx+2])
        second = int(input[idx+1]) + int(input[idx+2]) + int(input[idx+3]) # jesus christ

        if second > first:
            second_greater_than += 1

print(second_greater_than)