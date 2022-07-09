from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        
        while l < r:
            distance = r - l
            
            if height[l] > height[r]:
                area = height[r] * distance
                r -= 1
                
            else:
                area = height[l] * distance
                l += 1
                
            if area > maxArea:
                maxArea = area
        
        return maxArea