"""
Day 2: Password Philosophy
https://adventofcode.com/2020/day/2
"""


def load_data(filename="02/test_input.txt"):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

        data = []
        for line in lines:
            interval, letter, password = line.split()
            letter = letter.strip(":")
            low, high = [int(part) for part in interval.split("-")]
            data.append(
                dict(letter=letter, low=low, high=high, password=password)
            )

    return data



def part1(data):
    count = 0
    for line in data:
        occurence = line["password"].count(line["letter"])
        if (occurence >= line["low"]) and (occurence <= line["high"]):
            count += 1
    return count


def part2(data):
    count = 0
    for line in data:
        if (line["letter"] == line["password"][line["low"] - 1]) and (line["letter"] == line["password"][line["high"] - 1]):
            continue
        elif (line["letter"] != line["password"][line["low"] - 1]) and (line["letter"] != line["password"][line["high"] - 1]):
            continue
        else:
            count += 1
    return count


data = load_data("02/input.txt")
count = part1(data)
print(count)

another_count = part2(data)
print(another_count)
