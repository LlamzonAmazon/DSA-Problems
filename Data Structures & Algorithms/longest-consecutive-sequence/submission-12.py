class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        longest, curr = 0, 0

        for num in nums:
            if num-1 not in nums: # Start of consecutive sequence

                count = 1
                while num + count in nums:
                    count += 1
                
                longest = max(longest, count)

        return longest
