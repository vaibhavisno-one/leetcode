class Solution(object):
    def searchMatrix(self, matrix, target):
        
        merged= [item for sublist in matrix for item in sublist]

        if target  in merged:
            return True
        
        else:
            return False

        return -1