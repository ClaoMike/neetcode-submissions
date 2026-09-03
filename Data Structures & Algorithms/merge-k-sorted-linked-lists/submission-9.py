# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge2lists(l1, l2):
            sentinel = ListNode(next=l1)
            prev = sentinel
            dummy1 = l1
            dummy2 = l2

            while dummy1:

                while dummy2 and dummy2.val <= dummy1.val:
                    prev.next = dummy2
                    dummy2 = dummy2.next
                    prev.next.next = dummy1
                    prev = prev.next

                prev = dummy1
                dummy1 = dummy1.next

            if dummy2 is not None:
                prev.next = dummy2
            
            return sentinel.next
        
        def solve(arr):
            if len(arr) == 1:
                return arr[0]

            mid = len(arr)//2
            left_half, right_half = arr[0:mid], arr[mid:len(arr)]

            left_result = solve(left_half)
            right_result = solve(right_half)

            return merge2lists(left_result, right_result)

        if len(lists) == 0:
            return None

        elif len(lists) == 1:
            return lists[0]

        else:
            return solve(lists)