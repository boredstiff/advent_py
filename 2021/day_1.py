import os
from typing import List
import unittest


def calculate(data: List[int]) -> int:
    increment = 0

    for index, value in enumerate(data):
        if index > 0:
            if data[index - 1] < value:
                increment += 1
    return increment


def read_data_part_1():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'input_data', 'day_1.txt'))) as reader:
        return [int(i) for i in reader.readlines()]


class UnitTest(unittest.TestCase):

    @staticmethod
    def test_part_1():
        data = [
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

        assert calculate(data) == 7


if __name__ == '__main__':
    part_1_data = read_data_part_1()
    part_1_answer = calculate(part_1_data)
    print(part_1_answer)