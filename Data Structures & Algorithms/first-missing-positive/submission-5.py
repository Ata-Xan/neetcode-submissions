class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        FMP=1
        nums_set = set(nums)
        # print(list(range(1, len(nums_set)+2)))
        for i in range(1, len(nums_set)+2):
            if not i in nums_set:
                FMP=i
                break
        return FMP
    

            