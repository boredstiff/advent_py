import string
import unittest

from utils import read_data


def calculate_common_letters(common_letters: list[str]):
    result = 0
    for letter in common_letters:
        lowercase_match = string.ascii_lowercase.find(letter)
        if lowercase_match > 0:
            result += lowercase_match + 1
        uppercase_match = string.ascii_uppercase.find(letter)
        if uppercase_match > 0:
            result += uppercase_match + 27
    return result


def calculate_part_1(data: list[str]) -> int:
    result = 0
    for rucksack in data:
        halfway = len(rucksack) // 2
        first_compartment, second_compartment = rucksack[:halfway], rucksack[halfway:]
        common_letters = list(set(first_compartment) & set(second_compartment))
        result += calculate_common_letters(common_letters)
    return result


def calculate_part_2(data: list[str]) -> int:
    result = 0
    groups = [data[y: y + 3] for y in range(0, len(data), 3)]
    for group in groups:
        first_rucksack, second_rucksack, third_rucksack = group
        common_letters = list(set(first_rucksack) & set(second_rucksack) & set(third_rucksack))
        result += calculate_common_letters(common_letters)

    return result


class UnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]

    def test_part_1(self):
        assert calculate_part_1(self.test_data) == 157

    def test_part_2(self):
        assert calculate_part_2(self.test_data) == 70


if __name__ == '__main__':
    input_data = read_data('day_3', year=2022)
    part_1_answer = calculate_part_1(input_data)
    print(f'Part 1 answer: {part_1_answer}')
    part_2_answer = calculate_part_2(input_data)
    print(f'Part 2 answer: {part_2_answer}')
