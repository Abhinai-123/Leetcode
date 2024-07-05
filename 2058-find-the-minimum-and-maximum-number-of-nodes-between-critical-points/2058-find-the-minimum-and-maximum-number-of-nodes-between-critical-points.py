# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp=head
        q=1
        while(temp):
            temp=temp.next
            q=q+1
        if q <= 3:
            return [-1,-1]
        p1=head
        p2=head.next
        p3=head.next.next
        l=[]
        c=2
        ans=[]
        while(p3):
            if p2.val>p1.val and p2.val>p3.val:
                l.append(c)
            if p2.val < p1.val and p2.val < p3.val:
                l.append(c)
            c=c+1
            p1=p1.next
            p2=p2.next
            p3=p3.next
        if len(l)<2:
            return [-1,-1]
        mi=float('inf')
        ma=float('-inf')
        i=0
        j=1
        while(j<len(l)):
            if l[j]-l[i] <mi:
                mi=l[j]-l[i]
            i=i+1
            j=j+1
        ans.append(mi)
        ans.append(l[len(l)-1]-l[0])
        return ans
            