class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        dup=[0]*len(nums)
        j=0

        for i in range(len(nums)):

            if nums[i]!=0:
                dup[j] = nums[i]
                j+=1

            
        for i in range(len(nums)):
            nums[i]=dup[i]


        return nums