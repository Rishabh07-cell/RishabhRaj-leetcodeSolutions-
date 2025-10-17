class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode])->int:
        if not root:
            return 0
        queue=[(root,0)]
        max_width=0
        while queue:
            level_size=len(queue)
            first_index=queue[0][1]
            last_index=queue[-1][1]
            max_width=max(max_width,last_index - first_index+1)
            next_level=[]
            for node, index in queue:
                if node.left:
                    next_level.append((node.left,2 * index))
                if node.right:
                    next_level.append((node.right,2 * index+1))
            queue=next_level
        return max_width
