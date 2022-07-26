from typing import Optional

from neetcode.tree.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, left, right):
            if not root:
                return True
            
            if not(root.val < right and root.val > left):
                return False
            
            return (valid(root.left, left, root.val) and valid(root.right, root.val, right))
        
        return valid(root, float('-inf'), float('inf'))