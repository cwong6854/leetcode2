# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Intuition: 
        # DFS -> relies alot on edge cases
        # if at node, compare all differences between node 1 and node 2
        # e.g. if node1.val != node2.val -> return False
        # e.g. if node1.left and not node2.left -> return False
        # e.g. if node1.right and not node2.right -> return False
        # e.g. if node2.left and not node1.left -> return False
        # e.g. if node2.right and not node2.right -> return False
        isSame = [True]
        def dfs(node1, node2):
            # if both are None?
            if not node1 and not node2:
                return True
            # if either one is None?
            if not node1 or not node2:
                return False
            # if either value does not match?
            if node1.val != node2.val:
                return False
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        isSame[0] = dfs(p, q)
        return isSame[0]
