class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        def checkTree(node, subnode):
            if not node and not subnode:
                return True
            elif not node and subnode or node and not subnode:
                return False
            return (node.val == subnode.val) and checkTree(node.left, subnode.left) and checkTree(node.right, subnode.right)

            
            

        def dfs(a, b):
            if not a:
                return False

            if a.val == b.val and checkTree(a, b):
                return True
            return dfs(a.left, b) or dfs(a.right,b)
        return dfs(root, subRoot)
            
            



if __name__ == "__main__":
    # tree = TreeNode(4, TreeNode(1), TreeNode(2))
    # subtree = TreeNode(4, TreeNode(1), TreeNode(2))
    tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subtree = TreeNode(4, TreeNode(1), TreeNode(2))
    # tree = TreeNode(1, left=TreeNode(1))
    # subtree = TreeNode(1)

    w = Solution()
    print(w.isSubtree(tree, subtree))
