# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(next=list1)

        before_dummy1 = sentinel
        dummy1 = list1
        dummy2 = list2

        while dummy1:
            while dummy2 and dummy2.val <= dummy1.val:
                to_insert = dummy2
                dummy2 = dummy2.next
                to_insert.next = dummy1
                before_dummy1.next = to_insert
                before_dummy1 = to_insert

            before_dummy1 = dummy1
            dummy1 = dummy1.next
        
        if dummy2:
            before_dummy1.next = dummy2
                
        return sentinel.next