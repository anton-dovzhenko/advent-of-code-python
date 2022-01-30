class Solution:

    def parse_and_solve_p1(self, filename):
        n = self.parse(filename)
        s = self.solve_p1(n)
        return s

    def parse_and_solve_p2(self, filename):
        n = self.parse(filename)
        s = 0
        for i in range(2, len(n)):
            s += sum(n[i - 2:min(i + 1, len(n) - 1)]) > sum(n[max(0, i - 3):i])
        return s

    def solve_p1(self, n):
        s = 0
        for i in range(1, len(n)):
            s += n[i] > n[i - 1]
        return s

    def parse(self, filename):
        with open(filename) as f:
            return [int(line) for line in f]

