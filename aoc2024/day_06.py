import copy
import numpy as np


class Solution:

    def __init__(self):
        self.direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.direction_sym = ['^', '>', 'v', '<']

    def parse_and_solve_p1(self, filename):
        guard, puzzle = self.parse(filename)
        di = 0
        while True:
            step = self.direction[di % 4]
            next_guard = guard[0] + step[0], guard[1] + step[1]
            if self._is_outside_puzzle(puzzle, next_guard):
                break
            elif puzzle[next_guard] == '#':
                di += 1
            else:
                puzzle[next_guard] = '^'
                guard = next_guard

        return np.sum(puzzle == '^')

    def parse_and_solve_p2(self, filename):
        loops = 0
        guard, puzzle = self.parse(filename)
        for i in range(puzzle.shape[0]):
            for j in range(puzzle.shape[1]):
                c = puzzle[i][j]
                if c == '.':
                    puzzle_copy = copy.deepcopy(puzzle)
                    puzzle_copy[i][j] = '#'
                    loops += self.has_loop(guard, puzzle_copy)
                print(i, j)
        return loops

    def has_loop(self, guard, puzzle):
        di = 0
        while True:
            step = self.direction[di % 4]
            next_guard = guard[0] + step[0], guard[1] + step[1]
            if self._is_outside_puzzle(puzzle, next_guard):
                return False
            elif puzzle[next_guard] == '#':
                di += 1
            else:
                if puzzle[next_guard] == self.direction_sym[di % 4]:
                    return True
                puzzle[next_guard] = self.direction_sym[di % 4]
                guard = next_guard

    def _is_outside_puzzle(self, puzzle, index):
        return index[0] < 0 or index[1] < 0 or index[0] >= puzzle.shape[0] or index[1] >= puzzle.shape[1]

    def parse(self, filename):
        with open(filename) as f:
            puzzle = np.array([list(line) for line in f.read().splitlines()])
            guard = np.where(puzzle == '^')
            guard = guard[0][0], guard[1][0]
            return guard, puzzle


solution = Solution()
print("Parse test:", solution.parse('input/day_06_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_06_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_06.input'))
print("Solve 2 test:", solution.parse_and_solve_p2('input/day_06_test.input'))
print("Solve 2:", solution.parse_and_solve_p2('input/day_06.input'))


