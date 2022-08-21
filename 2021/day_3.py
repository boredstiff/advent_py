import unittest
from statistics import mode
from utils import read_data
from typing import List


def calculate_part_1(input_data: List[str]) -> int:
    gamma = ''
    collection: List[List[int]] = []
    # Fill up with empty arrays
    [collection.append([]) for x in input_data[0].strip()]
    for row in input_data:
        # It's a string, so loop through it
        for index, value in enumerate(row.strip()):
            collection[index].append(int(value))

    for each_collection in collection:
        most_common = mode(each_collection)
        gamma += str(most_common)

    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    return int(gamma, 2) * int(epsilon, 2)


class UnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = [
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010',
        ]

    def test_part_1(self):
        self.assertEqual(calculate_part_1(self.test_data), 198)

    def test_part_2(self):
        pass


if __name__ == '__main__':
    data = read_data('day_3')
    part_1_data = calculate_part_1(data)
    print('Part 1: ', part_1_data)
