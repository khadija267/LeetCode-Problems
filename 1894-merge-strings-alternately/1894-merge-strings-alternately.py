class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        len_w1,len_w2 = len(word1), len(word2)
        max_len,min_len= max(len_w1, len_w2), min(len_w1, len_w2)
        print('min_len: ',min_len)
        min_w = word1 if len_w1 == min_len else word2
        max_w=  word1 if len_w1 == max_len else word2
        print("max word is:", max_w)
        print("min word is:", min_w)
        for index, letter in enumerate(min_w[:min_len]):

            res.append(word1[index])
            res.append(word2[index])

        res.append(max_w[min_len:])
        print(res)

        print("".join(res))
        return "".join(res)
        