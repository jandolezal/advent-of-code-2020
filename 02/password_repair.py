"""
Day 2: Password Philosophy
https://adventofcode.com/2020/day/2
"""

from collections import namedtuple
import re


Entry = namedtuple("Entry", "password letter low high".split())


def load_data(filename="02/test_input.txt"):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        data = []
        for line in lines:
            low, high, letter, password = re.split("-|: | ", line)
            data.append(
                Entry(password, letter, int(low), int(high))
            )

    return data


def part1(data):
    count = 0

    for entry in data:
        occurence = entry.password.count(entry.letter)
        if entry.low <= occurence <= entry.high:
            count += 1

    return count


def part2(data):
    count = 0

    for entry in data:
        if (entry.password[entry.low-1] == entry.letter) and (entry.password[entry.high-1] != entry.letter):
            count += 1
        elif (entry.password[entry.high-1] == entry.letter) and (entry.password[entry.low-1] != entry.letter):
            count += 1

    return count


data = load_data("02/input.txt")
count = part1(data)
print(count)

another_count = part2(data)
print(another_count)
