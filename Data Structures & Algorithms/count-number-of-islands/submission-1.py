class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        
        # This is a graph problem where we are trying to find a connected graph within a matrix 

        # Since we can assume the grid is surrounded by 0's, we can define an edge node as
        # A node where all of it's unvisited neighbors are 0
        # Must check that the node is unvisited AND that it is a 1

        ans = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        # BFS is used here purely to mark nodes as visited
        def BFS(r: int, c: int):

            queue = collections.deque()
            queue.append( (r, c) )
            visited.add( (r,c) )

            while queue:
                row, col = queue.popleft() # Pop from head of queue
                print(row, col)

                # Identify neighbors and append to queue
                # Check all surrounding nodes: (x+1, y), (x, y+1), (x-1, y), (x, y-1)
                for dr, dc in [ (1, 0), (0, 1), (-1, 0), (0, -1) ]:

                    # If neighbor is an unvisited 1 and within bounds
                    if (row+dr in range(rows) and col+dc in range(cols) and
                       grid[row+dr][col+dc] == "1" and (row+dr, col+dc) not in visited):

                        queue.append( (row+dr, col+dc) )
                        visited.add( (row+dr, col+dc) )
                    

        for r in range(rows):
            for c in range(cols):
                
                # Only run BFS on unvisited 1's
                if grid[r][c] == "1" and (r, c) not in visited:
                   BFS(r, c)
                   ans += 1

        return ans

        



