import numpy as np


class Solution:

    def __init__(self):
        self.CODE = "XMAS"
        self.CODE_REV = self.CODE[::-1]
        self.CROSS = ['AMMSS', 'ASSMM', 'ASMSM', 'AMSMS']

    def parse_and_solve_p1(self, filename):
        count = 0
        data = self.parse(filename)
        count += np.sum(np.apply_along_axis(self._get_count, 0, data))
        count += np.sum(np.apply_along_axis(self._get_count_rev, 0, data))
        count += np.sum(np.apply_along_axis(self._get_count, 1, data))
        count += np.sum(np.apply_along_axis(self._get_count_rev, 1, data))

        for i in range(-data.shape[0], data.shape[1]):
            count += self._get_count(np.diagonal(data, offset=i))
            count += self._get_count_rev(np.diagonal(data, offset=i))

        data = np.rot90(data)
        for i in range(-data.shape[0], data.shape[1]):
            count += self._get_count(np.diagonal(data, offset=i))
            count += self._get_count_rev(np.diagonal(data, offset=i))
        return count

    def parse_and_solve_p2(self, filename):
        count = 0
        data = self.parse(filename)
        for i in range(1, data.shape[0] - 1):
            for j in range(1, data.shape[1] - 1):
                count += data[i, j] == 'A' and (data[i, j] + data[i - 1, j - 1] + data[i - 1, j + 1] + data[i + 1, j - 1] + data[i + 1, j + 1]) in self.CROSS
        return count

    def _get_count(self, array, rev=False):
        code = self.CODE_REV if rev else self.CODE
        count = 0
        match = 0
        for c in array:
            match = (match + 1) if c == code[match] else c == code[0]
            if match == len(code):
                count += 1
                match = 0
        return count

    def _get_count_rev(self, array):
        return self._get_count(array, True)

    def parse(self, filename):
        with open(filename) as f:
            return np.array([list(line) for line in f.read().splitlines()])


solution = Solution()
print("Parse test:", solution.parse('input/day_04_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_04_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_04.input'))
print("Solve 2 test:", solution.parse_and_solve_p2('input/day_04_test.input'))
print("Solve 2:", solution.parse_and_solve_p2('input/day_04.input'))


