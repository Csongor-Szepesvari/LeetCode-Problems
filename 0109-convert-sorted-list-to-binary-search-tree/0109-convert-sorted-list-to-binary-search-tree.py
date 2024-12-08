# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # solution is to recursively break down the list
        # grab the midpoint of the the list, make its left node the sorted_list to BST of list [0:midpoint]

        # to find the midpoint we need to iterate through the LL to find its length

        length = 0
        iterand = head
        while iterand:
            length += 1
            iterand = iterand.next
        
        
        return self.helper(length, head)

    def helper(self, length, head):
        if length <= 0:
            return None
        elif length == 1:
            return TreeNode(head.val)
        index = 0
        iterand = head
        mid = length//2
        while index < mid:
            iterand = iterand.next
            index += 1
        root = TreeNode(val=iterand.val)
        root.left = self.helper(length=mid, head=head)
        len_right = 0
        if length%2==0:
            len_right = mid-1
        else:
            len_right = mid
        root.right = self.helper(length=len_right, head=iterand.next)
        return root
        