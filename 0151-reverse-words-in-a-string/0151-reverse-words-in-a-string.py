class Solution(object):
    def reverseWords(self, s):
        s=s.strip()

        word=s.split()

        word.reverse()

        return " ".join(word)
        