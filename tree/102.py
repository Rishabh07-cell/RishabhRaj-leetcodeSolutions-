class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root):
        if root is None:
            return []
        result=[]
        queue=[root] 
        while queue:
            level_size=len(queue)
            level=[]
            for i in range(level_size):
                node=queue[0]
                queue=queue[1:]  
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
