class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return [] 
        result=[]
        queue=([root])
        left_to_right=True
        while queue:
            level_size=len(queue)
            level=[]
            for i in range(level_size):
                node=queue[0]
                queue=queue[1:]
                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
            left_to_right= not left_to_right
        return result
