class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique=[]

        for i in nums:
            if i not in unique:
                unique.append(i)


        for i in range(0,len(unique)):
            nums[i]=unique[i]


        return len(unique)