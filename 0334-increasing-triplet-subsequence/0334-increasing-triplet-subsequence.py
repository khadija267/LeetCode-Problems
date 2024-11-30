class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # length=len(nums)
        # m1=nums[0]
        # m2=nums[1]
        # for i in range(length-2):
        #     print(f'index: {i} m1: {m1} m2: {m2}')
        #     if m1<m2<nums[i+2]:
        #         return True
        #     else:
        #         m1=nums[i+1]
        #         m2=nums[i+2]
        # return False

        length=len(nums)
        m1=m2=m3=float('inf')
        for i in range(length):
            if m1>=nums[i]:
                m1=nums[i]
                print('m1',m1)
            elif (m2>=nums[i]):
                m2=nums[i]
                print('m2',m2)
            elif m1<m2:
                return True
        return False
                
                
        