class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        return self._check_access(data)

    def parse_and_solve_p2(self, filename):
        access_count = 0
        data = self.parse(filename)
        while True:
            access_next = self._check_access(data, remove_roll=True)
            access_count += access_next
            if access_next == 0:
                break
        return access_count

    def _check_access(self, data, remove_roll=False):
        access_count = 0
        neighbours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in range(1, len(data) - 1):
            for j in range(1, len(data[i]) - 1):
                if data[i][j] == '@':
                    rolls = 0
                    for n in neighbours:
                        if data[i + n[0]][j + n[1]] == '@':
                            rolls += 1
                    if rolls < 4:
                        access_count += 1
                        if remove_roll:
                            data[i][j] = '.'
        return access_count

    def parse(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                data.append(['.'] + list(line.strip()) + ['.'])
        data.insert(0, ['.'] * len(data[0]))
        data.append(['.'] * len(data[0]))
        return data


print("Parse test:", Solution().parse('input/day_04_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_04_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_04.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_04_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_04.input'))

