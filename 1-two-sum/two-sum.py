class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        indices = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in indices.keys():
                return [i, indices[complement]]

            else:
                indices[nums[i]] = i
            