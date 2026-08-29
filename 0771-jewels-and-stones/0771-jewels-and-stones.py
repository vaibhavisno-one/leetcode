class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq={}
        count=0
        for char in stones:
            freq[char]=freq.get(char,0)+1

        for char, value in freq.items():
            if char in jewels:
                count+=freq[char]
        
        return count