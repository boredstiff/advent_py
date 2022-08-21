from typing import List, Tuple
from utils import read_data
import unittest


def calculate_part_1(input_data: List[str]) -> int:
    horizontal_position = 0
    vertical_position = 0

    for row in input_data:
        instruction, value = row.split()
        if instruction == 'forward':
            horizontal_position += int(value)
        elif instruction == 'down':
            vertical_position += int(value)
        else:
            vertical_position -= int(value)

    return horizontal_position * vertical_position


class UnitTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2',
        ]

    def test_part_1(self):
        assert calculate_part_1(self.test_data) == 150


if __name__ == '__main__':
    data = read_data('day_2')
    part_1_data = calculate_part_1(data)
    print('Part 1: ', part_1_data)
