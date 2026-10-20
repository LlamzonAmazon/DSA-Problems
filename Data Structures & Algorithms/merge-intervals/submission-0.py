class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0]) # Sort intervals by start value

        ans = [intervals[0]] # Initialize answer with first interval

        for start, end in intervals[1:]:

            lastIntervalEnd = ans[-1][1]

            if start <= lastIntervalEnd: # If start value of interval <= last interval's end value

                # The last interval's end value becomes the current interval's end value
                ans[-1][1] = max(lastIntervalEnd, end)

            else: # Append to answer
                ans.append([start, end])

        return ans            