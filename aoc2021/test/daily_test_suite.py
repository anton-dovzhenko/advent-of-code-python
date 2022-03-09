import unittest
from aoc2021 import day_01, day_02, day_03, day_04, day_05, day_06, day_07, day_08, day_09, day_10


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

    def test_day_04(self):
        self.assertEqual(4512, day_04.Solution().parse_and_solve_p1("../input/day_04_test.in"))
        self.assertEqual(45031, day_04.Solution().parse_and_solve_p1("../input/day_04.in"))
        self.assertEqual(1924, day_04.Solution().parse_and_solve_p2("../input/day_04_test.in"))
        self.assertEqual(2568, day_04.Solution().parse_and_solve_p2("../input/day_04.in"))

    def test_day_05(self):
        self.assertEqual(5, day_05.Solution().parse_and_solve_p1("../input/day_05_test.in"))
        self.assertEqual(6548, day_05.Solution().parse_and_solve_p1("../input/day_05.in"))
        self.assertEqual(12, day_05.Solution().parse_and_solve_p2("../input/day_05_test.in"))
        self.assertEqual(19663, day_05.Solution().parse_and_solve_p2("../input/day_05.in"))

    def test_day_06(self):
        self.assertEqual(26, day_06.Solution().solve("../input/day_06_test.in", 18))
        self.assertEqual(5934, day_06.Solution().solve("../input/day_06_test.in", 80))
        self.assertEqual(26984457539, day_06.Solution().solve("../input/day_06_test.in", 256))
        self.assertEqual(386640, day_06.Solution().solve("../input/day_06.in", 80))
        self.assertEqual(1733403626279, day_06.Solution().solve("../input/day_06.in", 256))

    def test_day_07(self):
        self.assertEqual(37, day_07.Solution().parse_and_solve_p1("../input/day_07_test.in"))
        self.assertEqual(335271, day_07.Solution().parse_and_solve_p1("../input/day_07.in"))
        self.assertEqual(168, day_07.Solution().parse_and_solve_p2("../input/day_07_test.in"))
        self.assertEqual(95851339, day_07.Solution().parse_and_solve_p2("../input/day_07.in"))

    def test_day_08(self):
        self.assertEqual(26, day_08.Solution().parse_and_solve_p1("../input/day_08_test.in"))
        self.assertEqual(239, day_08.Solution().parse_and_solve_p1("../input/day_08.in"))
        self.assertEqual(61229, day_08.Solution().parse_and_solve_p2("../input/day_08_test.in"))
        self.assertEqual(946346, day_08.Solution().parse_and_solve_p2("../input/day_08.in"))

    def test_day_09(self):
        self.assertEqual(15, day_09.Solution().parse_and_solve_p1("../input/day_09_test.in"))
        self.assertEqual(425, day_09.Solution().parse_and_solve_p1("../input/day_09.in"))
        self.assertEqual(1134, day_09.Solution().parse_and_solve_p2("../input/day_09_test.in"))
        self.assertEqual(1135260, day_09.Solution().parse_and_solve_p2("../input/day_09.in"))

    def test_day_10(self):
        self.assertEqual(26397, day_10.Solution().parse_and_solve_p1("../input/day_10_test.in"))
        self.assertEqual(240123, day_10.Solution().parse_and_solve_p1("../input/day_10.in"))
        self.assertEqual(288957, day_10.Solution().parse_and_solve_p2("../input/day_10_test.in"))
        self.assertEqual(3260812321, day_10.Solution().parse_and_solve_p2("../input/day_10.in"))
