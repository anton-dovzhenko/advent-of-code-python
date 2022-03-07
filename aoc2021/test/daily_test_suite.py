import unittest
from aoc2021 import day_01, day_02, day_03


class AoC2021Tests(unittest.TestCase):

    def test_day_01(self):
        self.assertEqual(7, day_01.Solution().parse_and_solve_p1("../input/day_01_test.in"))
        self.assertEqual(1228, day_01.Solution().parse_and_solve_p1("../input/day_01.in"))
        self.assertEqual(5, day_01.Solution().parse_and_solve_p2("../input/day_01_test.in"))
        self.assertEqual(1257, day_01.Solution().parse_and_solve_p2("../input/day_01.in"))

    def test_day_02(self):
        self.assertEqual(150, day_02.Solution().parse_and_solve_p1("../input/day_02_test.in"))
        self.assertEqual(1524750, day_02.Solution().parse_and_solve_p1("../input/day_02.in"))
        self.assertEqual(900, day_02.Solution().parse_and_solve_p2("../input/day_02_test.in"))
        self.assertEqual(1592426537, day_02.Solution().parse_and_solve_p2("../input/day_02.in"))

    def test_day_03(self):
        self.assertEqual(198, day_03.Solution().parse_and_solve_p1("../input/day_03_test.in"))
        self.assertEqual(749376, day_03.Solution().parse_and_solve_p1("../input/day_03.in"))
        self.assertEqual(230, day_03.Solution().parse_and_solve_p2("../input/day_03_test.in"))
        self.assertEqual(2372923, day_03.Solution().parse_and_solve_p2("../input/day_03.in"))


