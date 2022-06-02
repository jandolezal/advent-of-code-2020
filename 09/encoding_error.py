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


def part2(data, wrong_num, size=2):
    while True:
        for i in range(len(data) - size):
            current_list = data[i : i + size]
            if sum(current_list) == wrong_num:
                return min(current_list) + max(current_list)
        size += 1


# Part 1
test_data = load_data()
test_wrong_num = part1(test_data, size=5)
assert test_wrong_num == 127, 'Part 1 does not work with test data.'

data = load_data('09/input.txt')
wrong_num = part1(data, size=25)
print(wrong_num)


# Part 2
test_list = part2(test_data, test_wrong_num)
assert test_list == 62, 'Part 2 does not work with test data.'

list_ = part2(data, wrong_num)
print(list_)
