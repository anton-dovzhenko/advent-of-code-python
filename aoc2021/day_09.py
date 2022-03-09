from functools import reduce
from operator import mul


class Solution:

    def parse_and_solve_p1(self, filename):
        matrix = self.parse(filename)
        risk = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                m = 9
                if i > 0:
                    m = min(m, matrix[i - 1][j])
                if i < len(matrix) - 1:
                    m = min(m, matrix[i + 1][j])
                if j > 0:
                    m = min(m, matrix[i][j - 1])
                if j < len(matrix[i]) - 1:
                    m = min(m, matrix[i][j + 1])
                if matrix[i][j] < m:
                    risk += 1 + matrix[i][j]
        return risk

    def parse_and_solve_p2(self, filename):
        matrix = self.parse(filename)
        areas = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                area = self._visit(matrix, i, j)
                areas.append(area)
        areas.sort()
        return reduce(mul, areas[-3:], 1)

    def _visit(self, matrix, i, j):
        if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[i]):
            return 0
        if matrix[i][j] == 9:
            return 0
        matrix[i][j] = 9
        return 1 + self._visit(matrix, i - 1, j) + self._visit(matrix, i + 1, j) + \
               self._visit(matrix, i, j - 1) + self._visit(matrix, i, j + 1)

    def parse(self, filename):
        with open(filename) as f:
            return [list(map(int, list(line.strip()))) for line in f.readlines()]

