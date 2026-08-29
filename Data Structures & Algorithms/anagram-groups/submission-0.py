class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs=[''.join(sorted(i)) for i in strs]
        indexes={}
        for i,value in enumerate(sorted_strs):
            indexes.setdefault(value, []).append(i)
        
        final_list=[]

        # print(indexes)
        
        for key, value in indexes.items():
            # print(key)
            key_list=[strs[i] for i in value]
            final_list.append(key_list)
        
        return final_list


            
