"""
Day 3: Toboggan Trajectory
https://adventofcode.com/2020/day/3
"""

from functools import reduce
from operator import mul


def load_data(filename = '03/test_input.txt'):
    with open(filename) as f:
        raw_lines = [line.strip() for line in f.readlines()]
        data = [[0 if char == "." else 1 for char in line] for line in raw_lines]
    return data



def part1(data, row_step=1, col_step=3):
    num_rows = len(data)
    num_cols = len(data[0])
    row = 0
    col = 0

    count = 0

    while row < num_rows - 1:
        row += row_step
        col = (col + col_step) % num_cols
        char = data[row][col]
        if char == 1:
            count += 1

    return count


def part2(data):
    STEPS = [
        (1,1),
        (1,3),
        (1,5),
        (1,7),
        (2,1),
        ]
    
    tree_counts = []

    for step in STEPS:
        tree_counts.append(part1(data, *step))
    return reduce(mul, tree_counts)



test_data = load_data()

count = part1(test_data)
assert count == 7, "Part 1 does not work on test data"

product = part2(test_data)
assert product == 336, "Part 2 does not work on test data"

data = load_data("03/input.txt")
count = part1(data)
print(count)

product = part2(data)
print(product)
