import os
import unittest


def read_data() -> list[list[int]]:
    with open(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(
                        os.path.dirname(__file__)), '2022/input_data', 'day_1.txt'))
    ) as reader:
        current_elf = []
        elves = []
        for line in reader:
            if line != "\n":
                current_elf.append(int(line))
            else:
                elves.append(current_elf)
                current_elf = []
        return elves


def calculate_part_1(data: list[list[int]]) -> int:
    return sorted([sum(x) for x in data])[-1]


def calculate_part_2(data: list[list[int]]) -> int:

    sort = sorted([sum(x) for x in data])
    result = sort[-3:]
    return sum(result)


class UnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

"""

    def read_test_data(self):
        current_elf = []
        elves = []

        for line in self.test_data.split('\n'):
            if line != "":
                current_elf.append(int(line))
            else:
                elves.append(current_elf)
                current_elf = []
        return elves

    def test_part_1(self):
        assert calculate_part_1(self.read_test_data()) == 24000

    def test_part_2(self):
        assert calculate_part_2(self.read_test_data()) == 45000


if __name__ == '__main__':
    input_data = read_data()
    part_1_answer = calculate_part_1(input_data)
    print(f'Part 1 answer: {part_1_answer}')
    part_2_answer = calculate_part_2(input_data)
    print(f'Part 2 answer: {part_2_answer}')
