from functools import cmp_to_key


class Solution:

    def parse_and_solve_p1(self, filename):
        result = 0
        rules, sequences = self.parse(filename)
        for s in sequences:
            if self._is_ordered(rules, s):
                result += s[len(s) // 2]
        return result

    def parse_and_solve_p2(self, filename):
        result = 0
        rules, sequences = self.parse(filename)
        for s in sequences:
            if not self._is_ordered(rules, s):
                s = sorted(s, key=cmp_to_key(lambda x, y: -1 if y in rules[x] else 0))
                result += s[len(s) // 2]
        return result

    def _is_ordered(self, rules, sequence):
        for i in range(0, len(sequence) - 1):
            if rules[sequence[i]] & set(sequence[i + 1:]):
                return False
        return True

    def parse(self, filename):
        with open(filename) as f:
            txt = f.read()
            txt = txt.split("\n\n")
            rules = [[int(n) for n in r.split("|")] for r in txt[0].split("\n")]
            rules = self.parse_rules(rules)
            sequences = [[int(n) for n in s.split(",")] for s in txt[1].split("\n")]
            return rules, sequences

    def parse_rules(self, rules):
        prec_rules = {}
        distinct = set()
        for r in rules:
            distinct.add(r[0])
            distinct.add(r[1])
        for r in distinct:
            prec_rules[r] = set()
        for r in rules:
            prec_rules[r[1]].add(r[0])
        return prec_rules


solution = Solution()
# print("Parse test:", solution.parse('input/day_05_test.input'))
print("Solve 1 test:", solution.parse_and_solve_p1('input/day_05_test.input'))
print("Solve 1:", solution.parse_and_solve_p1('input/day_05.input'))
print("Solve 2 test:", solution.parse_and_solve_p2('input/day_05_test.input'))
print("Solve 2:", solution.parse_and_solve_p2('input/day_05.input'))


