from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        i = 0
        max_length = 0
        
        for j in range(len(nums)):
            while max_deque and nums[j] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[j])
            
            while min_deque and nums[j] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[j])
            
            while max_deque[0] - min_deque[0] > limit:
                if nums[i] == max_deque[0]:
                    max_deque.popleft()
                if nums[i] == min_deque[0]:
                    min_deque.popleft()
                i += 1
            
            max_length = max(max_length, j - i + 1)
        
        return max_length
