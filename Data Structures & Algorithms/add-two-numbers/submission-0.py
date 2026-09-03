# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1

        def getLinkedListLength(node) -> int:
            length = 0
            dummy = node
            while dummy:
                length += 1
                dummy = dummy.next

            return length

        def addDigits(*args):
            s = sum(args)
            if s > 9:
                return s-10, 1
            else:
                return s, 0

        if getLinkedListLength(l1) < getLinkedListLength(l2):
            smaller = l1
            larger = l2  
        else:
            smaller = l2
            larger = l1
        
        dummy_small = smaller
        prev = None
        dummy_larger = larger
        remainder = 0

        while dummy_small:
            dummy_larger.val, remainder = addDigits(dummy_small.val, dummy_larger.val, remainder)
            prev = dummy_larger
            dummy_larger = dummy_larger.next
            dummy_small = dummy_small.next
        
        while remainder == 1:
            if dummy_larger is not None:
                dummy_larger.val, remainder = addDigits(dummy_larger.val, remainder)
                
                prev = dummy_larger
                dummy_larger = dummy_larger.next
            else:
                new_node = ListNode(val=1)
                prev.next = new_node
                remainder = 0

        return larger



