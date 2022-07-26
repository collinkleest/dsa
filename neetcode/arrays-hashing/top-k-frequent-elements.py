from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for i in range(len(nums) + 1)]
        hash_map = {}
        res = []
        
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        for key, val in hash_map.items():
            freq_list[val].append(key)
        
        for i in range(len(freq_list) - 1, -1, -1):
            for j in range(len(freq_list[i])):
                if len(res) == k:
                    return res
                res.append(freq_list[i][j])
        
        return res
        
                
            