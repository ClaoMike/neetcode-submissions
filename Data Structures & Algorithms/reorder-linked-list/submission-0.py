# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        def printLinkedList(node):
            dummy = node
            while dummy:
                print(f"{dummy.val} -> ", end="")
                dummy = dummy.next
            print()
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast == None:
            list2 = slow
            prev.next = None
        else:
            list2 = slow.next
            slow.next = None

        # print(slow.val)
   
        # printLinkedList(head)
        # printLinkedList(list2)

        prev = None
        dummy = list2
        while dummy:
            next_node = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = next_node
        
        reversed_list = prev
        # printLinkedList(reversed_list)

        dummy = head
        while dummy and reversed_list:
            next_node = dummy.next
            dummy.next = reversed_list
            reversed_list = reversed_list.next
            dummy.next.next = next_node
            dummy = dummy.next.next
