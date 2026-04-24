class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        p=0
        blank=0
        for i in moves:
            if i =="R":
                p=p+1
            elif i=="L":
                p=p-1
            else:
                blank+=1
        
        return abs(p) +blank
