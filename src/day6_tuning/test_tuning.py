from unittest import TestCase

from src.base import read_lines


class TestTuning(TestCase):

    def test_tuning(self):
        line = read_lines("day6_tuning/input.txt")[0].strip()
        for marker_length, answer in {4: 1210, 14: 3476}.items():
            unique_values = ""
            for index, val in enumerate(line):
                if val in unique_values:
                    unique_values = unique_values[unique_values.index(val) + 1:]
                unique_values += val
                if len(unique_values) == marker_length:
                    break

            self.assertEqual(answer, index + 1)
