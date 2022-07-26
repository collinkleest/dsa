from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in strs_map:
                strs_map.get(sorted_str).append(s)
            else:
                strs_map[sorted_str] = [s]
        
        return strs_map.values()


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}
        
        for s in strs:
            char_count = [0] * 26
            
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            
            if tuple(char_count) in strs_map:
                strs_map.get(tuple(char_count)).append(s)
            else:
                strs_map[tuple(char_count)] = [s]
        
        return strs_map.values()