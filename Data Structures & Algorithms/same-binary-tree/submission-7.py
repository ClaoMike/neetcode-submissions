# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        from collections import deque

        queue_p, queue_q = deque(), deque()

        queue_p.append(p)
        queue_q.append(q)

        while queue_p and queue_q:
            p = queue_p.popleft()
            q = queue_q.popleft()

            if (not p and q) or (p and not q):
                return False

            if q and p and q.val != p.val:
                return False
            
            if p:
                queue_p.append(p.left)
                queue_p.append(p.right)
            if q:
                queue_q.append(q.left)
                queue_q.append(q.right)

        if queue_p or queue_q:
            return False
        
        return True