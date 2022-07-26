from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if num in hash_map:
                return hash_map[num], i
            else:
                hash_map[diff] = i
        