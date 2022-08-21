import os
from typing import List
import unittest


def calculate_part_1(data: List[int]) -> int:
    increment = 0

    for index, value in enumerate(data):
        if index > 0:
            if data[index - 1] < value:
                increment += 1
    return increment


def calculate_part_2(data: List[int]) -> int:
    measurement_windows = []
    for index, value in enumerate(data):
        sum_value = value
        try:
            second_index = data[index + 1]
            sum_value += second_index
        except IndexError:
            continue

        try:
            third_index = data[index + 2]
            sum_value += third_index
        except IndexError:
            continue

        measurement_windows.append(sum_value)

    return calculate_part_1(measurement_windows)


def read_data_part_1():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'input_data', 'day_1.txt'))) as reader:
        return [int(i) for i in reader.readlines()]


class UnitTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263,
        ]

    def test_part_1(self):
        assert calculate_part_1(self.test_data) == 7

    def test_part_2(self):
        result = calculate_part_2(self.test_data)
        print(result)
        assert(result == 5)


if __name__ == '__main__':
    input_data = read_data_part_1()
    part_1_answer = calculate_part_1(input_data)
    print('Part 1: ', part_1_answer)
    part_2_answer = calculate_part_2(input_data)
    print('Part 2: ', part_2_answer)
