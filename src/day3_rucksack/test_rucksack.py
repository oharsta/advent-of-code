from unittest import TestCase

from src.base import read_lines


class TestRucksack(TestCase):

    def test_priorities(self):
        lines = read_lines("day3_rucksack/input.txt")
        priorities = {**{chr(nbr): index + 1 for index, nbr in enumerate(range(ord("a"), ord("z") + 1))},
                      **{chr(nbr): index + 27 for index, nbr in enumerate(range(ord("A"), ord("Z") + 1))}}
        sum_priorities = 0
        for line in [line.strip() for line in lines]:
            line_length = int(len(line) / 2)
            part1 = line[0:line_length]
            part2 = line[line_length:]
            items = [char for char in part1 if char in part2]
            sum_priorities += priorities[items[0]]

        self.assertEqual(8298, sum_priorities)

        sum_priorities = 0
        rucksacks = []
        for index, line in enumerate([line.strip() for line in lines]):
            rucksacks.append(line)
            if (index + 1) % 3 == 0:
                items = [char for char in rucksacks[0] if char in rucksacks[1] and char in rucksacks[2]]
                sum_priorities += priorities[items[0]]
                rucksacks.clear()

        self.assertEqual(2708, sum_priorities)
