class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=[]
        d={}
        d2={}
        r={}
        for i in nums1:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        for i in nums2:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]=d2[i]+1
        for i,j in d.items():
            if i in d2:
                r[i]=min(j,d2[i])
        for i,j in r.items():
            for k in range(j):
                l.append(i)
        return l
        