# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        prev = None
        first = head
        second = head.next
        new_head = second

        
        while second != None:

            print(first)
            print(second)
            print()
            first.next = second.next
            second.next = first
            if prev:
                prev.next = second
            prev = first
            print(first)
            print(second)
            print()
            print()
            first = first.next
            #print(first)
            if first != None:
                second = first.next
            else:
                second = None
            
        return new_head