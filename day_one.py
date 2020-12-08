from functools import reduce
from itertools import combinations


def get_numbers():
    with open('sample.txt') as f:
        data = f.readlines()
    data = [float(x.strip()) for x in data]
    return data

# PART A


def part_one(sample):
    const = 2020
    for i in sample:
        if (const - i) in sample:
            return (const - i) * i


print(part_one(get_numbers()))

# PART B


def part_two(sample):
    const = 2020
    for var in combinations(sample, 3):
        if sum(var) == const:
            return reduce(lambda x, y: x * y, var)


print(part_two(get_numbers()))
