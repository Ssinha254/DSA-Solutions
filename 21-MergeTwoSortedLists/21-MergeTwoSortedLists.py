# Last updated: 4/21/2026, 11:28:02 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
            
        temp1 = list1
        temp2 = list2 
        temp = ListNode()
        head = temp
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next

            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next

        while temp1:
            temp.next = temp1
            temp= temp.next
            temp1 = temp1.next
            
        while temp2:
            temp.next = temp2
            temp= temp.next
            temp2 = temp2.next
           
        return head.next