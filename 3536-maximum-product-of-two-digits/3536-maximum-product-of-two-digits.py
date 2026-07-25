class Solution:
    def maxProduct(self, n: int) -> int:
        sorted_num=sorted(str(n))

        return int(sorted_num[-1]) * int(sorted_num[-2])