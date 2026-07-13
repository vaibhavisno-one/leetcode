class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        result=[]
        

        for i in range(len(mat)):
            count=sum(mat[i])
            heapq.heappush(heap,(count,i))

        while(k>0):
            _,index=heapq.heappop(heap)
            result.append(index)
            k-=1

        return result
        

        

                