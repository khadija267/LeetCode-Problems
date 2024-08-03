class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        print('n before',n)
        len_flowerbed=len(flowerbed)-1
        for index, item in enumerate(flowerbed):
            if n==0:
                return True
            if len_flowerbed==0:
                if flowerbed[index]==1:
                    return False
                else:
                    return True
                break
            
            if ((flowerbed[0]==0)&(flowerbed[1]==0)):
                flowerbed[0]=1
                # print('new flowerbed',flowerbed)
                n-=1
            if ((flowerbed[len_flowerbed]==0)&(flowerbed[len_flowerbed-1]==0)) :
                flowerbed[len_flowerbed]=1
                # print('new flowerbed',flowerbed)
                n-=1
            if (index!=0)&(index!=(len_flowerbed)):
                if((flowerbed[index-1]) == 0) & ((flowerbed[index+1]) == 0):
                    if flowerbed[index]!=1:
                        flowerbed[index]=1
                        # print('new flowerbed',flowerbed)
                        n-=1
        print('n after',n)
        if n<=0:
            return True
        else:
            return False