class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        list(s)

        l = 0
        longest = 0
        window_counts = {}

        for r in range(len(s)):
            
            # Update s[r]'s count in dictionary
            if s[r] not in window_counts.keys():
                window_counts[s[r]] = 1
            else:
                window_counts[s[r]] += 1
            
            highest_count = max(window_counts.values())

            while (r-l+1) - highest_count > k:
                window_counts[s[l]] -= 1                    # update counts 
                l += 1                                      # increment left pointer
                highest_count = max(window_counts.values()) # recalculate highest_count

            longest = max(longest, r-l+1)

        return longest

