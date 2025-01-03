import collections
import re

import numpy as np


class Solution:

    def __init__(self):
        self.regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)')

    def parse_and_solve_p1(self, filename):
        mul_sum = 0
        data = self.parse(filename)
        for expression in self.regex.findall(data):
            mul_sum += self._eval_mul(expression)
        return mul_sum

    def parse_and_solve_p2(self, filename):
        mul_sum = 0
        data = "do()" + self.parse(filename)
        for part in data.split("don't()"):
            for part2 in part.split("do()")[1:]:
                for expression in self.regex.findall(part2):
                    mul_sum += self._eval_mul(expression)
        return mul_sum

    def _eval_mul(self, expression):
        n = expression[4:-1].split(",")
        return int(n[0]) * int(n[1])

    def parse(self, filename):
        with open(filename) as f:
            return f.read()


solution = Solution()
print("Parse test:", solution.parse('input/day_03_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_03_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_03.input'))
print("Solve 2 test:", solution.parse_and_solve_p2('input/day_03_02_test.input'))
print("Solve 2:", solution.parse_and_solve_p2('input/day_03.input'))


