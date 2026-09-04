# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse_node(prev, node):
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

            return prev, node

        def find_end_of_group_node(node):
            count = 0
            while node and node.next and count < k:
                node = node.next
                count += 1

            if count == k:
               return node
            else:
                return None

        sentinel = ListNode(next=head)
        prev = sentinel
        left = head
        right = sentinel

        while right and right.next:
            right = find_end_of_group_node(right)
            if right is None:
                break

            # node before left points to right as that will be the new head of the group
            prev.next = right
            
            # set prev for first left to be right's next
            first_in_next_group = right.next
            prev = first_in_next_group
            while left != first_in_next_group:
                prev, left = reverse_node(prev, left)        
                
            # here prev is right, left is first node in next subgroup
            while right != left:
                prev = right
                right = right.next
            right = prev
        
        return sentinel.next