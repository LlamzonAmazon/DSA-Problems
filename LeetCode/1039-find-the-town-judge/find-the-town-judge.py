class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        trusts = defaultdict(int)

        # Count trust relationships such that only the judge's trust count equals n-1
        for trustor, trustee in trust:
            trusts[trustor] -= 1
            trusts[trustee] += 1

        # Find judge as index with n-1 trust relationship
        for i in range(1, n + 1):
            if trusts[i] == n-1:
                return i

        return -1