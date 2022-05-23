"""
Day 7: Handy Haversacks
https://adventofcode.com/2020/day/7
"""


from collections import defaultdict


def load_data(filename="07/test_input.txt"):
    with open(filename) as f:
        raw_lines = [line.strip(".\n") for line in f.readlines()]
        data = defaultdict(set)
        for line in raw_lines:
            raw_outer, raw_inner = line.split(" contain ")
            outer = raw_outer.replace(" bags", "")
            inner = [inner.split(" ", maxsplit=1)[1].replace(" bags", "").replace(" bag", "") for inner in raw_inner.split(", ") if inner != "no other bags"]
            data[outer].update(inner)
        return data


def part1(data):
    containers = set()

    while True:
        past_length = len(containers)
        for outer, inner in data.items():
            if "shiny gold" in inner or containers & inner:
                containers.add(outer)
        if len(containers) == past_length:
            break

    return containers


test_data = load_data()

containers = part1(test_data)
assert len(containers) == 4, "Part 1 does not work on test data"

data = load_data("07/input.txt")
containers = part1(data)
print(len(containers))
