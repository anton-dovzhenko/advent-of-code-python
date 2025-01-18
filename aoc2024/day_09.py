from collections import OrderedDict
from sortedcontainers import SortedDict


class Solution:

    def parse_and_solve_p1(self, filename):
        data = self.parse(filename)
        s = 0
        e = len(data) - 1
        while s < e:
            if data[s] > -1:
                s += 1
            elif data[e] < 0:
                e -= 1
            else:
                data[s] = data[e]
                data[e] = -1
                s += 1
                e -= 1
        checksum = 0
        for i in range(len(data)):
            if data[i] > -1:
                checksum += i * data[i]
        return checksum

    def parse_and_solve_p2(self, filename):
        id_len, id_pos, gaps = self.parse2(filename)
        for id in reversed(id_pos.keys()):
            move_to = -1
            pos = id_pos[id]
            len = id_len[id]
            for index, length in gaps.items():
                if index > pos:
                    break
                if length >= len:
                    move_to = index
                    break
            if move_to > -1:
                id_pos[id] = move_to
                gaps[pos] = len
                if gaps[move_to] > len:
                    gaps[move_to + len] = gaps[move_to] - len
                del gaps[move_to]
        checksum = 0
        for id in id_pos.keys():
            pos = id_pos[id]
            for i in range(pos, pos + id_len[id]):
                checksum += i * id
        return checksum

    def parse(self, filename):
        with open(filename) as f:
            line = f.read()
            data = []
            for i in range(len(line)):
                if i % 2 == 0:
                    data = data + [i // 2] * int(line[i])
                else:
                    data = data + [-1] * int(line[i])
            return data

    def parse2(self, filename):
        with open(filename) as f:
            line = f.read()
            id_len = OrderedDict()
            id_pos = OrderedDict()
            gaps = SortedDict()
            index = 0
            for i in range(len(line)):
                if i % 2 == 0:
                    id_len[i // 2] = int(line[i])
                    id_pos[i // 2] = index
                else:
                    gaps[index] = int(line[i])
                index += int(line[i])
            return id_len, id_pos, gaps


solution = Solution()
print("Parse test:", solution.parse('input/day_09_test.input'))
print("Parse2 test:", solution.parse2('input/day_09_test.input'))
# print("Solve 1 test:", solution.parse_and_solve_p1('input/day_09_test.input'))
# print("Solve 1:", solution.parse_and_solve_p1('input/day_09.input'))
print("Solve 2 test:", solution.parse_and_solve_p2('input/day_09_test.input'))
print("Solve 2:", solution.parse_and_solve_p2('input/day_09.input'))

