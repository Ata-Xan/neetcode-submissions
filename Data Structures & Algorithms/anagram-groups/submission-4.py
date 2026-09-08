from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hashmap=defaultdict(list)
        for i in strs:
            char_dist=[0]*26
            for j in list(i): 
                char_dist[ord(j)-ord('a')]+=1
            key = tuple(char_dist)

            # if key not in anagram_hashmap:
            #     anagram_hashmap[key]=[i]
            # else:
            anagram_hashmap[key].append(i)
        
        return list(anagram_hashmap.values())



            
