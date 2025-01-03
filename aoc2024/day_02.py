class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        counter = 0
        for line in data:
            counter += self.is_safe(line)
        return counter

    def parse_and_solve_p2(self, filename):
        data = self.parse(filename)
        counter = 0
        for line in data:
            for i in range(len(line)):
                if self.is_safe(line[:i] + line[i + 1:]):
                    counter += 1
                    break
        return counter

    def is_safe(self, line):
        safe = True
        positive = None
        for i in range(1, len(line)):
            a = line[i - 1]
            b = line[i]
            if positive is None:
                positive = b > a
            if (positive and b <= a) or (not positive and b >= a) or abs(b - a) > 3:
                safe = False
                break
        return safe

    def parse(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                data.append([int(x) for x in line.split()])
            return data


print("Parse test:", Solution().parse('input/day_02_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_02_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_02.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_02_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_02.input'))


