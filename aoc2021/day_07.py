import sys

import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        s = self.parse(filename)
        fuel = sys.maxsize
        for i in range(s[0], 1 + s[-1]):
            fuel = min(fuel, np.sum(np.abs(s - i)))
        return fuel

    def parse_and_solve_p2(self, filename):
        s = self.parse(filename)
        fuel = sys.maxsize
        for i in range(s[0], 1 + s[-1]):
            fuel = min(fuel, int(sum(map(lambda x: (1 + x) * x / 2, np.abs(s - i)))))
        return fuel

    def parse(self, filename):
        with open(filename) as f:
            return np.array(sorted([int(i) for i in f.read().split(',')]))

