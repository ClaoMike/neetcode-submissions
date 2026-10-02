# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from collections import deque

        def areTreesEqual(tree1, tree2):
            q1, q2 = deque(), deque()
            q1.append(tree1)
            q2.append(tree2)
            
            while q1 and q2:
                tree1 = q1.popleft()
                tree2 = q2.popleft()

                if tree1.val != tree2.val:
                    return False
                
                if tree1.left:
                    q1.append(tree1.left)
            
                if tree1.right:
                    q1.append(tree1.right)

                if tree2.left:
                    q2.append(tree2.left)
            
                if tree2.right:
                    q2.append(tree2.right)

            if q1 or q2:
                return False

            return True

        queue = deque()
        queue.append(root)
        found = False

        while queue:
            node = queue.popleft()

            if node.val == subRoot.val:
                found = True
                if not areTreesEqual(node, subRoot):
                    found = False
                else:
                    return True
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return found