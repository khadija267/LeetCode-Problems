class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        import numpy as np
        result=[]
        max_candies=max(candies)
        # new_candies_list= [i+extraCandies for i in candies]
        new_candies_list=np.array(candies)+extraCandies
        print(new_candies_list)
        for i in new_candies_list:
            if i>=max_candies:
                result.append(True)
            else:
                result.append(False)
        return result  