class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in range(len(logs)):
            if logs[i]=="./":
                pass
            elif logs[i]=="../":
                if c>0:
                    c=c-1
            else:
                c=c+1
        return c
        