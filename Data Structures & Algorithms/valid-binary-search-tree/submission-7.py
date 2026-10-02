# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            return ( True if not node else ( False if not (low < node.val < high) else (dfs(node.left, low, node.val) and dfs(node.right, node.val, high)) ) )

        return dfs(root, float('-inf'), float('inf'))