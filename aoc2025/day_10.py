import sys

import cvxpy as cp
import itertools

import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        problems = self.parse(filename)
        result = 0
        for p in problems:
            L = p[0]
            B = p[1]
            num_of_presses = sys.maxsize
            for comb in itertools.product([0, 1], repeat=B.shape[0]):
                comb = np.array(comb)
                res = np.matmul(comb.T, B) % 2
                if np.array_equal(res, L):
                    num_of_presses = min(num_of_presses, comb.sum())
            result += num_of_presses

        return result

    def parse_and_solve_p2(self, filename):
        problems = self.parse(filename)
        result = 0
        for p in problems:
            B = p[1]
            J = p[2]
            x = cp.Variable(B.shape[0], integer=True)
            constraints = [x >= 0, x @ B == J]
            prob = cp.Problem(cp.Minimize(cp.sum(x)), constraints)
            prob.solve(verbose=False)
            result += x.value.sum()
        return int(result)

    def parse(self, filename):
        problems = []
        with open(filename) as f:
            for line in f:
                break1 = line.index(']')
                break2 = line.index('{')
                break3 = line.index('}')
                L = (np.array(list(line[1:break1])) == '#').astype(int)
                J = np.array(line[break2 + 1:break3].split(',')).astype(int)
                B = line[break1 + 1: break2].strip().split(' ')
                matrix = []
                for b in B:
                    b = np.array(b[1:-1].split(',')).astype(int)
                    x = np.zeros(len(L))
                    x[b] = 1
                    matrix.append(x)
                matrix = np.array(matrix)
                problems.append((L, matrix, J))
        return problems


print("Parse test:", Solution().parse('input/day_10_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_10_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_10.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_10_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_10.input'))

