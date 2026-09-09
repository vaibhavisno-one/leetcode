class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        total=0

        i=1000

        while i <=n:
            total+=n-i+1

            i*=1000
        return total