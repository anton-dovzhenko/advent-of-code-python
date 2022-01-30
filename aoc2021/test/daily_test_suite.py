import unittest
from aoc2021.day_01 import Solution


class AoC2021Tests(unittest.TestCase):

    def test_day_01(self):
        self.assertEqual(7, Solution().parse_and_solve_p1("../input/day_01_test.in"))
        self.assertEqual(1228, Solution().parse_and_solve_p1("../input/day_01.in"))
        self.assertEqual(5, Solution().parse_and_solve_p2("../input/day_01_test.in"))
        self.assertEqual(1257, Solution().parse_and_solve_p2("../input/day_01.in"))
