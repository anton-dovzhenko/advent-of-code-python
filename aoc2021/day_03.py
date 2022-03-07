import numpy as np


class Solution:

    def __init__(self):
        pass

    def parse_and_solve_p1(self, filename):
        m = self.parse(filename)
        thr = m.shape[1] / 2
        gamma = Solution.list_to_binary(str(int(x > thr)) for x in np.nditer(np.sum(m, axis=1)))
        epsilon = Solution.list_to_binary(str(int(x <= thr)) for x in np.nditer(np.sum(m, axis=1)))
        return gamma * epsilon

    def parse_and_solve_p2(self, filename):
        m = self.parse(filename)
        gamma = m
        epsilon = m
        for i in range(gamma.shape[0]):
            s = np.sum(gamma[i])
            common = 1 if s >= gamma.shape[1] / 2 else 0
            d = np.where(gamma[i] != common)[1]
            gamma = np.delete(gamma, d, axis=1)

        for i in range(epsilon.shape[0]):
            if epsilon.shape[1] == 1:
                break
            s = np.sum(epsilon[i])
            common = 0 if s >= epsilon.shape[1] / 2 else 1
            d = np.where(epsilon[i] != common)[1]
            epsilon = np.delete(epsilon, d, axis=1)

        gamma = Solution.list_to_binary(str(x) for x in np.nditer(gamma.flatten()))
        epsilon = Solution.list_to_binary(str(x) for x in np.nditer(epsilon.flatten()))
        return gamma * epsilon

    @staticmethod
    def list_to_binary(x):
        return int(''.join(x), 2)

    def parse(self, filename):
        def line_to_num(x):
            return [int(c) for c in x]
        with open(filename) as f:
            m = np.matrix([line_to_num(line.strip()) for line in f])
            m = np.transpose(m)
            return m

