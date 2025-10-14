# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        
        def right_side(node,depth):
            if node is None:
                return []
            if depth==len(result):
                result.append(node.val)
            right_side(node.right,depth+1)
            right_side(node.left,depth+1)
        right_side(root,0)
        return result


        
