# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = self.traverse(root, 0)
        return result

    def traverse(self, node: Optional[TreeNode], result: int) -> int:
        if not node:
            return 0
        return 1 + max(self.traverse(node.left, result), self.traverse(node.right, result))
