# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Adjacency list INDICES correspond to the value of the node
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        visited = {}

        def dfs(root):

            if root in visited:
                return visited[root]

            newNode = Node(root.val)
            visited[root] = newNode

            # For every node in it's neighbors, we just
            # If no neighbors, then the pop doesn't enter the for loop, and
            # the while loop now breaks because the stack is now empty
            # MUST CHECK IF NODE IS VISITED
            for neighbor in root.neighbors:
                newNode.neighbors.append( dfs(neighbor) )

            return newNode
        
        return dfs(node)

        