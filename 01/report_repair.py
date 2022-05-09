"""
Day 1: Report Repair
https://adventofcode.com/2020/day/1
"""


def load_data(filename="01/test_input.txt"):
    with open(filename) as f:
        data = [int(line.strip()) for line in f.readlines()]
    return data


def part1(data):
    for num in data:
        if 2020 - num in data:
            return (num, 2020 - num)


def part2(data):
    for num in data:
        for another_num in data:
            if 2020 - num - another_num in data:
                return (num, another_num, 2020 - num - another_num)


data = load_data("01/input.txt")
a, b = part1(data)
print(a, b, a * b)


data = load_data("01/input.txt")
a, b, c = part2(data)
print(a, b, c, a * b * c)
