"""
Day 6: Custom Customs
https://adventofcode.com/2020/day/6
"""


def load_data(filename="06/test_input.txt"):
    with open(filename) as f:
        data = [segment.replace("\n", "") for segment in f.read().strip("\n").split("\n\n")]
    return data


def part1(data):
    count = 0
    for group in data:
        count += len(set(group))
    return count


test_data = load_data()
test_count = part1(test_data)
assert test_count == 11, "Part 1 does not work with test data"

# Part 1
data = load_data("06/input.txt")
count = part1(data)
print(count)
