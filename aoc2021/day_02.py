import math
from functools import reduce


class Solution:

    def __init__(self):
        self.direction = {'up': [0, -1], 'down': [0, 1], 'forward': [1, 0]}

    def parse_and_solve_p1(self, filename):
        return self.solve_p1(self.parse(filename))

    def parse_and_solve_p2(self, filename):
        return self.solve_p2(self.parse(filename))

    def solve_p1(self, moves):
        return math.prod(reduce(lambda x, y: [x[0] + y[0], x[1] + y[1]], moves))

    def solve_p2(self, moves):
        hor = 0
        depth = 0
        aim = 0
        for m in moves:
            hor += m[0]
            aim += m[1]
            depth += aim * m[0]
        return hor * depth

    def parse(self, filename):
        def line_to_move(x):
            x = x.split(" ")
            return [int(x[1]) * n for n in self.direction[x[0]]]
        with open(filename) as f:
            return [line_to_move(line) for line in f]

