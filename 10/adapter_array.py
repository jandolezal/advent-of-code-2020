'''
Day 10: Adapter Array
https://adventofcode.com/2020/day/10
'''

from collections import Counter


def load_data(filename='10/test_input.txt'):
    with open(filename) as f:
        data = [int(line.strip('\n')) for line in f.readlines()]
        data = [0] + data + [max(data) + 3]
        return sorted(data)


def part1(data):
    differences = [data[i + 1] - data[i] for i in range(len(data) - 1)]
    counts = Counter(differences)
    product = counts[1] * counts[3]
    return product


# Part 1
test_data = load_data('10/another_test_input.txt')
test_product = part1(test_data)
assert test_product == 220, 'Part 1 does not work on the longer test data.'

data = load_data('10/input.txt')
product = part1(data)
print(product)
