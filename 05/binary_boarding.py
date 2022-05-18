"""
Day 5: Binary Boarding
https://adventofcode.com/2020/day/5
"""

from json import load


def load_data(filename="05/test_input.txt"):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def search(instructions, rows=True):
    if rows:
        instructions = instructions[:7]
        low = 0
        high = 127
    else:
        instructions = instructions[7:]
        low = 0
        high = 7

    for letter in instructions:
        if letter == "F" or letter == "L":
            high = low + (high - low) // 2
        elif letter == "B" or letter == "R":
            low = high - (high - low) // 2

    return low


def part1(data):
    rows = []
    cols = []
    ids = []

    for instructions in data:
        row = search(instructions)
        col = search(instructions, rows=False)
        id_ = row * 8 + col

        rows.append(row)
        cols.append(col)
        ids.append(id_)
    
    return sorted(ids, reverse=True)


test_data = load_data()
result = part1(test_data)
assert result[0] == 820, "Keep trying"


data = load_data("05/input.txt")
ids_list = part1(data)
print(ids_list[0])
