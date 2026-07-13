class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []

        
        for i in range(len(score)):
            heapq.heappush(heap, (-score[i], i))

        ans = [""] * len(score)
        place = 1

        while heap:
            _, idx = heapq.heappop(heap)

            if place == 1:
                ans[idx] = "Gold Medal"
            elif place == 2:
                ans[idx] = "Silver Medal"
            elif place == 3:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(place)

            place += 1

        return ans