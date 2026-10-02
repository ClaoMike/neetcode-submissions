# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(x, tree):
            path = []

            while True:
                path.append(tree)

                if x.val > tree.val:
                    tree = tree.right
                elif x.val < tree.val:
                    tree = tree.left
                else:
                    break
                    
            return path
        
        p1 = search(p, root)
        p2 = search(q, root)

        while len(p1) > len(p2):
            p1.pop()
        
        while len(p2) > len(p1):
            p2.pop()

        while p1[-1].val != p2[-1].val:
            p1.pop()
            p2.pop()

        return p1[-1]