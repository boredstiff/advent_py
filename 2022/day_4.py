import unittest

from utils import read_data


def calculate_part_1(data: list[str]) -> int:
    result = 0
    for pair in data:
        first, second = pair.split(',')
        first_start, first_end = [int(x) for x in first.split('-')]
        second_start, second_end = [int(x) for x in second.split('-')]
        first_sections = [n for n in range(first_start, first_end + 1)]
        second_sections = [n for n in range(second_start, second_end + 1)]
        overlapping_elements = list(set(first_sections) & set(second_sections))
        first_contained = True
        second_contained = True
        for section in first_sections:
            if section not in overlapping_elements:
                first_contained = False

        for section in second_sections:
            if section not in overlapping_elements:
                second_contained = False

        if first_contained or second_contained:
            result += 1
    return result


def calculate_part_2(data: list[str]) -> int:
    result = 0
    for pair in data:
        first, second = pair.split(',')
        first_start, first_end = [int(x) for x in first.split('-')]
        second_start, second_end = [int(x) for x in second.split('-')]
        first_sections = [n for n in range(first_start, first_end + 1)]
        second_sections = [n for n in range(second_start, second_end + 1)]
        overlapping_elements = list(set(first_sections) & set(second_sections))
        if overlapping_elements:
            result += 1
    return result


class UnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = [
            '2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8',
        ]

    def test_part_1(self):
        assert calculate_part_1(self.test_data) == 2

    def test_part_2(self):
        assert calculate_part_2(self.test_data) == 4


if __name__ == '__main__':
    input_data = read_data('day_4', year=2022)
    part_1_answer = calculate_part_1(input_data)
    print(f'Part 1 answer: {part_1_answer}')
    part_2_answer = calculate_part_2(input_data)
    print(f'Part 2 answer: {part_2_answer}')
