class Solution:
    def countGoodRotations(self, nums: List[int]) -> int:
        n = len(nums)
        m = n // 2
        S = sum(nums)
        w = sum(nums[:m])
        cnt = 0
        for k in range(n):
            if 2 * w > S:
                cnt += 1
            if k + 1 < n:
                w += nums[(k + m) % n] - nums[k]
        return cnt