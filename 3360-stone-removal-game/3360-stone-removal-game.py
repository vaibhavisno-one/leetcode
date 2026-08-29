class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove=10
        win=False

        while n>=remove:
            n-=remove
            remove-=1
            win=not win

        return win