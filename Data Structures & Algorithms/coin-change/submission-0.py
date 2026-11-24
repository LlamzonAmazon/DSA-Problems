class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [float('inf')] * amount   # dp[i] = min coins to make amount i

        for i in range(1, amount + 1):

            for c in coins:

                if c <= i:

                    # DP of the current amount is the min of
                    # DP of current amount (if already defined, which is: NOT infinity), or
                    # DP of previously computed amount + 1 coin
                    dp[i] = min(dp[i], dp[i-c] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]