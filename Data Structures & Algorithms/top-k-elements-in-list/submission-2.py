import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= 0:
            return []

        counts = {}
        freqs = [[] for i in range(len(nums)+1)] # indices correspond to counts

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for n, c in counts.items():
            freqs[c].append(n)

        res = []

        # Iterate through frequencies from most to least frequent
        for i in range(len(freqs)-1, 0, -1):

            if len(freqs[i]) > 0:

                # Add every value in this frequency to res
                for value in freqs[i]: 

                    # Only add if we haven't reached k frequent yet
                    if len(res) >= k: 
                        return res

                    res.append(value)
        
        return res
            