class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        import numpy as np
        result=[]
        max_candies=max(candies)
        new_candies_list= [i+extraCandies for i in candies]
        for i in new_candies_list:
            if i>=max_candies:
                result.append(True)
            else:
                result.append(False)
        return result     
                
        