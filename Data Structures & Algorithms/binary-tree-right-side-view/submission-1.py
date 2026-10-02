# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        from collections import deque

        answer = []
        queue = deque()
        queue.append( (root, 0) )

        while queue:
            node, depth = queue.popleft()

            if not queue or queue[0][1] != depth:
                answer.append(node.val)

            if node.left:
                queue.append( (node.left, depth + 1))

            if node.right:
                queue.append( (node.right, depth + 1) )

        return answer