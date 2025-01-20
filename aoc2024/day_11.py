class Solution:

    def parse_and_solve_p1(self, filename, blinks):
        data = self.parse(filename)
        for i in range(blinks):
            next_data = []
            for n in data:
                if n == 0:
                    next_data.append(1)
                elif len(str(n)) % 2 == 0:
                    n = str(n)
                    next_data.append(int(n[:len(n) // 2]))
                    next_data.append(int(n[len(n) // 2:]))
                else:
                    next_data.append(n * 2024)
            data = next_data
        return len(data)

    def parse_and_solve_p2(self, filename, blinks):
        data = self.parse(filename)
        cache = {}
        result = 0
        for n in data:
            result += self._do_blink(cache, n, blinks)
        return result

    def _do_blink(self, cache, n, blinks):
        if blinks == 0:
            return 1
        cache_key = (n, blinks)
        if cache_key not in cache:
            if n == 0:
                cache[cache_key] = self._do_blink(cache, 1, blinks - 1)
            elif len(str(n)) % 2 == 0:
                n = str(n)
                res = self._do_blink(cache, int(n[:len(n) // 2]), blinks - 1)
                res += self._do_blink(cache, int(n[len(n) // 2:]), blinks - 1)
                cache[cache_key] = res
            else:
                cache[cache_key] = self._do_blink(cache, n * 2024, blinks - 1)
        return cache[cache_key]

    def parse(self, filename):
        with open(filename) as f:
            return [int(x) for x in f.read().split(" ")]


solution = Solution()
print("Parse test:", solution.parse('input/day_11_test.input'))
print("Solve 1 test (6):", solution.parse_and_solve_p1('input/day_11_test.input', 6))
print("Solve 1 test (25):", solution.parse_and_solve_p1('input/day_11_test.input', 25))
print("Solve 1 (25):", solution.parse_and_solve_p1('input/day_11.input', 25))
print("Solve 2 test (25):", solution.parse_and_solve_p2('input/day_11_test.input', 25))
print("Solve 2 (25):", solution.parse_and_solve_p2('input/day_11.input', 25))
print("Solve 2 (75):", solution.parse_and_solve_p2('input/day_11.input', 75))

