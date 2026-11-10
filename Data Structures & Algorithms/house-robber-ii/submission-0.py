class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Accumulated value at any house i is the 
        # max accumulated value from house i-2 || max accumulated value from house i-3 

        # len(nums) = 1, findMax of houses from second house, findMax of houses minus last house
        return max(nums[0], self.findMax(nums[1:]), self.findMax(nums[:-1]))

    def findMax(self, nums) -> int:
        minusOne, minusTwo = 0, 0

        for i in nums:
            # Current Max rob value is max of 2nd previous house + curr or previous house
            currMax = max(minusTwo + i, minusOne)

            # Increment for next iteration
            minusTwo = minusOne
            minusOne = currMax
            
        return minusOne
