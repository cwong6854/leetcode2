# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p == q and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
    
if __name__ == "__main__":
    x = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    y = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    # x = TreeNode()
    # y = TreeNode()
    w = Solution()
    print(w.isSameTree(x, y))

        
    