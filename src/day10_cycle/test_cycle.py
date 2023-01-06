from unittest import TestCase

from src.base import read_lines


class TestCycle(TestCase):

    def test_cycle(self):
        self.do_test_cycle("input.txt", 12560)
        self.do_test_cycle("test_input.txt", 13140)

    def do_test_cycle(self, input_file, expected):
        instructions = [line.strip().split() for line in read_lines(f"day10_cycle/{input_file}")]
        cycles = [220, 180, 140, 100, 60, 20]
        pixel_cycles = [240, 200, 160, 120, 80, 40]
        cycle, signal_strengths, x, drawing = 0, 0, 1, ""

        def check_pixel_point(current_cycle, all_cycles, current_drawing, current_x):
            current_drawing += "#" if (current_cycle - 1) % 40 in range(current_x - 1, current_x + 2) else "."
            if all_cycles and current_cycle == all_cycles[-1]:
                print(drawing)
                current_drawing = ""
                all_cycles.pop()
            return current_drawing

        def check_point(current_cycle, all_cycles, strengths, current_x):
            if all_cycles and current_cycle == all_cycles[-1]:
                strengths += all_cycles[-1] * current_x
                all_cycles.pop()
            return strengths

        for instruction in instructions:
            cycle += 1
            drawing = check_pixel_point(cycle, pixel_cycles, drawing, x)
            signal_strengths = check_point(cycle, cycles, signal_strengths, x)
            if instruction[0] != "noop":
                cycle += 1
                drawing = check_pixel_point(cycle, pixel_cycles, drawing, x)
                signal_strengths = check_point(cycle, cycles, signal_strengths, x)
                x += int(instruction[1])

        self.assertEqual(expected, signal_strengths)
