'''
Day 8: Handheld Halting
https://adventofcode.com/2020/day/8
'''


from typing import List, Tuple


def load_data(filename='08/test_input.txt') -> List[Tuple[str, int]]:
    with open(filename) as f:
        data = []
        for line in f.readlines():
            command, num = line.split(' ')
            data.append((command, int(num)))
    return data


def part1(data):
    acc = 0
    i = 0
    visited = set()

    while i not in visited and i < (len(data)):
        visited.add(i)

        command, num = data[i]

        if command == 'nop':
            i += 1
        elif command == 'acc':
            acc += num
            i += 1
        elif command == 'jmp':
            i += num

    return i, acc


def part2(data):
    # Filter rows with either nop or jmp
    target_rows = [
        i for i, (command, _) in enumerate(data) if command in ('nop', 'jmp')
    ]

    # Try changing data (rows with nop or jmp) until success
    for i in target_rows:

        temp_data = data[:]  # copy data
        command, num = temp_data[i]

        if command == 'nop':
            temp_data[i] = ('jmp', num)
        else:
            temp_data[i] = ('nop', num)

        temp_i, acc = part1(temp_data)

        if temp_i == len(data):
            return temp_i, acc


test_data = load_data()
i, acc = part1(test_data)
assert acc == 5, 'Part 1 does not work on test data'

# Part 1
data = load_data('08/input.txt')
i, acc = part1(data)
print(i, acc)

# Part 2
i, acc = part2(data)
print(i, acc)
