import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                data.append(line.strip().split())
        operations = data[-1]
        data = data[:-1]
        data = np.array(data, dtype=int).T
        return self.calculate(data, operations)

    def parse_and_solve_p2(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                data.append(line)
        operations = data[-1]
        data = data[:-1]
        numbers = []
        prev_split = 0
        for i in range(1, len(operations) + 1):
            if i == len(operations) or operations[i] != ' ':
                row = []
                for column in data:
                    row.append(list(column[prev_split: i]))
                row = np.array(row).T
                row = [''.join(x).strip() for x in row]
                row = np.array([int(x) for x in row if len(x) > 0])
                numbers.append(row)
                prev_split = i
        return self.calculate(numbers, operations.split())

    def calculate(self, numbers, operations):
        result = 0
        for i in range(len(numbers)):
            row = numbers[i]
            if operations[i] == '+':
                result += np.sum(row)
            elif operations[i] == '*':
                result += np.prod(row)
            else:
                raise Exception(f'Unknown operation ' + operations[i])
        return result


print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_06_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_06.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_06_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_06.input'))

