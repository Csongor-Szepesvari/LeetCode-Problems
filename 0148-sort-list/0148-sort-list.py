# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# In order to sort a linked list with divide and conquer, we'll do merge-sort

# that is find the halfway point, sort the sublist, create a newlist by combining terms from new sorted lists
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # base cases: length is equal to 1
        if not head:
            return None

        if head.next == None:
            return head
            
        # otherwise we find halfway point and execute a sort on both

        def findHalfAndSever(head):
            # double iterates through to the middle of linked list to return the halfway head
            double = head
            previous = None
            while double != None and double.next != None:
                previous = head
                head = head.next
                double = double.next.next
            
            # sever the connection here
            previous.next = None
            return head

        front = head
        back = findHalfAndSever(head)
        # need to sever connection between front and back

        def merge_sorted_lists(list1, list2):
            # compares the first element of either list, and creates a sorted list as a result
            # O(n_1 + n_2) in the size of the lists
            new_list = ListNode()
            new_head = new_list
            while list1 and list2:
                #print("comparing", list1.val, "and", list2.val)
                if list1.val <= list2.val:
                    new_list.val = list1.val
                    list1 = list1.next
                else:
                    new_list.val = list2.val
                    list2 = list2.next
                if list1 and list2:
                    new_list.next = ListNode()
                    new_list = new_list.next
                else:
                    if list1:
                        new_list.next = list1
                    else:
                        new_list.next = list2
                #print("current list is", new_head)



            return new_head

        list1 = self.sortList(front)
        list2 = self.sortList(back)

        return merge_sorted_lists(list1,list2)
        