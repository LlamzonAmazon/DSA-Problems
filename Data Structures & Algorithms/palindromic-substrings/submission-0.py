class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        for i in range(len(s)):

            # Expand from cetner of ODD length palindrome
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                # Update res and expand window
                res += 1
                l -= 1
                r += 1

            # Expand from center of EVEN length palindrome
            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                # Update res and expand window
                res += 1
                l -= 1
                r += 1

        return res