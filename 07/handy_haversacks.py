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


def load_data_part2(filename="07/test_input.txt"):
    with open(filename) as f:
        raw_lines = [line.strip(".\n") for line in f.readlines()]
        data = defaultdict(set)
        for line in raw_lines:
            raw_outer, raw_inner = line.split(" contain ")
            inner = {}
            for inner in raw_inner.split(", "):
                count, bag = inner.split(" ", maxsplit=1)
                bag = (count, bag.replace(" bags", "").replace(" bag", ""))
                if bag[0] != "no":
                    data[raw_outer.replace(" bags", "")].add((int(bag[0]), bag[1]))
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


def part2(data, target, count=0):
    if target not in data:
        return 1
    else:
        for num, color in data[target]:
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
test_data = load_data_part2("07/test_input.txt")

data = load_data_part2("07/input.txt")

test_sum = part2(test_data, "shiny gold")
assert test_sum == 32, "Part 2 does not work with test data"

count = part2(data, "shiny gold")
print(count)
