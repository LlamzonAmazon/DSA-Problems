class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        # The town judge is one person with no outbound trust and all inbound trusts
        # Build an adjacency matrix to map trusts and their directions
        # Judge is the person (row) with all 0 and is trusted by all n-1

        judge = -1

        # 1 represents trust, 0 otherwise
        trusts, trusted = {}, {}

        for trustor, trustee in trust:

            trusts[trustor-1] = 1 + trusts.get(trustor-1, 0)
            trusted[trustee-1] = 1 + trusted.get(trustee-1, 0)
    
        # Eliminate all people who are not trusted by someone
        trusted_by_all = [1] * n 
        for t in range(n):
            if trusted.get(t, 0) < n-1: # If not trusted by all but themselves
                trusted_by_all[t] = 0

        # Find person who has 0 people they trust
        for c in range(n):
            if trusted_by_all[c] == 1 and trusts.get(c, 0) <= 0:
                judge = c+1

        return judge