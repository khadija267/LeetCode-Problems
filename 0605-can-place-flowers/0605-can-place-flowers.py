class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        i = 0

        while i < size:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
                count += 1
                i += 2  # Skip the next plot since we cannot plant a flower there
            else:
                i += 1

            if count >= n:
                return True

        return False