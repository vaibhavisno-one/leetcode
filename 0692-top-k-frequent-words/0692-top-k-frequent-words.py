class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=Counter(words)


        heap=[]

        for word, count in freq.items():
            heapq.heappush(heap,(-count,word))


        ans=[]


        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans