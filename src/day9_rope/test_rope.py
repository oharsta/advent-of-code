from unittest import TestCase

from src.base import read_lines


class TestRope(TestCase):

    def test_rope(self):
        moves = [(move[0], int(move[2])) for move in [line.strip() for line in read_lines("day9_rope/input.txt")]]
        directions = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
        tail_positions = set()
        tail, head = (0, 0), (0, 0)
        tail_positions.add((0, 0))
        for move in moves:
            direction = directions[move[0]]
            for _ in range(move[1]):
                head = (head[0] + direction[0], head[1] + direction[1])
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = (tail[0], tail[1])
