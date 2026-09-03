class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dist={}
        if len(s) == len(t):
            for i in range(len(s)):
                char_dist[s[i]]=char_dist.get(s[i],0)+1 
                char_dist[t[i]]=char_dist.get(t[i],0)-1
            
            print(char_dist)

            if not any(char_dist.values()):
                return True;
            else:
                return False
        else:
            return False;
        