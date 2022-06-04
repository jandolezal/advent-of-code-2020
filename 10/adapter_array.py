'''
Day 10: Adapter Array
https://adventofcode.com/2020/day/10
'''

from math import comb, prod
from collections import Counter
from typing import List


def load_data(filename: str = '10/test_input.txt') -> List[int]:
    with open(filename) as f:
        data = [int(line.strip('\n')) for line in f.readlines()]
        data = [0] + data + [max(data) + 3]
        return sorted(data)


def gather_differences(data: List[int]) -> List[int]:
    return [data[i + 1] - data[i] for i in range(len(data) - 1)]


def compute_combinations(n: int) -> int:
    '''Return number of possible removals of one(s) from group of at least two ones.'''
    if n > 1:
        # Remove none, one or two ones from the group and sum these combinations together
        return sum(comb(n - 1, i) for i in range(3))
    return 0


def find_ones(data: List[int]) -> List[int]:
    '''Find groups of ones and return list with lengths of these ones subgroups.'''
    ones = []
    count = 0

    for i in range(len(data)):
        if data[i] == 1:
            count += 1
        else:
            if count > 0:
                ones.append(count)
            count = 0

    return ones


def part1(data: List[int]) -> int:
    differences = gather_differences(data)
    counts = Counter(differences)
    product = counts[1] * counts[3]
    return product


def part2(data) -> int:
    # Start again with list of differences between numbers in the list
    differences = [data[i + 1] - data[i] for i in range(len(data) - 1)]
    # Find all combinations how to remove one(s) for single group of ones within the list
    single_combinations = []

    for count in find_ones(differences):
        single_combination = compute_combinations(count)
        if single_combination > 0:
            single_combinations.append(single_combination)

    # Multiple single combinations together
    return prod(single_combinations)


# Part 1
test_data = load_data('10/another_test_input.txt')
test_product = part1(test_data)
assert test_product == 220, 'Part 1 does not work on the longer test data.'

data = load_data('10/input.txt')
product = part1(data)
print(product)


# Part 2
test_product = part2(test_data)
assert test_product == 19_208, 'Part 2 does not work with longer test data.'
product = part2(data)
print(product)
