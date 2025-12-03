class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        rating = 0
        for line in data:
            num = line[0] * 10 + line[1]
            for i in range(2, len(line)):
                d = line[i]
                n1 = 10 * (num // 10) + d
                n2 = 10 * (num % 10) + d
                num = max(num, n1)
                num = max(num, n2)
            rating += num
        return rating

    def parse_and_solve_p2(self, filename):
        data = self.parse(filename)
        rating = 0
        for line in data:
            rem = len(line) - 12
            while rem > 0:
                removed = False
                for i in range(0, len(line) - 1):
                    if line[i] < line[i + 1]:
                        del line[i]
                        removed = True
                        break
                if not removed:
                    del line[-1]
                rem -= 1
            rating += Solution._digits_to_integer(line)
        return rating

    @staticmethod
    def _digits_to_integer(digits):
        i = 0
        for d in digits:
            i = i * 10 + d
        return i

    def parse(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                data.append([int(d) for d in line.strip()])
            return data


print("Parse test:", Solution().parse('input/day_03_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_03_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_03.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_03_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_03.input'))

