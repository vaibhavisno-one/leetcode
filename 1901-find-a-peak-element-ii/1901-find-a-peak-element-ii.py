class Solution(object):
    def findPeakGrid(self, mat):

        row = len(mat)
        col= len(mat[0])


        for i in range(row):
            for j in range (col):

                up=mat[i-1][j] if i>0 else(-1)
                down=mat[i+1][j] if i<row-1 else(-1)
                left=mat[i][j-1] if j>0 else(-1)
                right=mat[i][j+1] if j<col-1 else(-1)

                if mat[i][j]>up and mat[i][j]>down and mat[i][j]>right and mat[i][j]>left:

                    return [i,j]
                    

                
            
        
        