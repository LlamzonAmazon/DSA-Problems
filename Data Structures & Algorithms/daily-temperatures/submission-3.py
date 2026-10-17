class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # [[temperature, index]]
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > stack[-1][0]:
                top, indexTop = stack.pop()
                ans[indexTop] = i - indexTop

            stack.append([temperatures[i], i])

        return ans
            
