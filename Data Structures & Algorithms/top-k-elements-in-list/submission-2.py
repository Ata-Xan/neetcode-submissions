from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not 1<=n<=10**4:
            raise ValueError("The length of the input list should not exceed the range and 10^4 ")
        value_dist=defaultdict(lambda:0)

        for i in nums:
            if not -1000<=i<=1000:
                raise ValueError("The nums list entry should not exceed this range: -1000 and 1000")
            value_dist[i]+=1
        
        if not 1<=k<=len(value_dist):
            raise ValueError("k is not in the range of 1 and number of distinct elements in the entry list")
        
        # print(value_dist)
        value_dist_sorted=dict(sorted(value_dist.items(), key=lambda item: item[1]))


        return list(value_dist_sorted.keys())[len(value_dist_sorted)-k:]
        