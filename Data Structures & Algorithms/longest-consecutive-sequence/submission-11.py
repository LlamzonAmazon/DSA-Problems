
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        current_longest = 1
        longest = 1

        for i in range(1, len(nums)):
            
            if nums[i] == nums[i-1]:
                continue

            elif nums[i] == nums[i-1]+1:
                current_longest += 1

            else:
                current_longest = 1

            longest = max(longest, current_longest)

        return longest
