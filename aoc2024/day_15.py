import itertools

import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        r, field, moves = self.parse(filename)
        for move in moves:
            if move == '^':
                row = field[0:r[0], r[1]]
                index = np.where(row != 'O')[0][-1]
                if field[index, r[1]] == '.':
                    field[index:r[0], r[1]] = field[index + 1:r[0] + 1, r[1]]
                    r[0] -= 1
            elif move == 'v':
                row = field[r[0] + 1:, r[1]]
                index = r[0] + 1 + np.where(row != 'O')[0][0]
                if field[index, r[1]] == '.':
                    field[r[0] + 1: index + 1, r[1]] = field[r[0]:index, r[1]]
                    r[0] += 1
            elif move == '<':
                row = field[r[0], :r[1]]
                index = np.where(row != 'O')[0][-1]
                if field[r[0], index] == '.':
                    field[r[0], index:r[1]] = field[r[0], index + 1:r[1] + 1]
                    r[1] -= 1
            else:
                row = field[r[0], r[1] + 1:]
                index = r[1] + 1 + np.where(row != 'O')[0][0]
                if field[r[0], index] == '.':
                    field[r[0], r[1] + 1:index+1] = field[r[0], r[1]:index]
                    r[1] += 1
        return (np.array(np.where(field == 'O')).sum(axis=1) * np.array([100, 1])).sum()

    def print_field(self, field, robot):
        result = ''
        for i in range(len(field)):
            row = field[i]
            for j in range(len(row)):
                if i == robot[0] and j == robot[1]:
                    result += '@'
                else:
                    c = row[j]
                    result += c
            result += '\n'
        print(result)

    def parse_and_solve_p2(self, filename):
        return 0

    def parse(self, filename):
        with open(filename) as f:
            input = f.read()
            input = input.split("\n\n")
            field = input[0]
            moves = input[1].replace('\n', '')
            field = np.array([list(x.strip()) for x in field.split('\n')])
            robot = np.array(np.where(field == '@'))[:, 0]
            field[robot[0], robot[1]] = '.'
            return robot, field, moves


solution = Solution()
# print("Parse test:", solution.parse('input/day_15_test_2.input'))
print("Solve 1 test 1:", solution.parse_and_solve_p1('input/day_15_test_1.input'))
print("Solve 1 test 2:", solution.parse_and_solve_p1('input/day_15_test_2.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_15.input'))
# print("Solve 2:", solution.parse_and_solve_p2('input/day_15.input'))
