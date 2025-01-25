import itertools

import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename, w=11, t=7):
        data = self.parse(filename)
        mod = np.array([w, t])
        robots = (data[:, 0] + 100 * data[:, 1]) % mod
        W = (w - 1) / 2
        T = (t - 1) / 2
        q1 = ((robots[:, 0] < W) & (robots[:, 1] < T)).sum()
        q2 = ((robots[:, 0] > W) & (robots[:, 1] < T)).sum()
        q3 = ((robots[:, 0] < W) & (robots[:, 1] > T)).sum()
        q4 = ((robots[:, 0] > W) & (robots[:, 1] > T)).sum()
        return q1 * q2 * q3 * q4

    def _find_loop(self, data, mod):
        sec = 1
        robot_start = data[:, 0]
        while True:
            robots = (data[:, 0] + sec * data[:, 1]) % mod
            if (robots == robot_start).all():
                break
            sec += 1
        return sec

    def parse_and_solve_p2(self, filename, w=101, t=103, start=1):
        data = self.parse(filename)
        mod = np.array([w, t])

        loop = self._find_loop(data, mod)
        print(loop)

        nn = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
        nn.remove((0, 0))
        nn = np.array(nn)

        steps = start
        max_neighbours = -1
        max_neighbours_step = 0
        while steps < loop:
            robots = (data[:, 0] + steps * data[:, 1]) % mod
            robots_index = robots[:, 0] + robots[:, 1] * t
            neighbours_count = 0

            for r in robots:
                neighbours = r + nn
                neighbours = neighbours[:, 0] + neighbours[:, 1] * t
                neighbours_count += np.any(np.isin(robots_index, neighbours))

            if neighbours_count > max_neighbours:
                max_neighbours = neighbours_count
                max_neighbours_step = steps
                print(steps, neighbours_count)

            steps += 1
        return max_neighbours_step

    def parse(self, filename):
        with open(filename) as f:
            data = []
            for line in f.read().splitlines():
                line = line.split(" ")
                p = np.array([int(x) for x in (line[0].split("=")[1]).split(",")])
                v = np.array([int(x) for x in (line[1].split("=")[1]).split(",")])
                data.append([p, v])
            return np.array(data)


solution = Solution()
# print("Parse test:", solution.parse('input/day_14_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_14_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_14.input', w=101, t=103))
print("Solve 2:", solution.parse_and_solve_p2('input/day_14.input'))
