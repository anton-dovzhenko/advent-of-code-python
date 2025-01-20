import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        cost = 0
        visited = np.zeros(data.shape)
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                res = self.mark(data, visited, data[i][j], i, j)
                cost += res.prod()
        return cost

    def mark(self, data, visited, c, i, j):
        if i < 0 or i == data.shape[0] or j < 0 or j == data.shape[1] or data[i][j] != c or visited[i][j] == 1:
            return np.array([0, 0])
        visited[i][j] = 1
        area = 1
        perimeter = 0
        perimeter += i == 0 or data[i - 1][j] != c
        perimeter += j == 0 or data[i][j - 1] != c
        perimeter += i == data.shape[0] - 1 or data[i + 1][j] != c
        perimeter += j == data.shape[1] - 1 or data[i][j + 1] != c

        res = np.array([area, perimeter])
        res += self.mark(data, visited, c, i - 1, j)
        res += self.mark(data, visited, c, i, j - 1)
        res += self.mark(data, visited, c, i + 1, j)
        res += self.mark(data, visited, c, i, j + 1)
        return res

    def parse_and_solve_p2(self, filename):
        data = self.parse(filename)
        cost = 0
        visited = np.zeros(data.shape)
        left = np.zeros(data.shape)
        right = np.zeros(data.shape)
        up = np.zeros(data.shape)
        down = np.zeros(data.shape)
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                res = self.mark2(data, visited, left, right, up, down, data[i][j], i, j)
                cost += res.prod()
        return cost

    def mark2(self, data, visited, left, right, up, down, c, i, j):
        if i < 0 or i == data.shape[0] or j < 0 or j == data.shape[1] or data[i][j] != c or visited[i][j] == 1:
            return np.array([0, 0])
        visited[i][j] = 1
        area = 1
        sides = 0

        if (i == 0 or data[i - 1][j] != c) and up[i][j] == 0:
            sides += 1
            up[i][j] = 1
            self.mark_up(data, up, c, i, j, -1)
            self.mark_up(data, up, c, i, j, 1)
        if (i == data.shape[0] - 1 or data[i + 1][j] != c) and down[i][j] == 0:
            sides += 1
            down[i][j] = 1
            self.mark_down(data, down, c, i, j, -1)
            self.mark_down(data, down, c, i, j, 1)
        if (j == 0 or data[i][j - 1] != c) and left[i][j] == 0:
            sides += 1
            left[i][j] = 1
            self.mark_left(data, left, c, i, j, -1)
            self.mark_left(data, left, c, i, j, 1)
        if (j == data.shape[1] - 1 or data[i][j + 1] != c) and right[i][j] == 0:
            sides += 1
            right[i][j] = 1
            self.mark_right(data, right, c, i, j, -1)
            self.mark_right(data, right, c, i, j, 1)

        res = np.array([area, sides])
        res += self.mark2(data, visited, left, right, up, down, c, i - 1, j)
        res += self.mark2(data, visited, left, right, up, down, c, i, j - 1)
        res += self.mark2(data, visited, left, right, up, down, c, i + 1, j)
        res += self.mark2(data, visited, left, right, up, down, c, i, j + 1)

        return res

    def mark_up(self, data, up, c, i, j, increment):
        j = j + increment
        if 0 <= j < data.shape[1] and data[i][j] == c:
            if i == 0 or data[i - 1][j] != c:
                up[i][j] = 1
                self.mark_up(data, up, c, i, j, increment)

    def mark_down(self, data, down, c, i, j, increment):
        j = j + increment
        if 0 <= j < data.shape[1] and data[i][j] == c:
            if i == data.shape[0] - 1 or data[i + 1][j] != c:
                down[i][j] = 1
                self.mark_down(data, down, c, i, j, increment)

    def mark_left(self, data, left, c, i, j, increment):
        i = i + increment
        if 0 <= i < data.shape[0] and data[i][j] == c:
            if j == 0 or data[i][j - 1] != c:
                left[i][j] = 1
                self.mark_left(data, left, c, i, j, increment)

    def mark_right(self, data, right, c, i, j, increment):
        i = i + increment
        if 0 <= i < data.shape[0] and data[i][j] == c:
            if j == data.shape[1] - 1 or data[i][j + 1] != c:
                right[i][j] = 1
                self.mark_right(data, right, c, i, j, increment)

    def parse(self, filename):
        with open(filename) as f:
            return np.array([list(x) for x in f.read().split('\n')])


solution = Solution()
print("Parse test:", solution.parse('input/day_12_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_12_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_12.input'))
print("Solve 1 test:", solution.parse_and_solve_p2('input/day_12_test.input'))
print("Solve 1:", solution.parse_and_solve_p2('input/day_12.input'))

