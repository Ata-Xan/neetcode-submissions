class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_number=len(nums)

        if numbers_number==0:
            return 0
        # numbers_in_dictionary = {key:index for index, key in enumerate(nums)}
        numbers = set(nums)
        LCS=1
        for value in numbers:
            current_LCS=1
            # beginning of the sequence
            if value-1 not in numbers:
                i=1
                while value+i in numbers:
                    current_LCS+=1
                    i+=1
                LCS = max(LCS, current_LCS)
            else:
                continue
        
        return LCS
                    
        
            

        