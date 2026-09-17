class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_number=len(nums)

        if numbers_number==0:
            return 0
        numbers_in_dictionary = {key:index for index, key in enumerate(nums)}

        
        LCS=1
        for value, index in numbers_in_dictionary.items():
            
            current_LCS=1
            # beginning of the sequence
            if value-1 not in numbers_in_dictionary:
                i=1
                while value+i in numbers_in_dictionary:
                    current_LCS+=1
                    i+=1
                if current_LCS>LCS:
                    LCS=current_LCS
            else:
                continue
        
        return LCS
                    
        
            

        