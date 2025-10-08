class Solution:
    def arrangeCoins(self, n: int) -> int:
        sm=st=0
        for i in range(1,n+1):
            sm+=i
            if sm>n:
                break
            st+=1
        return st 
