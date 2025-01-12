class Solution:

    def parse_and_solve_p1(self, filename):
        calibration = 0
        data = self.parse(filename)
        for row in data:
            n, array = row
            if self._is_equals_1(n, array[0], 1, array):
                calibration += n
        return calibration

    def _is_equals_1(self, n, expr, pos, array):
        if pos == len(array):
            return n == expr
        if expr > n:
            return False
        return self._is_equals_1(n, expr * array[pos], pos + 1, array) or self._is_equals_1(n, expr + array[pos], pos + 1, array)

    def parse_and_solve_p2(self, filename):
        calibration = 0
        data = self.parse(filename)
        for row in data:
            n, array = row
            if self._is_equals_2(n, array[0], 1, array):
                calibration += n
        return calibration

    def _is_equals_2(self, n, expr, pos, array):
        if pos == len(array):
            return n == expr
        if expr > n:
            return False
        return self._is_equals_2(n, expr * array[pos], pos + 1, array) \
            or self._is_equals_2(n, expr + array[pos], pos + 1, array) \
            or self._is_equals_2(n, int(str(expr) + str(array[pos])), pos + 1, array)

    def parse(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                line = line.split(": ")
                x = int(line[0])
                y = [int(i) for i in line[1].split(" ")]
                data.append((x, y))
        return data


solution = Solution()
print("Parse test:", solution.parse('input/day_07_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_07_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_07.input'))
print("Solve 2 test:", solution.parse_and_solve_p2('input/day_07_test.input'))
print("Solve 2:", solution.parse_and_solve_p2('input/day_07.input'))

