import math


class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        inv_sum = 0
        for r in data:
            start = r[0]
            end = r[1]
            ds = math.floor(math.log10(start)) + 1
            if ds % 2 == 1:
                start = 10 ** ds
            si = int(str(start)[:len(str(start)) // 2])
            while True:
                invalid = int(str(si) * 2)
                if invalid > end:
                    break
                if invalid >= start:
                    inv_sum += invalid
                si += 1
        return inv_sum

    def parse_and_solve_p2(self, filename):
        data = self.parse(filename)
        factors = {}
        inv_nums = set()
        rmin = data[0][0]
        rmax = data[0][1]
        for r in data:
            rmin = min(rmin, r[0])
            rmax = max(rmax, r[1])
        dmin = math.floor(math.log10(rmin)) + 1
        dmax = math.floor(math.log10(rmax)) + 1

        for d in range(dmin, dmax):
            if d not in factors:
                f = Solution._get_factors(d)
                factors[d] = f[:-1]
            for f in factors[d]:
                repeat = d // f
                si = 10 ** (f - 1)

                while True:
                    invalid = int(str(si) * repeat)
                    if invalid > rmax:
                        break
                    if Solution._is_in_range(data, invalid):
                        inv_nums.add(invalid)
                    si += 1

        return sum(inv_nums)

    @staticmethod
    def _is_in_range(data, x):
        for r in data:
            if r[0] <= x <= r[1]:
                return True
        return False

    @staticmethod
    def _get_factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]

    def parse(self, filename):
        with open(filename) as f:
            data = f.read()
            data = list(map(lambda x: list(map(int, x.split('-'))), data.split(',')))
        return data


print("Parse test:", Solution().parse('input/day_02_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_02_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_02.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_02_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_02.input'))

