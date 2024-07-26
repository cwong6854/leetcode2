# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Intuition:
        # make variable of balanced true -> default is True
        # dfs through the tree, and process node from bottom up
        # if the absolute diff between left and right is greater than 1, set res to False
        # for Each Node -> it's calculated as 1 + max(left, right)

        # Time Complexity:
        # O(n) -> visit each node
        
        # Space complexity: 
        # O(1)
        res = [True]
        def dfs(node):
            if not node:
                return -1 # returns height
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                res[0] = False
            return 1 + max(left, right)
        dfs(root)
        return res[0]
if __name__ == "__main__": 
    solution = Solution().isBalanced
    example = TreeNode(3, TreeNode(2), TreeNode(7, TreeNode(6), TreeNode(9)))
    assert(solution(example)==True)
    print("All test cases passed!")