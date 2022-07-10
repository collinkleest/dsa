from typing import List


class Solution:
    
    # bruteforce solution
    def search(self, nums: List[int], target: int) -> int:
        
        for n in range(0, len(nums)):
            
            if nums[n] == target:
                return n
            
        return -1

    # optimal solution
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            
            # left sorted portion of array
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1 
                else:
                    r = m - 1
            # right sorted portion of array
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1 
                
        
        return -1
        
    

