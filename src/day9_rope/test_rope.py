from unittest import TestCase

from src.base import read_lines


class TestRope(TestCase):

    def test_rope(self):
        def apply_move(position, move_to_apply):
            return position[0] + move_to_apply[0], position[1] + move_to_apply[1]

        def new_position(leader, follower):
            # If the head is two steps away then the tail needs to turn also
            if abs(leader[0] - follower[0]) > 1 or abs(leader[1] - follower[1]) > 1:
                if leader[0] != follower[0]:
                    follower = apply_move(follower, moves["D"] if leader[0] > follower[0] else moves["U"])
                if leader[1] != follower[1]:
                    follower = apply_move(follower, moves["R"] if leader[1] > follower[1] else moves["L"])
            return follower

        turns = [(turn[0], int(turn[2:])) for turn in [line.strip() for line in read_lines("day9_rope/input.txt")]]
        moves = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
        tail_positions = set()
        last_tail_positions = set()
        head = (0, 0)
        tails = [(0, 0) for _ in range(0, 9)]
        tail_positions.add((0, 0))
        last_tail_positions.add((0, 0))
        for turn in turns:
            move = moves[turn[0]]
            for _ in range(turn[1]):
                head = apply_move(head, move)
                tails[0] = new_position(head, tails[0])
                for i in range(1, len(tails)):
                    tails[i] = new_position(tails[i - 1], tails[i])
                tail_positions.add(tails[0])
                last_tail_positions.add(tails[8])

        self.assertEqual(5902, len(tail_positions))
        self.assertEqual(2445, len(last_tail_positions))