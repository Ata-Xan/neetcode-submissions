class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n<2 or n>100000:
            raise ValueError("Length of input array shouldn't be between 2 and 100000")
        if nums[1]<-30 or nums[1]>30:
            raise ValueError("The elements range should be out of this -30 and 30")
        prefix=[1]*n
        suffix=[1]*n
        products=[1]*n
        for i in range(1, n):
            if nums[i]<-30 or nums[i]>30:
                raise ValueError("The elements range should be out of this -30 and 30")
            prefix[i]=prefix[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        
        for i in range(n):
            products[i]=prefix[i]*suffix[i]
        
        return products
            


        
        