import re
import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        points = self.parse(filename)
        points_no_diagonal = []
        for p in points:
            if p[0] == p[2] or p[1] == p[3]:
                points_no_diagonal.append(p)
        return self.solve(points_no_diagonal)

    def parse_and_solve_p2(self, filename):
        points = self.parse(filename)
        return self.solve(points)

    def solve(self, points):
        cache = {}
        for p in points:
            steps = max(abs(p[0] - p[2]), abs(p[1] - p[3]))
            direction = ((p[2] - p[0]) / steps, (p[3] - p[1]) / steps)
            for s in range(steps + 1):
                point = (p[0] + direction[0] * s, p[1] + direction[1] * s)
                cache[point] = 1 + cache.get(point, 0)
        return np.sum(1 < np.fromiter(cache.values(), dtype=int))

    def parse(self, filename):
        def parse_line(x):
            return [int(n) for n in (','.join(x.split(' -> '))).split(',')]
        with open(filename) as f:
            return [parse_line(line) for line in f.readlines()]


