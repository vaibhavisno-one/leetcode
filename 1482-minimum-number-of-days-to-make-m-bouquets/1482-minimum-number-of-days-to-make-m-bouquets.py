class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)
        total = m*k
        if total>n:
            return -1
        low=min(bloomDay)
        high=max(bloomDay)


        def canMake(i):
            count=0
            b=0
            for j in bloomDay:
                if i>=j:
                    count+=1
                    if count==k:
                        b+=1
                        count=0
                else:
                    count =0
            return b>=m
                    

        while(low<high):
            mid=(low+high)//2

            if canMake(mid):
                high=mid
            else:
                low=mid+1
            
        return low
        
        
            



        