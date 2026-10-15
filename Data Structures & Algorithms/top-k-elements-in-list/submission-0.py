import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for i in nums:
            if i not in counts.keys():
                counts[i] = 1
            else:
                counts[i] += 1

        heap = []
        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap) # Pop smallest element

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
        

        

