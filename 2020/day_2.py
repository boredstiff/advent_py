import unittest
from typing import List

from utils import read_data


def calculate_part_1(data: List[str]) -> int:
    results = 0

    for entry in data:
        tokens = entry.split(' ')
        minimum, maximum = tokens[0].split('-')
        value = tokens[1][0]
        password = tokens[2]
        if int(minimum) <= password.count(value) <= int(maximum):
            results += 1
    return results


def calculate_part_2(data: List[str]) -> int:
    results = 0
    for entry in data:
        tokens = entry.split(' ')
        first, second = tokens[0].split('-')
        first = int(first) - 1
        second = int(second) - 1
        value = tokens[1][0]
        password = tokens[2]
        if password[first] == value and password[second] != value:
            results += 1
        elif password[first] != value and password[second] == value:
            results += 1
    return results


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_data = [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc',
        ]

    def test_part_1(self):
        result = calculate_part_1(self.input_data)
        self.assertEqual(2, result)

    def test_part_2(self):
        result = calculate_part_2(self.input_data)
        self.assertEqual(1, result)


if __name__ == '__main__':
    input_data = read_data('day_2', year=2020)
    part_1_data = calculate_part_1(input_data)
    print(f'Part 1: {part_1_data}')
    part_2_data = calculate_part_2(input_data)
    print(f'Part 2: {part_2_data}')
