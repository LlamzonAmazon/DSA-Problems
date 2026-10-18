class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Matrix is sorted - rows are in increasing order, like a list of sorted lists

        # We know we've found the row to search if row[i+1][0] > target
        # Not row[i][0] < target because that doesn't exclude future rows in the matrix 

        # Treat the first item of every row as a node in a BST

        # Select appropriate list -> Binary Search

        n, m = len(matrix), len(matrix[0])

        for i in range(n):

            # Only perform Binary Search in row where 
            # next row's first item is GREATER THAN the target
            if i == n-1 or matrix[i+1][0] > target:

                row = matrix[i]
                l, r = 0, m-1
                mid = m // 2
                
                while l <= r:

                    if row[l] == target or row[mid] == target or row[r] == target:
                        return True

                    # if target must be in left half
                    elif l < target:
                        l += 1
                        r = mid

                    # if target must be in right half
                    else: 
                        r -= 1
                        l = mid

        return False