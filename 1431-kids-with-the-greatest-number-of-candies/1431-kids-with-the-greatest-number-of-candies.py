class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[False] * len(candies)
        max_candies= max(candies)
        for ind,item in enumerate(candies):
            if item+extraCandies>= max_candies:
                res[ind]=True
        return res