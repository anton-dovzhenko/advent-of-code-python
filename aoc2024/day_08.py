import math
import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        dim, pos = self.parse(filename)
        anti_nodes = set()
        for antennas in pos:
            for i in range(len(antennas)):
                for j in range(i + 1, len(antennas)):
                    a1 = antennas[i]
                    a2 = antennas[j]
                    vec = a2 - a1
                    an1 = a1 - vec
                    an2 = a2 - vec
                    if self._is_in_dim(dim, an1):
                        anti_nodes.add(tuple(an1))
                    if self._is_in_dim(dim, an2):
                        anti_nodes.add(tuple(an2))
        return len(anti_nodes)

    def parse_and_solve_p2(self, filename):
        dim, pos = self.parse(filename)
        anti_nodes = set()
        for antennas in pos:
            for i in range(len(antennas)):
                for j in range(i + 1, len(antennas)):
                    a1 = antennas[i]
                    a2 = antennas[j]
                    vec = a2 - a1
                    vec = vec / math.gcd(vec[0], vec[1])
                    anti_nodes.add(tuple(a1))
                    k = 1
                    while True:
                        an = a1 + vec * k
                        if self._is_in_dim(dim, an):
                            anti_nodes.add(tuple(an))
                            k += 1
                        else:
                            break
                    k = 1
                    while True:
                        an = a1 - vec * k
                        if self._is_in_dim(dim, an):
                            anti_nodes.add(tuple(an))
                            k += 1
                        else:
                            break

        return len(anti_nodes)

    def _is_in_dim(self, dim, an):
        return 0 <= an[0] < dim[0] and 0 <= an[1] < dim[1]

    def parse(self, filename):
        with open(filename) as f:
            puzzle = np.array([list(line) for line in f.read().splitlines()])
            return puzzle.shape, [np.argwhere(puzzle == x) for x in np.unique(puzzle) if x != '.']


solution = Solution()
print("Parse test:", solution.parse('input/day_08_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_08_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_08.input'))
print("Solve 2 test:", solution.parse_and_solve_p2('input/day_08_test.input'))
print("Solve 2:", solution.parse_and_solve_p2('input/day_08.input'))

