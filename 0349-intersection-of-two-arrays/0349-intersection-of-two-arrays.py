class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen =set(nums1)
        seen2=set()

        inter=[]

        for num in nums2:
            if num in seen:
                seen2.add(num)

        for num in seen2:
            inter.append(num)
        return inter