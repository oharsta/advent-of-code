from unittest import TestCase

from base import read_lines


class TestCalories(TestCase):

    def test_max_calories(self):
        input = read_lines("calories/input.txt")
        results = {}
        for line in input:
            i = len(results)
            new_line = line == "\n"
            nbr = int(line.replace("\n", "")) if not new_line else 0
            if new_line:
                results[i + 1] = 0
            elif i in results:
                results[i] = results[i] + nbr
            else:
                results[i + 1] = nbr
        max_calories = max(results.values())
        self.assertEqual(68775, max_calories)
