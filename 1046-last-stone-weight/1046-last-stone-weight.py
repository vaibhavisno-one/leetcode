class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap=[-stone for stone in stones]

        heapq.heapify(heap)

        if len(heap) == 1:
            return -heapq.heappop(heap)

        while len(heap) >1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)

            new=y-x
            if new != 0:
                heapq.heappush(heap,-new)
        return -heap[0] if heap else 0