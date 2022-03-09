import re
import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        nums, boards = self.parse(filename)
        for n in nums:
            for b in boards:
                np.place(b, b == n, 0)
                if np.any(0 == np.sum(b, 0)) or np.any(0 == np.sum(b, 1)):
                    return np.sum(b) * n

    def parse_and_solve_p2(self, filename):
        nums, boards = self.parse(filename)
        score = None
        for n in nums:
            next_boards = []
            for b in boards:
                np.place(b, b == n, 0)
                if np.any(0 == np.sum(b, 0)) or np.any(0 == np.sum(b, 1)):
                    score = np.sum(b) * n
                else:
                    next_boards.append(b)
            boards = next_boards
        return score

    def parse(self, filename):
        def parse_row(x):
            return [int(n) for n in re.split('\\s+', x.strip())]
        with open(filename) as f:
            s = f.read().split("\n\n")
            n = [int(x) for x in s[0].split(',')]
            boards = []
            for i in range(1, len(s)):
                boards.append(np.array([parse_row(b) for b in s[i].split('\n')]))
            return n, boards

