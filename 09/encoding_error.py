'''
Day 9: Encoding Error
https://adventofcode.com/2020/day/9
'''


def load_data(filename='09/test_input.txt'):
    with open(filename) as f:
        data = [int(line.strip('\n')) for line in f.readlines()]
    return data


def part1(data, size=5):
    for i in range(len(data)):
        preamble = data[i : i + size]
        target_num = data[i + size]

        if not any(target_num - num in preamble for num in preamble):
            return target_num


# Part 1
test_data = load_data()
wrong_num = part1(test_data, size=5)
assert wrong_num == 127, 'Part 1 does not work with test data.'

data = load_data('09/input.txt')
wrong_num = part1(data, size=25)
print(wrong_num)
