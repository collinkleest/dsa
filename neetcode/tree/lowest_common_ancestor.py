from neetcode.tree.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        root_val = root.val
        
        p_val = p.val
        
        q_val = q.val
        
        # we need to traverse right side of tree
        if p_val > root_val and q_val > root_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # we need to traverse left side of tree
        elif p_val < root_val and q_val < root_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root