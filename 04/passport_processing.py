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


def is_valid(passport, advanced=False):
    present_keys = passport.keys()

    # Part 1 conditions
    all_present = len(present_keys) == len(FIELDS)
    all_present_exc_cid = len(present_keys) == len(FIELDS) - 1 and ("cid" not in present_keys)

    if all_present or all_present_exc_cid:
        if not advanced: 
            return True
        else:
            # Part 2 conditions
            if (
                passport["byr"].isdigit() and 1920 <= int(passport["byr"]) <= 2002 and 
                passport["iyr"].isdigit() and 2010 <= int(passport["iyr"]) <= 2020 and
                passport["eyr"].isdigit() and 2020 <= int(passport["eyr"]) <= 2030 and
                ((re.fullmatch(r"^\d+cm$", passport["hgt"]) and 150 <= int(passport["hgt"].strip("cm")) <= 193) or
                (re.fullmatch(r"^\d+in$", passport["hgt"]) and 59 <= int(passport["hgt"].strip("in")) <= 76)) and
                re.fullmatch(r"^#([a-f|0-9]{6})", passport["hcl"]) and
                passport["ecl"] in "amb blu brn gry grn hzl oth".split() and len(passport["ecl"]) == 3 and
                re.fullmatch("\d{9}", passport["pid"])
            ):
                return True
            else:
                return False
    else:
        return False


def part1(data):
    count = 0
    for passport in data:
        if is_valid(passport):
            count += 1
    return count


def part2(data):
    count = 0
    for passport in data:
        if is_valid(passport, advanced=True):
            count += 1
    return count


test_data = load_data()
count = part1(test_data)
assert count == 2, "Part 1 does not work with test data"


data = load_data("04/input.txt")
count = part1(data)
print(count)

count_advanced = part2(data)
print(count_advanced)
