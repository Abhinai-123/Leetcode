# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1=head.next
        ptr2=ptr1.next
        if ptr2==None:
            return ptr1
        while(ptr1 and ptr2):
            while(ptr2 and ptr2.val!=0):
                ptr1.val  =ptr1.val + ptr2.val
                ptr2=ptr2.next
            ptr1.next=ptr2.next
            ptr1=ptr1.next
            if ptr1:
                ptr2=ptr1.next
        return head.next