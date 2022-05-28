"""
Day 7: Handy Haversacks
https://adventofcode.com/2020/day/7
"""


from collections import defaultdict
import re
from typing import Dict


def load_data(filename="07/test_input.txt") -> Dict[str, Dict[str, int]]:
    with open(filename) as f:
        raw_lines = [line.strip(".\n") for line in f.readlines()]

        data = defaultdict(dict)

        for line in raw_lines:
            parent = re.search(r"^\w+ \w+", line)[0]
            raw_children = re.findall(r"\d+ \w+ \w+", line)

            for child in raw_children:
                count, color = child.split(" ", maxsplit=1)
                data[parent].update({color: int(count)})

        return data


def part1(data):
    containers = set()

    while True:
        past_length = len(containers)
        for outer, inner in data.items():
            if "shiny gold" in inner.keys() or containers & set(inner.keys()):
                containers.add(outer)
        if len(containers) == past_length:
            break

    return containers


def part2(data, target, count=0):
    if target not in data:
        return 1
    else:
        for color, num in data[target].items():
            count += num * part2(data, color, count=1)
    return count


# Part 1
test_data = load_data()

containers = part1(test_data)
assert len(containers) == 4, "Part 1 does not work on test data"

data = load_data("07/input.txt")
containers = part1(data)
print(len(containers))


# Part 2
test_data = load_data("07/test_input.txt")

test_sum = part2(test_data, "shiny gold")
assert test_sum == 32, "Part 2 does not work with test data"

count = part2(data, "shiny gold")
print(count)
