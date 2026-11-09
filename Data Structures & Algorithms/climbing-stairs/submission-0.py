class Solution:
    def climbStairs(self, n: int) -> int:
        
        oneStep, twoSteps = 1, 1

        for i in range(n-1):
            temp = oneStep
            oneStep = oneStep + twoSteps
            twoSteps = temp

        return oneStep