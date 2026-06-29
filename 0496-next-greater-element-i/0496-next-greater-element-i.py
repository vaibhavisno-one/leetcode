class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        ans=[-1]*len(nums2)
        st=[]

        for i in range(len(nums2)-1,-1, -1):

            while st and st[-1]<=nums2[i]:
                st.pop()
            if st:
                ans[i]=st[-1]

                
                
            st.append(nums2[i])

        dic={}

        for i in range(len(nums2)):
            dic[nums2[i]]=ans[i]

        result=[]

        for num in nums1:
            result.append(dic[num])    
        
        return result