class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """


        freq={}
        for i in s:
            # val=s.count(i)

            # freq[i]=val

            freq[i] =freq.get(i,0)+1


            sorted_chars = sorted(freq, key=freq.get, reverse=True)

            
            ans = ""

            for ch in sorted_chars:
                ans += ch * freq[ch]

        return ans
            


            
        