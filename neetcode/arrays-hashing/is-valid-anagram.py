class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        tmap = {}
        smap = {}
        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i], 0) + 1
            tmap[t[i]] = tmap.get(t[i], 0) + 1
        
        return smap == tmap


    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        t = ''.join(sorted(t))
        s = ''.join(sorted(s))
        return s == t

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        schars = [0] * 26
        tchars = [0] * 26 
        
        for i in range(len(s)):
            schars[ord(s[i]) - ord('a')] += 1
            tchars[ord(t[i]) - ord('a')] += 1
        
        return tchars == schars        
