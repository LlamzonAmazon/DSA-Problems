class Solution:
    def rob(self, nums: List[int]) -> int:
        
        l, r = 0, 0

        for n in nums:
            curr = max(l + n, r)
            l = r
            r = curr

        return r