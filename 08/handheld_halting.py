'''
Day 8: Handheld Halting
https://adventofcode.com/2020/day/8
'''


def load_data(filename='08/test_input.txt'):
    with open(filename) as f:
        data = []
        for line in f.readlines():
            command, num = line.split(" ")
            data.append((command, int(num)))
    return data


def part1(data):
    acc = 0
    i = 0
    visited = set()

    while i not in visited:
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


test_data = load_data()
i, acc = part1(test_data)
assert acc == 5, "Part 1 does not work on test data"

# Part 1
data = load_data('08/input.txt')
i, acc = part1(data)

print(i, acc)
