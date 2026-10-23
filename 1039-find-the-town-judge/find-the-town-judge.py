class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        # The town judge is one person with no outbound trust and all inbound trusts
        # Build an adjacency matrix to map trusts and their directions
        # Judge is the person (row) with all 0 and is trusted by all n-1

        judge = -1

        # Initialize matrix with 0's in an n•n matrix 
        trust_matrix = [[0] * n for _ in range(n)] # index = label-1 
        
        # Iterate through trust and build matrix
        for i in range(len(trust)):
            trustor_label = trust[i][0]-1
            trustee_label = trust[i][1]-1

            trust_matrix[trustor_label][trustee_label] = 1

        # 1 Represents still being a judge candidate, judge is index with value 1
        trusted = [1] * n 

        # Search for row of all 0's and a column of all 1's except for in that column
        for r in range(n):
            for c in range(n):

                # Has been trusted by all until now AND is not trusted by person r+1
                if trusted[c] == 1 and trust_matrix[r][c] == 0 and r != c:
                    trusted[c] = 0

        print(trusted)

        # Search for person with all 0 trust and is trusted by all
        for r in range(n):
            if 1 not in trust_matrix[r] and trusted[r] == 1:
                judge = r+1

        return judge