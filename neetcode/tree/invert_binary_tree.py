from typing import Optional

from neetcode.tree.tree_node import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return root
        
        # recursively invert nodes
        # bsf (breath search first)
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        