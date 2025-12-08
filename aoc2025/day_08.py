import collections
import numpy as np


class Solution:

    def parse_and_solve_p1(self, filename, pairs):
        data = self.parse(filename)
        circuits = [-1] * len(data)
        circuit_id = 0
        distances = self._get_shortest_distances(data)
        cnt = 0
        for key, value in distances.items():
            if cnt == pairs:
                break
            p1 = value[0]
            p2 = value[1]
            if circuits[p1] == -1 and circuits[p2] == -1:
                circuit_id += 1
                circuits[p1] = circuit_id
                circuits[p2] = circuit_id
            elif circuits[p1] == -1 or circuits[p2] == -1:
                circuits[p1] = max(circuits[p1], circuits[p2])
                circuits[p2] = max(circuits[p1], circuits[p2])
            elif circuits[p1] != circuits[p2]:
                old = circuits[p2]
                for i in range(len(circuits)):
                    if circuits[i] == old:
                        circuits[i] = circuits[p1]
            cnt += 1

        circuits = collections.Counter(circuits)
        del circuits[-1]
        return np.array(sorted(list(circuits.values()), reverse=True))[:3].prod()

    def parse_and_solve_p2(self, filename):
        data = self.parse(filename)
        circuits = [-1] * len(data)
        circuit_id = 0
        distances = self._get_shortest_distances(data)

        for key, value in distances.items():
            p1 = value[0]
            p2 = value[1]
            if circuits[p1] == -1 and circuits[p2] == -1:
                circuit_id += 1
                circuits[p1] = circuit_id
                circuits[p2] = circuit_id
            elif circuits[p1] == -1 or circuits[p2] == -1:
                circuits[p1] = max(circuits[p1], circuits[p2])
                circuits[p2] = max(circuits[p1], circuits[p2])
            elif circuits[p1] != circuits[p2]:
                old = circuits[p2]
                for i in range(len(circuits)):
                    if circuits[i] == old:
                        circuits[i] = circuits[p1]
            if -1 not in circuits:
                break

        return data[p1][0] * data[p2][0]

    def _get_shortest_distances(self, data):
        distances = {}
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                d = self._euclidean(data[i], data[j])
                distances[d] = (i, j)
        distances = collections.OrderedDict(sorted(distances.items()))
        return distances

    def _euclidean(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2)

    def parse(self, filename):
        boxes = []
        with open(filename) as f:
            for line in f:
                boxes.append([int(x) for x in line.split(",")])
        return boxes


print("Parse test:", Solution().parse('input/day_08_test.input'))
print("Solve 1 test:", Solution().parse_and_solve_p1('input/day_08_test.input', pairs=10))
print("Solve 1:", Solution().parse_and_solve_p1('input/day_08.input', pairs=1000))
print("Solve 2 test:", Solution().parse_and_solve_p2('input/day_08_test.input'))
print("Solve 2:", Solution().parse_and_solve_p2('input/day_08.input'))

