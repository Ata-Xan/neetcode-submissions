class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # if not 2<=n<=100000:
        #     raise ValueError("Length of input array shouldn't be between 2 and 100000")
        # if not -30 <= nums[1] <= 30:
        #     raise ValueError("The elements range should be out of this -30 and 30")
        # prefix=[1]*n
        # suffix=[1]*n
        # products=[1]*n
        # for i in range(1, n):
        # if not -30 <= nums[i] <= 30:
        #         raise ValueError("Each element must be between -30 and 30")
        #     prefix[i]=prefix[i-1]*nums[i-1]
        
        # for i in range(n-2,-1,-1):
        #     suffix[i]=suffix[i+1]*nums[i+1]
        
        # for i in range(n):
        #     products[i]=prefix[i]*suffix[i]
        # ======================================== second method (division based)
        n=len(nums)
        if not 2<=n<=100000:
            raise ValueError("Length of input array shouldn't be between 2 and 100000")
        products=[0]*n
        all_array_products=1
        zero_index=-1
        count=0
        for i in range(n):
            if not -30 <= nums[i] <= 30:
                raise ValueError("Each element must be between -30 and 30")
            if nums[i]==0:
                count+=1
                if count>1:
                    return [0]*n
                zero_index=i
                continue 
            all_array_products=all_array_products*nums[i]
        if zero_index>-1:
            products[zero_index]=all_array_products
            return products
        else:
            for i in range(n):
                products[i]=all_array_products//nums[i]
        return products
            


        
        