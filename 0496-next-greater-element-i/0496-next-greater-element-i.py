class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        arr=[-1]*len(nums2)

        for i in range(len(nums2)):
            while st and nums2[st[-1]]< nums2[i]:

                x=st.pop()
                arr[x]=nums2[i]
            st.append(i)

        ge={}

        for i in range(len(arr)):
            ge[nums2[i]]=arr[i]
        
        res=[]

        for num in nums1:
            res.append(ge[num])

        return res