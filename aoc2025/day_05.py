from operator import itemgetter


class Solution:

    def parse_and_solve_p1(self, filename):
        ranges, ids = self.parse(filename)
        valid_cnt = 0
        for i in ids:
            for r in ranges:
                if r[0] <= i <= r[1]:
                    valid_cnt +=1
                    break
        return valid_cnt

    def parse_and_solve_p2(self, filename):
        ranges, ids = self.parse(filename)
        compressed = self.compress_ranges(ranges)
        valid_cnt = 0
        for c in compressed:
            valid_cnt += 1 + c[1] - c[0]
        return valid_cnt

    def compress_ranges(self, ranges):
        ranges = sorted(ranges, key=itemgetter(0))
        compressed = [ranges[0]]
        for i in range(1, len(ranges)):
            r = ranges[i]
            if r[0] <= compressed[-1][1]:
                compressed[-1][1] = max(compressed[-1][1], r[1])
            else:
                compressed.append(r)
        return compressed

    def parse(self, filename):
        ranges = []
        ids = []
        with open(filename) as f:
            for line in f:
                if '-' in line:
                    ranges.append([int(x) for x in line.split('-')])
                elif len(line.strip()) > 0:
                    ids.append(int(line))
        return ranges, ids


print("Parse test:", Solution().parse('input/day_05_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_05_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_05.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_05_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_05.input'))

