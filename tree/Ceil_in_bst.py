class Solution:
    def findCeil(self,root, x):
        # code here
        ceil=-1
        while root:
            if root.data==x:
                return x 
            elif root.data<x:
                root=root.right
            else:
                ceil=root.data
                root=root.left
        return ceil
