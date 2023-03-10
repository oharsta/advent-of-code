from unittest import TestCase

from src.base import read_lines


class TestCalories(TestCase):

    def test_max_calories(self):
        lines = read_lines("day1_calories/input.txt")
        results = []
        rucksack = []
        for line in [line.strip() for line in lines]:
            if line:
                nbr = int(line.strip())
                rucksack.append(nbr)
            else:
                results.append(sum(rucksack))
                rucksack.clear()

        max_calories = max(results)
        self.assertEqual(68775, max_calories)

        sorted_calories = sorted(results)
        top_three = sorted_calories[-1] + sorted_calories[-2] + sorted_calories[-3]
        self.assertEqual(202585, top_three)
