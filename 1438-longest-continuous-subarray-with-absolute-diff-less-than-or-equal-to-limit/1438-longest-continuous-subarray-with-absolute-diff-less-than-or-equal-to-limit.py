from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mad=deque()
        mid=deque()
        i=0
        j=0
        ml=0
        while(i<=j and j<len(nums)):
            while mad and mad[-1]<nums[j]:
                mad.pop()
            mad.append(nums[j])
            while mid and mid[-1]>nums[j]:
                mid.pop()
            mid.append(nums[j])
            while(abs(mad[0]-mid[0]))>limit:
                if nums[i]==mad[0]:
                    mad.popleft()
                if nums[i]==mid[0]:
                    mid.popleft()
                i=i+1
            ml=max(ml,(j-i+1))
            j=j+1
        return ml
            