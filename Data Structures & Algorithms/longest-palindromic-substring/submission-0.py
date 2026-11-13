class Solution:
    def longestPalindrome(self, s: str) -> str:

        res, lenRes = 0, 0

        for i in range(len(s)):

            # Expand from cetner of ODD length palindrome
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ((r-l) + 1) > lenRes: # Current palindrome is greater than the current longest

                    # Store center and length of of palindrome
                    res = l
                    lenRes = (r-l)+1
                
                # Expand window
                l -= 1
                r += 1

            # Expand from center of EVEN length palindrome
            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ((r-l) + 1) > lenRes: # Current palindrome is greater than the current longest

                    # Store center and length of of palindrome
                    res = l
                    lenRes = (r-l)+1
                
                # Expand window
                l -= 1
                r += 1

        return s[res : (res+lenRes)]