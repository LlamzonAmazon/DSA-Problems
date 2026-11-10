class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # The cost to reach any floor i is just the min(cost[i-1], cost[i-2])

        fromMinusOne, fromMinusTwo = 0, 0

        for i in range(2, len(cost)+1):
            # min(cost from -1-floor + -1-floor's cost, cost from -2-floor + -2-floor's cost)
            floorCost = min(fromMinusOne + cost[i-1], fromMinusTwo + cost[i-2])

            fromMinusTwo = fromMinusOne
            fromMinusOne = floorCost

        return fromMinusOne