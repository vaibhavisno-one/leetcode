class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total=0
        prod=1
        for digit in str(n):
            total+=int(digit)
            prod*=int(digit)

        if n % (total+prod) ==0:
            return True
        else:
            return False