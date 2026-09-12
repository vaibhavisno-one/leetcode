class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        ans=0
        distinct=set(nums)
        for x in distinct:
            idx=[]
            for i,j in enumerate(nums):
                if j==x:
                    idx.append(i)
            if len(idx)==3 and idx[1]-idx[0] == idx[2]-idx[1]:
                ans+=1

        return ans
                