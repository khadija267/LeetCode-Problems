class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_length = 0
        a=len(str1)
        b=len(str2)
        while b>0:
            # a=b
            remainder=a%b
            a=b
            b=remainder
          
        gcd_length=a
        return str1[:gcd_length]
    
