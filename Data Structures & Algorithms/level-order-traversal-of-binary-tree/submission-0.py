class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = [] # DFS Stack

        def dfs(node, level):
            if not node:
                return

            if level == len(res): # first time reaching this depth
                res.append([])
            
            res[level].append(node.val)
        
            dfs(node.left, level + 1)  # left before right keeps level order left-to-right
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res