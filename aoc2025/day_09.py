class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        max_area = 0
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                length = 1 + abs(data[i][0] - data[j][0])
                height = 1 + abs(data[i][1] - data[j][1])
                max_area = max(max_area, length * height)
        return max_area

    def parse_and_solve_p2(self, filename):
        data = self.parse(filename)
        max_area = 0
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                length = 1 + abs(data[i][0] - data[j][0])
                height = 1 + abs(data[i][1] - data[j][1])
                bottom_left = min(data[i][0], data[j][0]), min(data[i][1], data[j][1])
                top_right = max(data[i][0], data[j][0]), max(data[i][1], data[j][1])
                match = True
                for k in range(len(data)):
                    start = data[k]
                    end = data[-1 if k == len(data) - 1 else k + 1]
                    horizontal = start[1] == end[1]
                    match = match and not (horizontal and min(start[0], end[0]) < top_right[0] and max(start[0], end[0]) > bottom_left[0] and bottom_left[1] < start[1] < top_right[1])
                    match = match and not (not horizontal and min(start[1], end[1]) < top_right[1] and max(start[1], end[1]) > bottom_left[1] and bottom_left[0] < start[0] < top_right[0])
                    if not match:
                        break
                if match:
                    max_area = max(max_area, length * height)
        return max_area

    def parse(self, filename):
        data = []
        with open(filename) as f:
            for line in f:
                data.append([int(d) for d in line.strip().split(',')])
            return data


print("Parse test:", Solution().parse('input/day_09_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_09_test.input'))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_09.input'))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_09_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_09.input'))


