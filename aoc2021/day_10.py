import statistics


class Solution:

    def __init__(self):
        self.close = {')': '(', ']': '[', '}': '{', '>': '<'}

    def parse_and_solve_p1(self, filename):
        lines = self.parse(filename)
        points = {')': 3, ']': 57, '}': 1197, '>': 25137}
        s = 0
        for line in lines:
            stack = []
            for c in list(line.strip()):
                if c in '([{<':
                    stack.append(c)
                else:
                    if len(stack) > 0 and stack[-1] == self.close[c]:
                        del stack[-1]
                    else:
                        s += points[c]
                        break
        return s

    def parse_and_solve_p2(self, filename):
        lines = self.parse(filename)
        scores = []
        for line in lines:
            stack = []
            for c in list(line.strip()):
                if c in '([{<':
                    stack.append(c)
                else:
                    if len(stack) > 0 and stack[-1] == self.close[c]:
                        del stack[-1]
                    else:
                        stack = []
                        break
            if len(stack) > 0:
                scores.append(self.score(reversed(stack)))
        return statistics.median(scores)

    def score(self, stack):
        points = {'(': 1, '[': 2, '{': 3, '<': 4}
        s = 0
        for c in stack:
            s = s * 5 + points[c]
        return s

    def parse(self, filename):
        with open(filename) as f:
            return f.readlines()

