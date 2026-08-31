class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i, value in enumerate(nums):
            compliment_of_target=target-value
            if compliment_of_target in visited:
                return [visited[compliment_of_target], i]
            else:
                visited[value]=i
        