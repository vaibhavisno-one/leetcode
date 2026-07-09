class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]

        result=[]
        for i in arr:
            dist=abs(i-x)

            heapq.heappush(heap,(-dist,-i))

            if len(heap)>k:
                heapq.heappop(heap)

            
        for dist,i in heap:
            result.append(-i)


        result.sort()
        return result