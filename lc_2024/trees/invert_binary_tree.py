# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Intuition
        # given a node, if left and right, then switch
        # Method
        # DFS -> Depth first search

        # Time complexity
        # O(n) -> visit each node

        # Space complexity: 
        # ~ O(log n)
        
        if root == None:
            return
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root
if __name__ == "__main__": 
    solution = Solution().invertTree
    example = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    expected = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))

    def checkSameTree(tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        if tree1.val != tree2.val:
            return False
        return checkSameTree(tree1.left, tree2.left) and checkSameTree(tree1.right, tree2.right)
    assert(checkSameTree(tree1=solution(example), tree2=expected)==True)
    print("All test cases passed!")
