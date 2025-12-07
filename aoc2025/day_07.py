class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        count = 0
        for i in range(1, len(data)):
            row = data[i]
            for j in range(1, len(row)):
                if data[i - 1][j] == 1:
                    if data[i][j] >= 0:
                        data[i][j] = 1
                    else:
                        count += 1
                        if data[i][j - 1] != -1:
                            data[i][j - 1] = 1
                        if data[i][j + 1] != -1:
                            data[i][j + 1] = 1
        return count

    def parse_and_solve_p2(self, filename):
        data = self.parse(filename)
        for i in range(1, len(data)):
            row = data[i]
            for j in range(1, len(row)):
                if data[i - 1][j] >= 1:
                    if data[i][j] >= 0:
                        data[i][j] += data[i - 1][j]
                    else:
                        if data[i][j - 1] != -1:
                            data[i][j - 1] += data[i - 1][j]
                        if data[i][j + 1] != -1:
                            data[i][j + 1] += data[i - 1][j]
        return sum(data[-1])

    def parse(self, filename):
        data = []
        mapping = {'S': 1, '^': -1, '.': 0}
        with open(filename) as f:
            for line in f:
                data.append(list(mapping[x] for x in list('.' + line.strip() + '.')))
        return data


print("Parse test:", Solution().parse('input/day_07_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_07_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_07.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_07_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_07.input'))

