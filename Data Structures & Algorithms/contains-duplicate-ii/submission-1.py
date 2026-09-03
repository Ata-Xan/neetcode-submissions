class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_dist={}
        for i in range(len(nums)):
            if i>k:
                smallest_index = min(value_dist,key=value_dist.get)
                del value_dist[smallest_index]
            if nums[i] in value_dist:
                return True
            else:
                value_dist[nums[i]]=i
            
        return False

        