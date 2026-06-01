class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        end=len(nums)-k

        result=[]

        result= nums[end:]+nums[:end]

        for i in range(len(nums)):
            nums[i]=result[i]

        
