class Solution:
    def reverseDegree(self, s: str) -> int:
        alpha='abcdefghijklmnopqrstuvwxyz'
        revMap={}
        for i in range(len(alpha)-1,-1,-1):
            revMap[alpha[i]]=26-i
        total=0
        for i,char in enumerate(s,1):
            
            total += i * revMap[char]
        return total