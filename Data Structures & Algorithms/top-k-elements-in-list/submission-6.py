import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Build hashmap of counts
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        # Maintain a min heap of size k in order to keep top f frequencies in the heap
        # If top of heap LT the one we're inserting, then pop and push (replace)
        # Heap is keyed by freqeuncy in a tuple of (freq : num)

        heap = []
        for num, count in counts.items():

            if len(heap) < k:
                heapq.heappush(heap, (count, num))
                continue

            # Only need to consider popping if the heap is at capacity k
            if count > heap[0][0]: 
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))
                
        res = []
        for item in heap:
            res.append(item[1])
        
        return res