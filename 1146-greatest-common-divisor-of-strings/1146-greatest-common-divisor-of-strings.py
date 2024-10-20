class Solution:
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     if str1 + str2 != str2 + str1:
    #         return ""
    #     a=len(str1)
    #     b=len(str2)
    #     while b>0:
    #         # remainder=a%b
    #         # a=b
    #         # b=remainder
    #         a,b=b,a%b
    #     gcd_length=a
    #     return str1[:gcd_length]
    
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     # remove duplicated strings in order
    #     # str2="".join(sorted(set(str2),key=str2.index))
    #     # substring= []
    #     substring=""
    #     max_str= str1 if len(str1)>len(str2) else str2
    #     for i in range( len(max_str)-1):
    #         print (i)
    #         if (max_str[i]==max_str[i+1]):
    #             continue
    #         if (max_str[0]==max_str[i+1]):
    #             substring=max_str[0:i+1]
    #             break

    #     print("substring:",substring)
    #     if substring:
    #         str1 = "".join(str1.rsplit(substring))
    #     else:
    #         str1 = ""
    #     print("str1:",str1)
    #     return substring if not str1 else ""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_len =len(str2)
        substring = ""

        for i in range(1, min_len + 1):
            test_substring = str1[:i]
            print('test_substring:', test_substring)
            
            if (test_substring * (len(str1)//i) == str1 and
                test_substring * (len(str2)//i) == str2):
                substring = test_substring

        return substring