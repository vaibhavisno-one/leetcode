class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        

        arr=[]

        for num in nums1:

            found=False
            for i in range(len(nums2)):
                if num==nums2[i]:
                    for j in range(i+1,len(nums2)):
                        if nums2[j]>num:
                            arr.append(nums2[j])
                            found=True
                            break

                    if not found:
                        arr.append(-1)
                    break
        return arr

        