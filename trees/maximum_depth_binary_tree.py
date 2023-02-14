# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxDepth = 1
        def traverse(node, depth):
            count = 1
            if node.left:
                count = max(count, traverse(node.left, depth + 1))
            if node.right:
                count = max(count, traverse(node.right, depth + 1))
            print(count,depth)
            return max(count, depth)
        return traverse(root, maxDepth) if root else 0

if __name__ == "__main__":
    x = TreeNode(9, 
        
        TreeNode(9),TreeNode(20, TreeNode(15), TreeNode(7)))
    y = Solution()
    y.maxDepth(x)