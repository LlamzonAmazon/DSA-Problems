class Solution:
    def numDecodings(self, s: str) -> int:

        # Build compute cache
        cache = {len(s) : 1}

        def dfs(i):

            if i in cache: # Already computed character
                return cache[i]
            elif s[i] == "0": # Leading 0
                return 0

            # ACCOUNTS FOR SINGLE DIGIT CHARACTERS
            count = dfs(i+1) # dfs(i+1) = # ways to decode after looking at one character

            # Check if digits can be COMBINED into a single character
            if (i+1) < len(s) and ( s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456" ):
                count += dfs(i + 2)

            cache[i] = count

            return count

        return dfs(0)