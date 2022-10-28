import unittest

from utils import read_data


def calculate_part_1(data: str) -> int:
    result = 0

    for each in data:
        match each:
            case '(':
                result += 1
            case ')':
                result -= 1
    return result


class UnitTest(unittest.TestCase):

    def test_part_1(self):
        assert calculate_part_1('(())') == 0
        assert calculate_part_1('()()') == 0
        assert calculate_part_1('(((') == 3
        assert calculate_part_1('(()(()(') == 3
        assert calculate_part_1('))(((((') == 3
        assert calculate_part_1('())') == -1
        assert calculate_part_1('))(') == -1
        assert calculate_part_1(')))') == -3
        assert calculate_part_1(')())())') == -3


if __name__ == '__main__':
    input_data = read_data('day_1', year=2015)
    part_1_answer = calculate_part_1(input_data[0])
    print('Part 1: ', part_1_answer)
