# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque, defaultdict
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []
        h = defaultdict(list)
        queue = deque()
        queue.append( (root, 0) )

        while queue:
            node, level = queue.popleft()
            h[level].append(node.val)

            if node.left:
                queue.append( (node.left, level + 1) )

            if node.right:
                queue.append( (node.right, level + 1) )

        i = 0
        while True:
            if i in h.keys():
                answer.append(h[i])
                i += 1
            else:
                break

        return answer