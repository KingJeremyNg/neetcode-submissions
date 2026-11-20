# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Running list of parent nodes to process
        stack = [root]

        # While there are nodes
        while stack:
            # Grab node on top of stack
            node = stack.pop()
            # Swap children
            node.left, node.right = node.right, node.left

            # If there are children, add to stack for processing
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root