class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        c=0
        ml=0
        for i in range(n):
            if nums[i]==0:
                c=c-1
            if nums[i]==1:
                c=c+1
            if c==0:
                ml=max(ml,i+1)
            if c in d:
                ml=max(ml,i-d[c])
            if c not in d:
                d[c]=i
        return ml
                