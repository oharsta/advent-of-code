import re
from unittest import TestCase

from src.base import read_lines


class TestCleanup(TestCase):

    def test_cleanup(self):
        self.do_cleanup(True)
        self.do_cleanup(False)

    def do_cleanup(self, all_at_once):
        def parse_move(s):
            return [int(group) for group in re.search(r"move (\d+) from (\d+) to (\d+)", s).groups()]

        crates_dict = {}
        lines = read_lines("day5_supply_stacks/input.txt")
        result = ""
        for line in [line for line in lines if "[" in line]:
            for index, crate in enumerate([line[i:i + 4].strip() for i in range(0, len(line.rstrip()), 4)]):
                if crate.strip():
                    crates = crates_dict.get(index + 1, [])
                    crates.append(crate[1:2])
                    crates_dict[index + 1] = crates
        for line in crates_dict.values():
            line.reverse()
        for line in [line.strip() for line in lines if "move" in line]:
            moves, origin, destination = parse_move(line)
            origin_val = crates_dict[origin]
            if all_at_once:
                crates_dict[destination] += origin_val[len(origin_val) - moves:len(origin_val)]
                crates_dict[origin] = origin_val[0: len(origin_val) - moves]
            else:
                for _ in range(0, moves):
                    crates_dict[destination].append(origin_val.pop())
        for k in range(len(crates_dict)):
            result += crates_dict[k + 1][-1]
        self.assertEqual("MHQTLJRLB" if all_at_once else "RLFNRTNFB", result)
