import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        data = np.array(data)
        return np.sum((50 + np.cumsum(data)) % 100 == 0)

    def parse_and_solve_p2(self, filename):
        data = self.parse(filename)
        zero_count = 0
        start = 50
        for d in data:
            if 0 < start + d < 100:
                pass
            elif start == 0:
                zero_count += abs(d) // 100
            elif d > 0:
                zero_count += 1 + ((d - (100 - start)) // 100)
            else:
                zero_count += 1 + (-d - start) // 100
            start = (start + d) % 100
        return zero_count

    def parse(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                sign = -1 if line.startswith('L') else 1
                data.append(sign * int(line[1:]))
            return data


print("Parse test:", Solution().parse('input/day_01_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_01_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_01.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_01_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_01.input'))


