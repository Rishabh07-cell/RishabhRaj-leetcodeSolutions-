class Solution:
    def shipWithinDays(self, weights: List[int], d: int) -> int:
        def check(ar):
            days,cur = 1,0
            for i in weights:
                if cur+i<=ar:
                    cur+=i
                else:
                    days+=1
                    cur=i
            return days
        l,r=max(weights),sum(weights)
        while l<r:
            mid=(l+r)//2
            days=check(mid)
            if days<=d:
                r=mid
            else:
                l=mid+1
        return r

        
