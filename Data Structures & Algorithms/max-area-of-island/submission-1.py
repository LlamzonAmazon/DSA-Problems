from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        # use a hashmap to store whether or not i've visited a node
        # visited = { (i, j) : True }
        # if (i, j) not in visited: 
        # Every time we iterate, mark this position as visited visited[(i, j] = True
        
        # Use BFS queue to explore islands

        for i in range(ROWS):

            for j in range(COLS):
                
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                
                area = 0
                visited.add((i,j))

                queue =  deque([[i, j]]) # Initialize BFS queue
                while queue:

                    r, c = queue.popleft()
                    area += 1

                    # Add all of it's neighbors to queue ONLY IF it's an unvisited 1 
                    for dr, dc in dirs:

                        x, y = r+dr, c+dc
                        if ( x in range(ROWS) and y in range(COLS) and
                             grid[x][y] == 1 and (x, y) not in visited ):

                            queue.append([x, y])
                            visited.add((x, y))

                maxArea = max(maxArea, area)

        return maxArea