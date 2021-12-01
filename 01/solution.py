#! /usr/bin/python

filepath = 'input.txt'
file = open(filepath, 'r').read().strip().split('\n')
input = map(int, file)

# part 1
greater_than = 0

for idx, val in enumerate(input):
    if idx > 0:
        if val > input[idx - 1]:
            greater_than += 1

print(greater_than)

# part 2
second_greater_than = 0

for idx, val in enumerate(input):
    if idx <= len(input) - 4:
        first = val + input[idx+1] + input[idx+2]
        second = input[idx+1] + input[idx+2] + input[idx+3] 

        if second > first:
            second_greater_than += 1

print(second_greater_than)