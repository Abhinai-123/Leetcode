class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        n=len(nums)
        fc=0
        oc=0
        while(i<=j and j<n):
            if nums[j]%2!=0:
                oc=oc+1

            while(oc>k):
                if nums[i]%2!=0:
                    oc=oc-1
                i=i+1

            if oc == k:
                temp = i
                while temp <= j and nums[temp] % 2 == 0:
                    temp += 1
                    fc += 1
                fc += 1  
            
            j=j+1
        return fc