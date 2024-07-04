# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        c=1
        temp=head
        while(temp.next):
            c=c+1
            temp=temp.next
        
        k=(k%c)
        if k==0:
            return head
        temp.next=head
        for i in range(abs(c-k)):
            temp=temp.next
        nh=temp.next
        temp.next=None
        return nh








        