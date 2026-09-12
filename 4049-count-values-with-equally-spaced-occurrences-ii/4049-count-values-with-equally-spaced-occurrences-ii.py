class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos = {}
        for i, v in enumerate(nums):
            if v in pos:
                pos[v].append(i)
            else:
                pos[v] = [i]

        ans = 0
        for idx in pos.values():
            if len(idx) < 3:
                continue
            d = idx[1] - idx[0]
            good = True
            for k in range(2, len(idx)):
                if idx[k] - idx[k-1] != d:
                    good = False
                    break
            if good:
                ans += 1
        return ans