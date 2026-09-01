from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}

        if len(nums) < 0 or len(nums) > 10**5:
            raise ValueError("nums length must be between 1 and 10^5")

        for i, value in enumerate(nums):

            if value < -(10**9) or value > 10**9:
                raise ValueError("Each number must be between -10^9 and 10^9")

            if value in numbers:
                return True

            numbers[value] = i

        return False