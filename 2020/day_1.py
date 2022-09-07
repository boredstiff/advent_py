import unittest

from typing import List

from utils import read_data


def calculate_part_1(data: List[int]) -> int:
    for first in data:
        for second in data:
            if first + second == 2020:
                return first * second
    return 0


def calculate_part_2(data: List[int]) -> int:
    for first in data:
        for second in data:
            for third in data:
                if first + second + third == 2020:
                    return first * second * third
    return 0


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.input_data = [
            1721,
            979,
            366,
            299,
            675,
            1456,
        ]

    def test_part_1(self):
        result = calculate_part_1(self.input_data)
        self.assertEqual(result, 514579)

    def test_part_2(self):
        result = calculate_part_2(self.input_data)
        self.assertEqual(result, 241861950)


if __name__ == '__main__':
    data = read_data('day_1', as_int=True, year=2020)
    part_1_data = calculate_part_1(data)
    print(f'Part 1: {part_1_data}')
    part_2_data = calculate_part_2(data)
    print(f'Part 2: {part_2_data}')
