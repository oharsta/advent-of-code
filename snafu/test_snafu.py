from unittest import TestCase

from snafu.snafu import length_of_snafu


class TestSnafu(TestCase):

    def test_length_of_snafu(self):
        turning_points = {2: 1, 12: 2, 62: 3, 312: 4, 1562: 5, 7812: 6, 39062: 7, 195312: 8, 976562: 9, 4882812: 10,
                  24414062: 11, 122070312: 12, 610351562: 13, 3051757812: 14, 15258789062: 15}
        for k, v in turning_points.items():
            self.assertEqual(length_of_snafu(k), v)
            self.assertEqual(length_of_snafu(k + 1), v + 1)
