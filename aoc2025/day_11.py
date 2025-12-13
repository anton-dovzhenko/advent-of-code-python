import sys

import cvxpy as cp
import itertools

import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        conns = self.parse(filename)
        return self._next_step(conns, 'you')

    def _next_step(self, conns, node):
        if node == 'out':
            return 1
        else:
            path_count = 0
            for next_node in conns[node]:
                path_count += self._next_step(conns, next_node)
            return path_count


    def parse_and_solve_p2(self, filename):
        conns = self.parse(filename)
        cache = {}
        return self._next_step2(cache, conns, 'svr', False, False)

    def _next_step2(self, cache, conns, node, dac, fft):
        if node == 'out' and dac and fft:
            return 1
        elif node in conns:
            path_count = 0
            for next_node in conns[node]:
                next_dac = dac or (next_node == 'dac')
                next_fft = fft or (next_node == 'fft')
                cache_key = (next_node, next_dac, next_fft)
                if cache_key not in cache:
                    cache[cache_key] = self._next_step2(cache, conns, next_node, next_dac, next_fft)
                path_count += cache[cache_key]
            return path_count
        return 0

    def parse(self, filename):
        conns = {}
        with open(filename) as f:
            for line in f:
                line = line.strip().split(': ')
                from_node = line[0]
                out_nodes = line[1].split(' ')
                for on in out_nodes:
                    if from_node not in conns:
                        conns[from_node] = list()
                    conns[from_node].append(on)

        return conns


print("Parse test:", Solution().parse('input/day_11_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_11_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_11.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_11_2_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_11.input'))

