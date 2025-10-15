class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        ld=[]
        prev=None
        while root or ld:
            while root:
                ld.append(root)
                root=root.left
            root=ld.pop()
            if prev is not None and root.val<=prev:
                return False
            prev=root.val
            root=root.right
        return True
