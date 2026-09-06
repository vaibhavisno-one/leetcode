class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        Bset=set(banned)
        freq={}

        i,n=0,len(paragraph)

        while i<n:
            while i<n and not paragraph[i].isalpha():
                i+=1
            temp=[]
            while i<n and paragraph[i].isalpha():
                temp.append(paragraph[i].lower())

                i+=1

            word="".join(temp)
            if word and word not in Bset:
                freq[word]=freq.get(word,0)+1
            high=0
            res=""
        for word in freq:
            if freq[word]>high:
                res=word
                high=freq[word]

        return res