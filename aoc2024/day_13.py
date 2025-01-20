import cvxpy as cp
import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        tokens = 0
        data = self.parse(filename)
        for game in data:
            t = self.solve(*game)
            if t is not None:
                tokens += np.dot(t, np.array([3, 1]))
        return int(tokens)

    def parse_and_solve_p2(self, filename):
        tokens = 0
        data = self.parse(filename, adjustment=10000000000000)
        for game in data:
            t = self.solve(*game)
            if t is not None:
                tokens += np.dot(t, np.array([3, 1]))
        return int(tokens)

    def parse(self, filename, adjustment=0):
        with open(filename) as f:
            i = 0
            data = []
            game = []
            for line in f.read().splitlines():
                if i % 4 <= 1:
                    line = line.split(" ")
                    game.append(int(line[-2].split('+')[-1][:-1]))
                    game.append(int(line[-1].split('+')[-1]))
                elif i % 4 == 2:
                    line = line.split(" ")
                    game.append(int(line[-2].split('=')[-1][:-1]) + adjustment)
                    game.append(int(line[-1].split('=')[-1]) + adjustment)
                    data.append(game)
                    game = []
                i += 1
            return data

    def solve(self, a1, a2, b1, b2, c1, c2):
        x = cp.Variable(2, integer=True)
        A = np.array([[a1, a2], [b1, b2]])
        C = np.array([c1, c2])
        objective = cp.Minimize(np.array([3, 1]) @ x)
        constraints = [x.T @ A == C]
        problem = cp.Problem(objective, constraints)
        problem.solve(verbose=False)
        return x.value


solution = Solution()
print("Parse test:", solution.parse('input/day_13_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_13_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_13.input'))
print("Solve 2 test:", solution.parse_and_solve_p2('input/day_13_test.input'))
print("Solve 2:", solution.parse_and_solve_p2('input/day_13.input'))

