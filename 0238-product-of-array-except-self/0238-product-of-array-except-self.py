class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        zero=nums.count(0)
        if zero>1:
            return [0]*len(nums)
        
        for num in nums:
            if num!=0:
                product=product*num

        result=[]
        for num in nums:
            if zero==1:
                if num==0:
                    result.append(product)
                else:
                    result.append(0)

        
            else:
                result.append(product//num)

        return result

        


        
        
        