class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        if len(heights) <= 1:
            return -1

        # USE TWO-POINTER
        l, r = 0, len(heights)-1
        maxVol = 0

        while l < r:

            volume = (r-l) * (min(heights[l], heights[r]))

            maxVol = max(maxVol, volume)

            if (heights[l] < heights[r]): # Update bottleneck index
                l+=1
            else:
                r-=1 
            
        return maxVol