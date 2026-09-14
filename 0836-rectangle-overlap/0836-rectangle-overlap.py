class Solution:
    def isRectangleOverlap(self, rect1: List[int], rect2: List[int]) -> bool:
        return (
            rect1[0] < rect2[2] and
            rect1[2] > rect2[0] and
            rect1[1] < rect2[3] and
            rect1[3] > rect2[1]
        )