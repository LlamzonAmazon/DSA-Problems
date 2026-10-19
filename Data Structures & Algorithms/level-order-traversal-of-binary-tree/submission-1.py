# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            
            sublist = [] 

            for i in range(len(queue)): # Build sublist from REMAINING items in queue
                node = queue.popleft() # Pop top of queue if it exists

                if node:
                    sublist.append(node.val) # Append node value to sublist

                    # Append all of node's children to queue
                    queue.append(node.left) 
                    queue.append(node.right)

                # Exits when sublist is populated with all nodes of the level 
                # which were to be popped from queue

            if sublist:
                ans.append(sublist)

        return ans
