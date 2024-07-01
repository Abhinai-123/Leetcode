class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c=0
        if len(arr)<3:
            return False
        for i in range(3):
            if arr[i]%2!=0:
                c=c+1
        if c==3:
            return True
        i=0
        j=3
        while(i<j and j<len(arr)):
            if arr[i]%2!=0:
                c=c-1
            
            if arr[j]%2!=0:
                c=c+1
            if c==3:
                return True
            i=i+1
            j=j+1
        return False
            
        