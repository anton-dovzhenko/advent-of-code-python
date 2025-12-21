import numpy as np


class Solution:
    """
    Does not solve general case, only counts cases where placing is figure in 3x3 square is enough,
    or where figure's area is greater than rectangle's area.
    This works for AoC input
    """

    def parse_and_solve(self, filename):
        figures, rectangles = self.parse(filename)
        super_fit = 0
        no_fit = 0
        areas = []
        for f in figures:
            areas.append(np.sum(f))
        areas = np.array(areas)
        for r in rectangles:
            sides = r[0]
            rec_len = 3 * (sides[0] // 3)
            rec_height = 3 * (sides[1] // 3)
            fig_count = r[1]
            min_area = (areas * fig_count).sum()
            max_area = (9 * fig_count).sum()
            super_fit += (rec_len * rec_height) >= max_area
            no_fit += min_area > sides[0] * sides[1]
        return super_fit, no_fit, len(rectangles)

    def parse(self, filename):
        with open(filename) as f:
            file = f.read()
            file = file.split("\n\n")

            figures = []
            for line in file[:-1]:
                line = (np.array([list(x) for x in line[3:].split("\n")]) == '#').astype(int)
                figures.append(line)

            rectangles = []
            for line in file[-1].split("\n"):
                line = line.split(": ")
                rectangles.append((np.array(line[0].split('x')).astype(int), np.array(line[1].split(' ')).astype(int)))
        return figures, rectangles


print("Parse test:", Solution().parse('input/day_12_test.input'))
print("Solve test:", Solution().parse_and_solve('input/day_12_test.input'))
print("Solve:", Solution().parse_and_solve('input/day_12.input'))

