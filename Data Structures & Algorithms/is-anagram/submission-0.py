class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_hashmap = dict()
        t_hashmap = dict()

        for i in range(len(s)):
            s_hashmap[s[i]] = s_hashmap.get(s[i], 0) + 1
        for l in range(len(s)):
            t_hashmap[t[l]] = t_hashmap.get(t[l], 0) + 1
        if s_hashmap == t_hashmap:
            return True
        else:
            return False


        