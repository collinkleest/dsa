from typing import Optional

from neetcode.tree.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive DFS (depth first search) solution
        # base cases
        # O(N), memory complexity height of the tree O(N) where N is the height
        if not root: return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative DFS (depth first search) solution
        # level by level traversal
        # base case
        if not root: return 0
        
        level = 0
        queue = deque([root])
        
        while queue:
            
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative DFS (depth first search) solution
        # pre order
        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res