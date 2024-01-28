class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[False] * len(candies)
        print(res)
        for ind,item in enumerate(candies):
            if item+extraCandies>= max(candies):
                res[ind]=True
        return res