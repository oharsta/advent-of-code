from unittest import TestCase

from base import read_lines

"""
Rock (A X) defeats Scissors (C Z), Scissors (C Z) defeats Paper (B Y), and Paper (B Y) defeats Rock (A X)
1 for Rock (X), 2 for Paper (Y), and 3 for Scissors (Z)
0 if you lost, 3 if the round was a draw, and 6 if you won
"""
score_dict = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3
}


class TestRockPaperScissors(TestCase):

    def test_max_score(self):
        lines = read_lines("day2_rock_paper_scissors/input.txt")
        score = 0
        for line in lines:
            score += score_dict[line.strip()]
        self.assertEqual(15632, score)

        # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
        score = 0
        for line in [l.strip() for l in lines]:
            his = line[0]
            strategy = line[2]
            if strategy == "X":
                mine = "Z" if his == "A" else "Y" if his == "C" else "X"
            elif strategy == "Y":
                mine = "X" if his == "A" else "Z" if his == "C" else "Y"
            else:
                mine = "X" if his == "C" else "Z" if his == "B" else "Y"
            outcome = f"{his} {mine}"
            score += score_dict[outcome]
        self.assertEqual(14416, score)
