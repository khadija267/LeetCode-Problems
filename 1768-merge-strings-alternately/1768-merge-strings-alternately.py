class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2 = len(word2)
        result=""
        min_len=min(len1,len2)
        for i in range(min_len):
            result=result+word1[i]+word2[i]

        if len1>len2:
            result=result+word1[min_len:]
        else:
            result=result+word2[min_len:]
        return result