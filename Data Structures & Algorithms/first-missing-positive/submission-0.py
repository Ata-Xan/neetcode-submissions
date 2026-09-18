class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        FMP=1
        nums_dict={k:v for v,k in enumerate(nums) if k>0}

        for i in range(len(nums_dict)):
            if FMP in nums_dict:
                FMP+=1
        else:
            return FMP
    

            