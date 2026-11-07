class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Algorithm only needs to track the best possible totals for the two previous states

        prev, prevPrev = 0, 0

        # Iterate through nums
        for n in nums:

            # Set current max rob value to either max of prevPrev + current house OR prevPrev
            # We basically maintain the max of indices and use previously computed
            curr = max(prevPrev + n, prev) 

            prevPrev = prev
            prev = curr

        return prev