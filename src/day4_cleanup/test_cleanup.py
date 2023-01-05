from unittest import TestCase

from src.base import read_lines


class TestCleanup(TestCase):

    def test_cleanup(self):
        def ranges(line):
            range = line.split(",")
            return [int(s) for s in range[0].split("-")], [int(s) for s in range[1].split("-")]

        def fully_contains(line):
            first_range, second_range = ranges(line)
            return (first_range[0] >= second_range[0] and first_range[1] <= second_range[1]) or (
                    second_range[0] >= first_range[0] and second_range[1] <= first_range[1])

        def partial_overlaps(line):
            first_range, second_range = ranges(line)
            return not (first_range[1] < second_range[0] or first_range[0] > second_range[1])

        lines = read_lines("day4_cleanup/input.txt")
        outcome = len([line for line in lines if fully_contains(line.strip())])
        self.assertEqual(466, outcome)

        outcome = len([line for line in lines if partial_overlaps(line.strip())])
        self.assertEqual(865, outcome)
