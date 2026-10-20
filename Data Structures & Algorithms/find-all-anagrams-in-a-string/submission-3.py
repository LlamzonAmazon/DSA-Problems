class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []

        pCount = {}
        for c in p:
            pCount[c] = 1 + pCount.get(c, 0)

        window = {}
        for c in s[:len(p)-1]:
            window[c] = 1 + window.get(c, 0)

        res = []
        
        for r in range(len(p)-1, len(s)):
            
            l = r - (len(p)-1)

            window[s[r]] = 1 + window.get(s[r], 0) # update character count

            if window == pCount:
                res.append(l)

            print(window)

            window[s[l]] -= 1
            if window[s[l]] <= 0:
                del window[s[l]]

        return res            