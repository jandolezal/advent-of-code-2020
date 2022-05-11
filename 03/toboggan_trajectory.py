"""
Day 3: Toboggan Trajectory
https://adventofcode.com/2020/day/3
"""

def load_data(filename = '03/test_input.txt'):
    with open(filename) as f:
        raw_lines = [line.strip() for line in f.readlines()]
        data = [[0 if char == "." else 1 for char in line] for line in raw_lines]
    return data



def part1(data):
    num_rows = len(data)
    num_cols = len(data[0])
    col = 0
    count = 0

    for row in range(1, num_rows):
        col += 3
        try:
            char = data[row][col]
        except IndexError:
            col -= num_cols
            char = data[row][col]
        if char == 1:
            count += 1

    return count

data = load_data()
count = part1(data)
assert count == 7, "Part 1 does not work on test data"

data = load_data("03/input.txt")
count = part1(data)
print(count)
