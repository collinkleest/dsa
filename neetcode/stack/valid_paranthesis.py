class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToCloseMap = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c in openToCloseMap:
                if stack and stack[-1] == openToCloseMap[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        
        return True if not stack else False