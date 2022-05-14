"""
Day 4: Passport Processing
https://adventofcode.com/2020/day/4
"""

import re


FIELDS = "byr iyr eyr hgt hcl ecl pid cid".split()


def load_data(filename="04/test_input.txt"):
    with open(filename) as f:
        raw_data = [re.split("\n| ", segment) for segment in f.read().strip("\n").split("\n\n")]

        data = []

        for segment in raw_data:
            data.append(dict([tuple(pair.split(":")) for pair in segment]))

    return data


def is_valid(passport):
    present_keys = passport.keys()
    if len(present_keys) == len(FIELDS):
        return True
    elif (len(present_keys) == len(FIELDS) - 1) and ("cid" not in present_keys):
        return True
    else:
        return False


def part1(data):
    count = 0
    for passport in data:
        if is_valid(passport):
            count += 1
    return count

test_data = load_data()
count = part1(test_data)
assert count == 2, "Part 1 does not work with test data"


data = load_data("04/input.txt")
count = part1(data)
print(count)
