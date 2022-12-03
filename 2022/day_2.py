import os
import unittest

from utils import read_data


def calculate_part_1(data: list[str]) -> int:
    player_rock_value = 1
    player_paper_value = 2
    player_scissors_value = 3

    lose = 0
    draw = 3
    win = 6

    score = 0
    for each_round in data:
        opponent, player = each_round.split(' ')
        player = player.strip()

        match opponent:
            case 'A':  # Opponent Rock
                match player:
                    case 'X':  # Player Rock
                        score += draw + player_rock_value
                    case 'Y':  # Player Paper
                        score += win + player_paper_value
                    case 'Z':  # Player Scissors
                        score += lose + player_scissors_value
            case 'B':  # Opponent Paper
                match player:
                    case 'X':  # Player Rock
                        score += lose + player_rock_value
                    case 'Y':  # Player Paper
                        score += draw + player_paper_value
                    case 'Z':  # Player Scissors
                        score += win + player_scissors_value
            case 'C':  # Opponent Scissors
                match player:
                    case 'X':  # Player Rock
                        score += win + player_rock_value
                    case 'Y':  # Player Paper
                        score += lose + player_paper_value
                    case 'Z':  # Player Scissors
                        score += draw + player_scissors_value
    return score


def calculate_part_2(data: list[str]) -> int:
    player_rock_value = 1
    player_paper_value = 2
    player_scissors_value = 3

    lose = 0
    draw = 3
    win = 6

    score = 0
    for each_round in data:
        opponent, player = each_round.split(' ')
        player = player.strip()

        match opponent:
            case 'A':  # Opponent Rock
                match player:
                    case 'X':  # Need to lose
                        score += lose + player_scissors_value
                    case 'Y':  # Need to draw
                        score += draw + player_rock_value
                    case 'Z':  # Need to win
                        score += win + player_paper_value
            case 'B':  # Opponent Paper
                match player:
                    case 'X':  # Need to lose
                        score += lose + player_rock_value
                    case 'Y':  # Need to draw
                        score += draw + player_paper_value
                    case 'Z':  # Need to win
                        score += win + player_scissors_value
            case 'C':  # Opponent Scissors
                match player:
                    case 'X':  # Need to lose
                        score += lose + player_paper_value
                    case 'Y':  # Need to draw
                        score += draw + player_scissors_value
                    case 'Z':  # Need to win
                        score += win + player_rock_value
    return score


class UnitTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = [
            'A Y',
            'B X',
            'C Z',
        ]

    def test_part_1(self):
        assert calculate_part_1(self.test_data) == 15

    def test_part_2(self):
        assert calculate_part_2(self.test_data) == 12


if __name__ == '__main__':
    input_data = read_data('day_2', year=2022)
    part_1_answer = calculate_part_1(input_data)
    print(f'Part 1 answer: {part_1_answer}')
    part_2_answer = calculate_part_2(input_data)
    print(f'Part 2 answer: {part_2_answer}')
