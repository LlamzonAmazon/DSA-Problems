class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest = 0
        window = set()

        for r in range(len(s)):

            if s[r] in window:
                
                while s[r] in window:
                    window.discard(s[l]) # Remove duplicate at left of window
                    l += 1 # Slide window - l acts as a removal pointer
            
            window.add(s[r])   
            longest = max(longest, (r-l)+1) # Set longest substring count

        return longest
            