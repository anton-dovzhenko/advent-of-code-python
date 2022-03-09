import sys
import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename):
        lines = self.parse(filename)
        s = 0
        for line in lines:
            s += sum(len(digit) in (2, 4, 3, 7) for digit in line[1])
        return s

    def parse_and_solve_p2(self, filename):
        s = 0
        lines = self.parse(filename)
        for line in lines:
            render = self._parse_numbers(line[0])
            render = dict((v, k) for k, v in render.items())
            s += int(''.join(str(render[''.join(sorted(x))]) for x in line[1]))
        return s

    def _parse_numbers(self, numbers):
        render = {}
        numbers = [''.join(sorted(n)) for n in numbers]
        for n in numbers:
            n = ''.join(sorted(n))
            nl = len(n)
            if nl == 2:
                render[1] = n
            elif nl == 4:
                render[4] = n
            elif nl == 3:
                render[7] = n
            elif nl == 7:
                render[8] = n
        for n in numbers:
            nl = len(n)
            ns = set(n)
            if nl == 5:
                if 2 == len(ns & set(render[1])):
                    render[3] = n
                elif 3 == len(ns & set(render[4])):
                    render[5] = n
                else:
                    render[2] = n
            elif nl == 6:
                if 1 == len(ns & set(render[1])):
                    render[6] = n
                elif 4 == len(ns & set(render[4])):
                    render[9] = n
                else:
                    render[0] = n
        return render

    def parse(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            lines = (line.strip().split(' | ') for line in lines)
            return [[line[0].split(' '), line[1].split(' ')] for line in lines]


