class Solution:

    def solve(self, filename, days):
        fish = self.parse(filename)
        while days > 0:
            next_fish = {}
            for key, value in fish.items():
                if key > 0:
                    next_fish[key - 1] = value + next_fish.get(key - 1, 0)
                else:
                    next_fish[8] = value + next_fish.get(8, 0)
                    next_fish[6] = value + next_fish.get(6, 0)
            fish = next_fish
            days -= 1
        return sum(fish.values())

    def parse(self, filename):
        with open(filename) as f:
            fish = {}
            for i in f.read().split(','):
                n = int(i)
                fish[n] = 1 + fish.get(n, 0)
            return fish

