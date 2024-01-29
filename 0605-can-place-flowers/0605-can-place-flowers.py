class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        i = 0

        while i < size:
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == size - 1 or flowerbed[i + 1] == 0:
                        count += 1
                        i += 2
                        continue
            i += 1

        return count >= n