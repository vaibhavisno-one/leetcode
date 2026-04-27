class Solution(object):
    def searchMatrix(self, matrix, target):
        
        merged= [item for row in matrix for item in row]


        merged.sort()
        low=0
        high=len(merged)-1

        while(low<=high):
            mid=(low+high)//2

            if merged[mid]==target:
                return True
            
            elif merged[mid]>target:
                high=mid-1
            else:
                low=mid+1
            
        return False
        
        
        return -1

        