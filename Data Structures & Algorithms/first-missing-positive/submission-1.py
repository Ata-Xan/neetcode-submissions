class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        FMP=1
        # nums_dict={k:v for v,k in enumerate(nums) if k>0}
        nums_set = set(nums)
        for i in range(len(nums_set)):
            if FMP in nums_set:
                FMP+=1
        
        return FMP
    

            