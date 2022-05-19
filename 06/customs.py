"""
Day 6: Custom Customs
https://adventofcode.com/2020/day/6
"""


def load_data(filename="06/test_input.txt"):
    with open(filename) as f:
        data = [segment for segment in f.read().strip("\n").split("\n\n")]
    return data


def part1(data):
    count = 0
    for group in data:
        count += len(set(group.replace("\n", "")))
    return count


def part2(data):
    count = 0
    for group in data:
        forms = group.split("\n")   
        # Cheating
        # https://stackoverflow.com/questions/70480885/find-common-character-in-list-of-strings
        # count += len(set.intersection(*map(set, forms)))
        # This one works better for my brain
        count += len(set.intersection(*[set(form) for form in forms]))
    return count


test_data = load_data()
test_count = part1(test_data)
assert test_count == 11, "Part 1 does not work with test data"

# Part 1
data = load_data("06/input.txt")
count = part1(data)
print(count)


# Part 2
test_count = part2(test_data)
assert test_count == 6, "Part 2 does not work with test data"

count = part2(data)
print(count)
