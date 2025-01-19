import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        heights: np.array = self.parse(filename)
        starts = [{(x[0].item(), x[1].item()): 1} for x in np.argwhere(heights == 0)]
        for i in range(1, 10):
            next_starts = []
            for s in starts:
                next_dict = {}
                for p in s.keys():
                    if p[0] > 0 and heights[p[0] - 1, p[1]] == i:
                        next_dict[(p[0] - 1, p[1])] = 1
                    if p[1] > 0 and heights[p[0], p[1] - 1] == i:
                        next_dict[(p[0], p[1] - 1)] = 1
                    if p[0] < heights.shape[0] - 1 and heights[p[0] + 1, p[1]] == i:
                        next_dict[(p[0] + 1, p[1])] = 1
                    if p[1] < heights.shape[1] - 1 and heights[p[0], p[1] + 1] == i:
                        next_dict[(p[0], p[1] + 1)] = 1
                if len(next_dict) > 0:
                    next_starts.append(next_dict)
            starts = next_starts

        return sum(len(s) for s in starts)

    def parse_and_solve_p2(self, filename):
        heights: np.array = self.parse(filename)
        starts = [{(x[0].item(), x[1].item()): 1} for x in np.argwhere(heights == 0)]
        for i in range(1, 10):
            next_starts = []
            for s in starts:
                next_dict = {}
                for p in s.keys():
                    paths = s[p]
                    if p[0] > 0 and heights[p[0] - 1, p[1]] == i:
                        p_next = (p[0] - 1, p[1])
                        next_dict[p_next] = paths + next_dict.get(p_next, 0)
                    if p[1] > 0 and heights[p[0], p[1] - 1] == i:
                        p_next = (p[0], p[1] - 1)
                        next_dict[p_next] = paths + next_dict.get(p_next, 0)
                    if p[0] < heights.shape[0] - 1 and heights[p[0] + 1, p[1]] == i:
                        p_next = (p[0] + 1, p[1])
                        next_dict[p_next] = paths + next_dict.get(p_next, 0)
                    if p[1] < heights.shape[1] - 1 and heights[p[0], p[1] + 1] == i:
                        p_next = (p[0], p[1] + 1)
                        next_dict[p_next] = paths + next_dict.get(p_next, 0)
                if len(next_dict) > 0:
                    next_starts.append(next_dict)
            starts = next_starts

        return sum(sum(s.values()) for s in starts)

    def parse(self, filename):
        with open(filename) as f:
            return np.array([[-1 if x == '.' else int(x) for x in list(line)] for line in f.read().splitlines()])


solution = Solution()
print("Parse test:", solution.parse('input/day_10_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_10_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_10.input'))
print("Solve 2 test:", solution.parse_and_solve_p2('input/day_10_test.input'))
print("Solve 2:", solution.parse_and_solve_p2('input/day_10.input'))

