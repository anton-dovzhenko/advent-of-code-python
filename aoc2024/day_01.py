import collections
import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        data = np.array(data)
        return np.abs(np.sort(data[:, 0]) - np.sort(data[:, 1])).sum()

    def parse_and_solve_p2(self, filename):
        data = self.parse(filename)
        data = np.array(data)
        counter = collections.Counter(data[:, 1])
        map_func = np.vectorize(lambda x: 0 if x not in counter else x * counter[x])
        return map_func(data[:, 0]).sum()

    def parse(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                data.append([int(x) for x in line.split()])
            return data


print("Parse test:", Solution().parse('input/day_01_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_01_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_01.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_01_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_01.input'))


