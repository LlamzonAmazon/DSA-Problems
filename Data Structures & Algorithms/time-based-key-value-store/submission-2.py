class TimeMap:

    def __init__(self):
        self.timeMap = {} # Hashmap keyed by name

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timeMap:
            self.timeMap[key] = [[value, timestamp]]
        else:
            # Simple append to end because timestamps are strictly increasing 
            self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        timestamps = self.timeMap.get(key, [])      

        # Binary Search
        l, r = 0, len(timestamps)-1

        while l <= r:
            mid = (l+r) // 2

            if timestamps[mid][0] == timestamp:
                return timestamps[mid][0] 

            elif timestamps[mid][1] <= timestamp: # Value is a current/previous timestamp
                res = timestamps[mid][0] # Take it 
                l = mid+1

            else: 
                r = mid-1                

        return res
            