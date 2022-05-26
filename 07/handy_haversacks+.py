"""
Day 7: Handy Haversacks
https://adventofcode.com/2020/day/7
"""


from collections import defaultdict


def load_data(filename="07/test_input.txt"):
    with open(filename) as f:
        raw_lines = [line.strip(".\n") for line in f.readlines()]
        graph = defaultdict(set)
        for line in raw_lines:
            raw_parent, raw_children = line.split(" contain ")
            parent = raw_parent.replace(" bags", "")
            children = [child.split(" ", maxsplit=1)[1].replace(" bags", "").replace(" bag", "") for child in raw_children.split(", ") if child != "no other bags"]
            graph[parent].update(children)
        return graph


def part1(data):
    parents = set()
    for outer, inner in data.items():
        if "shiny gold" in inner:
            parents.add(outer)
    for outer, inner in data.items():
        if parents & inner:
            parents.add(outer)
    for outer, inner in data.items():
        if parents & inner:
            parents.add(outer)
    for outer, inner in data.items():
        if parents & inner:
            parents.add(outer)
    for outer, inner in data.items():
        if parents & inner:
            parents.add(outer)
    for outer, inner in data.items():
        if parents & inner:
            parents.add(outer)
    return parents

    


test_data = load_data()
print(test_data)

parents = part1(test_data)
print(parents)

data = load_data("07/input.txt")
parents = part1(data)
print(parents)
print(len(parents))

# not 93, 